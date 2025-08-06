import os

def add_toc():
    with open('index.html', 'r') as f:
        content = f.read()

    toc = '<div class="table-of-contents">\n<h2>Table of Contents</h2>\n<ol>\n'
    for i in range(1, 61):
        toc += f'<li><a href="#page-{i}">Page {i}</a></li>\n'
    toc += '</ol>\n</div>'

    content = content.replace('</header>', '</header>\n' + toc)

    with open('index.html', 'w') as f:
        f.write(content)

add_toc()
print("Table of Contents added successfully!")
