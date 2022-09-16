from pathlib import Path
from io import StringIO
from contextlib import redirect_stdout
import os
from datetime import datetime

def execute_code(path, ):
    s=StringIO()
    with redirect_stdout(s):
        # try catch block avoided intentionally, user should get debugging information about his code
        exec(open(path+"/main.py").read())
    with open(path+'/logs', 'a') as f:
        print(s.getvalue())
        f.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S"+'\n'))
        f.write('='*50+'\n')
        f.write(s.getvalue())
        f.write('\n'+'='*50+'\n')

def edit_code(path):
    file = "%s/main.py" % path
    if not os.path.exists(file):
        Path(file).touch()
    from main import EDITOR
    os.system(EDITOR+' '+file)
    execute_code(path)

def log_file(id):
    from main import MAIN_DIR
    file = "%s/%s/logs" % (MAIN_DIR, id)
    with open(file, 'r') as f:
        for line in f:
            print(line.strip())

def edit(last):
    from main import MAIN_DIR
    path="%s/%s" % (MAIN_DIR, str(last))
    if not os.path.exists(path):
        os.mkdir(path)
    edit_code(path)

def log(args, last):
        if len(args) < 2:
            log_file(last)
            return
        from main import MAIN_DIR
        if not os.path.exists("%s/%s/logs" % (MAIN_DIR, args[1])):
            print("pycalc %s does not exist" % args[1])
            return
        log_file(args[1])

def list_dir():
    from main import MAIN_DIR
    for id in sorted(os.listdir(MAIN_DIR)):
        print(id)

def help():
    print('''
the program allows you to create code in python, execute it, and save the logs

usage: pycalc [OPTION]

options:
    new - create code, execute it, and save output to logs
    edit [id] - edit code, and execute it
    last - edit recently created code
    log [id] - print logs of chosen pycalc. If none id is provided, it prints most recent file logs
    list - print list of available files
    help - print this menu''')
