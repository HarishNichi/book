import os
import re

def clean_html_content(content, page_num):
    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
    if body_match:
        content = body_match.group(1)

    # Remove unwanted tags
    content = re.sub(r'<nav.*?</nav>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<header.*?</header>', '', content, flags=re.DOTALL)
    content = re.sub(r'<footer.*?</footer.*>', '', content, flags=re.DOTALL)
    content = re.sub(r'<body>', '', content, flags=re.DOTALL)
    content = re.sub(r'</body>', '', content, flags=re.DOTALL)
    content = re.sub(r'<html>', '', content, flags=re.DOTALL)
    content = re.sub(r'</html>', '', content, flags=re.DOTALL)

    # Make titles consistent
    if not re.search(r'<h[1-2]>', content):
        content = f'<h2>Page {page_num}</h2>\n{content}'
    else:
        content = re.sub(r'<h1>(.*?)</h1>', r'<h2>\1</h2>', content)

    # Replace old title
    content = content.replace('The Orphan\'s Shadow', 'Child of the Crimson Pendant')

    return content

def create_single_page():
    with open('index.html', 'w') as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Child of the Crimson Pendant</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Child of the Crimson Pendant</h1>
    </header>
    <main>
""")

    for i in range(1, 61):
        filename = f"page_{i:02d}.html"
        if os.path.exists(filename):
            with open(filename, 'r') as page_file:
                content = page_file.read()
                cleaned_content = clean_html_content(content, i)
                with open('index.html', 'a') as f:
                    f.write(f'<div id="page-{i}" class="page-content-container">')
                    f.write(cleaned_content)
                    f.write('</div>\n')

    with open('index.html', 'a') as f:
        f.write("""
    </main>
    <div class="pagination-controls">
        <button id="prev-page">Previous</button>
        <span id="page-number">Page 1</span>
        <button id="next-page">Next</button>
    </div>
    <script src="main.js" defer></script>
</body>
</html>
""")

create_single_page()
print("Single page created successfully!")
