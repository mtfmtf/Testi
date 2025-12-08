import os, sys

FILE=f'docs{os.sep}_includes{os.sep}nav.html'
# FILE=f'..{os.sep}docs{os.sep}_includes{os.sep}nav.html'

def update_nav(time):
    with open(f'{FILE}', 'w') as new_nav:
        new_nav.write('<nav style="margin-bottom: 20px;"> <a href="home.html">home</a> |  <a href="seite2.html">seite '
                      '2</a> | <a href="seite3.html">seite 3</a> | <a href="test.html">test file</a> </nav>')
        new_nav.write(f'<font color="#FF0000"><b>last update: {time}</b></font><font color="#CDCD00">\n')
