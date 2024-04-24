# learn-llamaindex

- The idea of this project to understand core concepts of LlamaIndex
- `main.py` will lead you to couple of different approaches which are local and openai
- One of them can be used for your personal data which i used for my own obsidian

## Prepare local environment

- 'brew install ollama'
- 'ollama pull mistral'
- 'ollama serve'

## Prepare for your obsidian

- Create `.env` file in root directory
- Copy the path of your obsidian vault folder. example: `OBSIDIAN_VAULT_FOLDER='/Users/xxx/obsidian-vault'`
- Create virtual development environment by executing 'python3 -m venv .venv'
- Activate the virtual environment `source .venv/bin/activate`
- Install packages `pip install -r requirements.txt`
- Run main `python3 main.py`