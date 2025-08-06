import os
import re

def replace_image_in_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Find all img tags
    img_tags = re.findall(r'<img.*?>', content)

    for img_tag in img_tags:
        # Extract alt text
        alt_match = re.search(r'alt="(.*?)"', img_tag)
        alt_text = alt_match.group(1) if alt_match else "Placeholder"

        # Create new img tag
        new_img_tag = f'<img src="https://via.placeholder.com/800x600?text={alt_text.replace(" ", "+")}" alt="{alt_text}" class="story-image">'

        # Replace old img tag
        content = content.replace(img_tag, new_img_tag)

    with open(filename, 'w') as f:
        f.write(content)

# Replace in all page_XX.html files
for i in range(1, 61):
    filename = f"page_{i:02d}.html"
    if os.path.exists(filename):
        replace_image_in_file(filename)

print("All images replaced with placeholders.")
