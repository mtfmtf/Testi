import os


# file names/locations
HEADER = '---\n---\n'
HEADER_NAV = HEADER + '{% include nav.html %}'

DIRECTORY = f'docs{os.sep}'
INCLUDE = DIRECTORY + f'_includes{os.sep}'
NAV=f'{INCLUDE}nav.html'
UPDATE=f'{INCLUDE}update.html'
PAGES=f'{DIRECTORY}pages{os.sep}'


def create_base_md(name, page):
    # with open(f'..{os.sep}{DIRECTORY}{name}.md', 'w', newline='\n') as md:
    with open(f'{DIRECTORY}{name}.md', 'w', newline='\n') as md:
        md.write(HEADER)
        s = '{% include_relative pages/'
        s += f'{page}'
        s += '.md %}'
        md.write(f'{s}')

def create_page_md(name, content: list):
    print(f'YOUR CONTENT IN {PAGES}{name}.md')
    # with open(f'..{os.sep}{PAGES}{name}.md', 'w', newline='\n') as md:
    with open(f'{PAGES}{name}.md', 'w', newline='\n') as md:
        md.write(f'{HEADER}')
        md.write('<nav style="margin-bottom: 20px;"> <a href="home.html">home</a></nav>\n')
        md.write(f'# <span style="color: #FF0000; font-weight: bold; margin-bottom: 10px">{name}s list </span>\n')
        for e in content:
            md.write(e+'\n')

def update_last_run(time):
    with open(f'{UPDATE}', 'w') as new_update:
        new_update.write(f'<span style="color: #FF0000; font-weight: bold; margin-bottom: 10px">last update: {time} </span>')

def update_nav(tabs: list):
    print('updating nav')
    with open(f'{NAV}', 'w', newline='\n') as new_nav:
        new_nav.write('<nav style="margin-bottom: 20px;">\n\t<a href="home.html">home</a>')
        for i, e in enumerate(tabs,start=1):
            new_nav.write(f'\t| <a href="base_{i}.html">{e}</a>')
            create_base_md(f'base_{i}',f'{e}')
        new_nav.write('</nav>\n{% include update.html %}\n')