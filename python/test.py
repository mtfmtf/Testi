import sys
import os
from datetime import datetime

#DIRECTORY=f'..{os.sep}docs{os.sep}'
DIRECTORY=f'cfp{os.sep}'
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
  print(f'TEST on {datetime.now().strftime("%Y%m%d-%H%M%S")}')
  print_to_file('test.md')
  print(f'last run: {datetime.now().strftime("%Y%m%d-%H%M%S")}\n')
  
