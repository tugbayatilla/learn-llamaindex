import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.mylogging import show_log, LogLevel, log
show_log(LogLevel.INFO)


from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama


# bge embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")
# ollama
Settings.llm = Ollama(model="mistral", request_timeout=30.0)


PERSIST_DIR = ".storage"
if not os.path.exists(PERSIST_DIR):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)
    log('Persisted')
else:
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
    log('Persisted data loaded')


query_engine = index.as_query_engine()

while True:
    print('What is your question? example:  What did the quthor do growing up?')
    question = input('?> ')
    if not question:
        print('Exiting...')
        break

    print('The question is: ', question)

    response = query_engine.query(question)
    print(response)
