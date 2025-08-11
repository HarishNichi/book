import os
import re

def extract_content(filename):
    """Extracts the main story content from a page's HTML."""
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as page_file:
        content = page_file.read()
        # First, try to find a specific story content div
        match = re.search(r'<div class="story-content">(.*?)</div>', content, re.DOTALL)
        if match:
            return match.group(1).strip()

        # Fallback to the page-content div
        match = re.search(r'<div class="page-content">(.*?)</div>', content, re.DOTALL)
        if match:
            return match.group(1).strip()

        # Fallback to the whole body if specific divs aren't found
        body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
        if body_match:
            page_content = body_match.group(1)
            # Clean up common boilerplate tags
            page_content = re.sub(r'<nav.*?</nav>', '', page_content, flags=re.DOTALL)
            page_content = re.sub(r'<script.*?</script>', '', page_content, flags=re.DOTALL)
            page_content = re.sub(r'<div class="pagination">.*?</div>', '', page_content, flags=re.DOTALL)
            page_content = re.sub(r'<h1>.*?</h1>', '', page_content, flags=re.DOTALL)
            return page_content.strip()
    return None

def create_final_page():
    """Generates the final index.html from all story pages."""
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

    # Process pages 1 to 60
    page_order = list(range(1, 61))

    # Add bridge pages
    page_order.extend(['60a', '60b', '60c'])

    # Add pages 61 to 150
    page_order.extend(list(range(61, 151)))

    for page_num in page_order:
        # Format page number for filename
        if isinstance(page_num, int):
            filename = f"page_{page_num:02d}.html"
        else:
            filename = f"page_{page_num}.html"

        page_content = extract_content(filename)
        if page_content:
            with open('index.html', 'a') as f:
                f.write(f'<div id="page-{page_num}" class="page-content-container">')
                f.write(page_content)
                f.write('</div>\n')
        else:
            print(f"Warning: Could not find or process content for {filename}")

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

if __name__ == "__main__":
    create_final_page()
    print("Final single page created successfully!")
