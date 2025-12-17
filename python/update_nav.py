import os, sys, datetime

UPDATE=f'docs{os.sep}_includes{os.sep}update.html'
NAV=f'..{os.sep}docs{os.sep}_includes{os.sep}navu.html'

def update_last_run(time):
    with open(f'{UPDATE}', 'w') as new_update:
        new_update.write(f'<span style="color: #FF0000; font-weight: bold; margin-bottom: 10px">last update: {time} </span>')

def update_nav(tabs):
    print('updating nav')
    print(tabs)
    with open(f'{NAV}', 'w', newline='\n') as new_nav:
        new_nav.write('<nav style="margin-bottom: 20px;">\n\t<a href="home.html">home</a>')
        for i, e in enumerate(tabs,start=1):
            new_nav.write(f'\t| <a href="{e}.html">seite {i}</a>')
        new_nav.write('</nav>\n{% include update.html%}')
        create_base_md(name in tabs)

def create_base_md(name):
    with open(f'..{os.sep}{name}.md', 'w', newline='\n') as md:
        md.write('---')
        md.write('---')
        s = '{% include_relative pages/'+name+'.md %}'
        md.write(s)




'''<nav style="margin-bottom: 20px;"> 
    <a href="home.html">home</a> |  
    <a href="page2.html">seite 2</a> | 
    <a href="page3.html">seite 3</a> | 
    <a href="test.html">test file</a> |
    <a href="cal.html">calender</a> |
</nav>
{% include update.html%}
'''