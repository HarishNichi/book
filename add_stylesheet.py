import os

def add_stylesheet_to_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    if '<link rel="stylesheet" href="style.css">' not in content:
        content = content.replace('</head>', '    <link rel="stylesheet" href="style.css">\n</head>')
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Added stylesheet to {filename}")

# Add to index.html
add_stylesheet_to_file('index.html')

# Add to all page_XX.html files
for i in range(1, 61):
    filename = f"page_{i:02d}.html"
    add_stylesheet_to_file(filename)

print("All pages updated with stylesheet link.")
