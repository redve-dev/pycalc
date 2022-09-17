import os
from sys import argv
from commands import edit, log, list_dir, help

MAIN_DIR = f"{os.environ['HOME']}/Programming/python/PYCALC"
EDITOR="nvim"

def switch_case(args):
    try:
        last = max(map(int, os.listdir(MAIN_DIR)))
    except ValueError:
        last=1

    match args[0]:
        case "new":
            edit(last+1)
        case "last":
            edit(last)
        case "log":
            log(args, last)
        case "edit":
            if len(args) <= 1:
                return
            edit(args[1])
        case 'list':
            list_dir()
        case "help":
            help()
        case _:
            print('unrecognized command, exec "pycalc help" to get list of available commands')

def main():
    _, *instructions = argv
    if not instructions:
        print('exec "pycalc help" to get list of available commands\n')
        return

    if not os.path.isdir(MAIN_DIR):
        os.mkdir(MAIN_DIR)
    switch_case(instructions)

if __name__ == '__main__':
    main()
