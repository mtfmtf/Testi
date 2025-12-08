import sys, os
from update_nav import *
from datetime import datetime

'''
file tree in docker by now
app
|- user -> csv with user data
    |- list.csv
|- docs -> for md-files
    |- _includes: 
        |-nav.html
        |-update.html
test.py

'''

DIRECTORY=f'docs{os.sep}'
HEADER='---\n---\n{% include nav.html %}'

def print_to_file(filename):
  sys.stdout.flush()
  modus = 'a' if os.path.exists(f'{DIRECTORY}{filename}') else 'wt'
  print(f'Modus:{modus}')
  sys.stdout=open(f'{DIRECTORY}{filename}',f'{modus}')
  if modus != 'a' : print(f'{HEADER}')

def restore_print():
  sys.stdout.close()
  sys.stdout=sys.__stdout__

if __name__=="__main__":
    # print(f'TEST on {datetime.now().strftime("%Y%m%d-%H%M%S")}')
    time = datetime.now().strftime("%Y%m%d-%H%M%S")

    update_nav(time)
    print_to_file('test.md')

    for file in os.listdir("user"):
        if file.endswith("csv"):
            csv = f'user{os.sep}{file}'
            print(f'file {csv} found! It contents:')
            with open(f'{csv}', 'r') as f:
                a = f.readline()
                for i, line in enumerate(f, start=1):
                    print(i, line)
    print(f'last run: {time}\n')
    restore_print()