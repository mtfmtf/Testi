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
  modus = 'a' if os.path.exists(f'{DIRECTORY}{filename}') else 'w'
  print(f'Modus:{modus}')
  sys.stdout=open(f'{DIRECTORY}{filename}',f'{modus}',newline='')
  if modus != 'a' : print(f'{HEADER}')

def restore_print():
  # sys.stdout.close()
  sys.stdout=sys.__stdout__

if __name__=="__main__":
    # print(f'TEST on {datetime.now().strftime("%Y%m%d-%H%M%S")}')
    time = datetime.now().strftime("%Y%m%d-%H%M%S")

    # update_last_run(time)
    # print_to_file('test.md')
    tabs = list()
    all = set()
    for file in os.listdir(f"..{os.sep}user"):
        if file.endswith("csv"):
            tabs.append(f'{file[0:len(file)-4]}')
            csv = f'..{os.sep}user{os.sep}{file}'
            print(f'\n## file {file[0:len(csv)-4]} found! It contents:\n')
            with open(f'{csv}', 'r') as f:
                a = f.readline()
                for i, line in enumerate(f, start=1):
                    line = line.replace('\n','')
                    line = line.replace(' ','')
                    if line not in all:
                        print(i, line)
                    else: print('DOPPELT')
                    all.add(line)
    print(f'last run: {time}\n{len(all)}')
    restore_print()
    update_nav(tabs)
