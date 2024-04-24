import os
from Command import Command
from mylogging import register_log, LogLevel, log
register_log(LogLevel.INFO)

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama

def setup_for_local():
    Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")
    Settings.llm = Ollama(model="mistral", request_timeout=30.0)

def run(command: Command, folder):
    PERSIST_DIR = f".storage_for_{command.name.lower()}"
    if not os.path.exists(PERSIST_DIR):
        documents = SimpleDirectoryReader(folder).load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        log(f'Persisted into {PERSIST_DIR}')
    else:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
        log(f'Persisted data loaded from {PERSIST_DIR}')


    query_engine = index.as_query_engine()

    while True:
        print('What is your question?')
        question = input('?> ')
        if not question:
            print('Exiting...')
            break

        print('The question is: ', question)

        response = query_engine.query(question)
        print("The answer is: ")
        print(response)
