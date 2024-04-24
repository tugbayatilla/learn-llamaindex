from utils.mylogging import *
class Command(Enum):
    LOCAL = 'local'
    OPENAI = 'openai'
    EXIT = 'exit'
    MYOBSIDIAN = 'my'

while True:
    print(f'write {', '.join([f"{data.value} for {data.name}" for data in Command])} ')
    selection = input('?> ')

    match selection:
        case Command.LOCAL.value:
            import local_models.starter as local_starter
            local_starter
        case Command.OPENAI.value:
            import openai_models.starter as openai_starter
            openai_starter
        case Command.MYOBSIDIAN.value:
            import my_obsidian.starter as my_obsidian_starter
            my_obsidian_starter
        case Command.EXIT.value:
            print('Exiting...')
            break
        