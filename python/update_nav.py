import os, sys

FILE=f'docs{os.sep}_includes{os.sep}update.html'

def update_nav(time):
    with open(f'{FILE}', 'w') as new_nav:
        new_nav.write(f'<span style="color: #FF0000; font-weight: bold; margin-left: 10px">last update: {time} </span>\n')
