import os
import re

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
                page_content_match = re.search(r'<div class="page-content">(.*?)</div>', content, re.DOTALL)
                if page_content_match:
                    page_content = page_content_match.group(1)
                else:
                    body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
                    if body_match:
                        page_content = body_match.group(1)
                        # remove nav and script tags
                        page_content = re.sub(r'<nav.*?</nav>', '', page_content, flags=re.DOTALL)
                        page_content = re.sub(r'<script.*?</script>', '', page_content, flags=re.DOTALL)

                with open('index.html', 'a') as f:
                    f.write(f'<div id="page-{i}" class="page-content-container">')
                    f.write(page_content)
                    f.write('</div>\n')

    with open('index.html', 'a') as f:
        f.write("""
    </main>
    <script src="main.js" defer></script>
</body>
</html>
""")

create_single_page()
print("Single page created successfully!")
