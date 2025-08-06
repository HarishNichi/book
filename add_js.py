import os

def add_js_to_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    if '<script src="main.js" defer></script>' not in content:
        content = content.replace('</body>', '    <script src="main.js" defer></script>\n</body>')
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Added JS to {filename}")

# Add to index.html
add_js_to_file('index.html')

# Add to all page_XX.html files
for i in range(1, 61):
    filename = f"page_{i:02d}.html"
    add_js_to_file(filename)

print("All pages updated with JS script tag.")
