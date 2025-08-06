import os
import re

def update_page(i):
    filename = f"page_{i:02d}.html"
    with open(filename, 'r') as f:
        content = f.read()

    # Fix stylesheet link
    content = content.replace('/workspace/style.css', 'style.css')
    content = content.replace('/style.css', 'style.css')


    # Create new nav
    prev_page = f"page_{i-1:02d}.html"
    next_page = f"page_{i+1:02d}.html"

    nav = '<nav class="sticky-nav">\n'
    if i > 1:
        nav += f'        <a href="{prev_page}">Previous Page</a>\n'
    nav += '        <a href="index.html">Home</a>\n'
    if i < 60:
        nav += f'        <a href="{next_page}">Next Page</a>\n'
    nav += '    </nav>'

    # Replace old nav
    new_content, count = re.subn(r'<nav.*?</nav>', nav, content, flags=re.DOTALL)

    if count == 0:
        # If no nav was found, add it before the body tag
        new_content = content.replace('</body>', nav + '\n</body>')

    with open(filename, 'w') as f:
        f.write(new_content)

for i in range(1, 61):
    update_page(i)

print("All pages updated successfully!")
