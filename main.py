import os
from sys import argv
from commands import edit, log, list_dir, help

MAIN_DIR = "%s/Programming/python/PYCALC" % os.environ['HOME']
EDITOR="nvim"

def switch_case(args):
    try:
        last = max((int(i) for i in os.listdir(MAIN_DIR)))
    except ValueError:
        last=1

    if args[0] == "new":
        return edit(last+1)
    if args[0] == "last":
        return edit(last)
    if args[0] == "log":
        return log(args, last)
    if args[0] == "edit":
        if len(args) <= 1:
            return
        return edit(args[1])
    if args[0] == 'list':
        return list_dir()
    if args[0] == "help":
        return help()

def main():
    _, *instructions = argv
    if not instructions:
        print("exec \"pycalc help\" to get list of available commands\n")
        return

    if not os.path.isdir(MAIN_DIR):
        os.mkdir(MAIN_DIR)
    switch_case(instructions)

if __name__ == '__main__':
    main()
