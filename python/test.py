import sys, os
from file_updater import *
from datetime import datetime

'''
file tree in repo by now
root
|- user -> csv with user data
    |- name1.csv
    |- name2.csv
    |- name3.csv
|- docs -> for md-files
    |- home.md
    |- all.md           // data from UNION name in user
    |- base_x.md        // one for file in user
    |- pages 
        |-page_x.html   // one for base_?.md in docs
    |- _includes: 
        |-nav.html
        |-update.html
test.py

'''


def print_to_file(filename):
  sys.stdout.flush()
  modus = 'w'
  # modus = 'a' if os.path.exists(f'{DIRECTORY}{filename}') else 'w'
  print(f'Modus:{modus}')
  sys.stdout=open(f'..{os.sep}{DIRECTORY}{filename}',f'{modus}',newline='\n')
  print(f'{HEADER_NAV}\n')

def restore_print():
  # sys.stdout.close()
  sys.stdout=sys.__stdout__

if __name__=="__main__":
    # print(f'TEST on {datetime.now().strftime("%Y%m%d-%H%M%S")}')
    time = datetime.now().strftime("%Y%m%d-%H%M%S")

    tabs = list()
    all = set()
    crop = set()

    for file in sorted(os.listdir(f"..{os.sep}user")):
        if file.endswith("csv"):
            tabs.append(f'{file[0:len(file)-4]}')
            csv = f'..{os.sep}user{os.sep}{file}'
            print(f'\n## file {file[0:len(csv)-4]} found! It contents:\n')
            with (open(f'{csv}', 'r') as f):
                a = f.readline()
                tmp = list()
                for i, line in enumerate(f, start=1):
                    cropped_line = line.replace('\n','')
                    cropped_line = cropped_line.replace(' ','')
                    if cropped_line not in crop:
                        print(i, line)
                        all.add(line)
                    tmp.append(line)
                    crop.add(cropped_line)
                create_page_md(f'{file[0:len(file)-4]}',sorted(tmp))

    update_last_run(time)
    update_nav(tabs)

    print_to_file('all.md')
    for e in sorted(list(all)):
        a = e.rsplit(', http')
        print(a[0]+'\n')
    restore_print()

