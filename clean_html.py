import re

def clean_html():
    with open('index.html', 'r') as f:
        content = f.read()

    # 1. Replace old title
    content = content.replace('The Orphan\'s Shadow', 'Child of the Crimson Pendant')

    # 2. Make page titles consistent (h2)
    content = re.sub(r'<h1>(Child of the Crimson Pendant - Page \d+)</h1>', r'<h2>\1</h2>', content)

    # 3. Remove container and scene divs
    content = content.replace('<div class="container">', '')
    content = content.replace('<div class="scene">', '')
    content = content.replace('</div>', '') # This is a bit risky, but should work for this case

    # 4. Remove pagination divs
    content = re.sub(r'<div class="pagination">.*?</div>', '', content, flags=re.DOTALL)

    # 5. Remove extra body tags
    content = content.replace('<body>', '')
    content = content.replace('</body>', '')

    # Remove extra nav tags
    content = re.sub(r'<nav.*?</nav>', '', content, flags=re.DOTALL)


    with open('index.html', 'w') as f:
        f.write(content)

clean_html()
print("HTML cleaned successfully!")
