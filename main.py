from dotenv import load_dotenv
load_dotenv()

import os
from Command import Command
from starter import run, setup_for_local

while True:
    print(f'write {', '.join([f"{data.value} for {data.name}" for data in Command])} ')
    selection = input('?> ')

    match Command(selection):
        case Command.LOCAL:
            setup_for_local()
            run(Command.LOCAL, 'data')
        case Command.MYOBSIDIAN:
            obsidian_vault_folder = os.getenv('OBSIDIAN_VAULT_FOLDER')
            if not obsidian_vault_folder:
                raise ValueError('OBSIDIAN_VAULT_FOLDER must be given in environment variables. Create a .env file and set in it.')
            setup_for_local()
            run(Command.MYOBSIDIAN, obsidian_vault_folder)
        case Command.OPENAI:
            run(Command.OPENAI, 'data')
        case Command.EXIT:
            print('Exiting...')
            break
        