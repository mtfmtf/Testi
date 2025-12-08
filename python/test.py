import sys
import os
from datetime import datetime

'''
file tree in docker by now
app
|-user -> csv with user data
|-docs -> for md-files
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
  print_to_file('test.md')
  print(f'last run: {datetime.now().strftime("%Y%m%d-%H%M%S")}\n')
  restore_print()
  for file in os.listdir("user"):
      if file.endswith("csv"):
          ff = f'user{os.sep}{file}'
          with open(f'{ff}', 'r') as f:
              a = f.readline()
              while a:
                  print(a)
                  a = f.readline()