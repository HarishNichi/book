import os

def add_pagination_controls():
    with open('index.html', 'r') as f:
        content = f.read()

    pagination_controls = """
    <div class="pagination-controls">
        <button id="prev-page">Previous</button>
        <span id="page-number">Page 1</span>
        <button id="next-page">Next</button>
    </div>
"""

    content = content.replace('</main>', '</main>\n' + pagination_controls)

    with open('index.html', 'w') as f:
        f.write(content)

add_pagination_controls()
print("Pagination controls added successfully!")
