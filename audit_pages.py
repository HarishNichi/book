import os
import re

def audit_pages():
    issues_found = False
    for i in range(1, 61):
        filename = f"page_{i:02d}.html"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                content = f.read()

            # Check for title
            if not re.search(r'<h[1-2]>.*?</h[1-2]>', content, re.DOTALL):
                print(f"Page {i}: Missing title.")
                issues_found = True

            # Check for content length
            body_match = re.search(r'<body.*?>(.*?)</body>', content, re.DOTALL)
            if body_match:
                body_content = body_match.group(1)
                # Remove tags for a more accurate content length check
                body_content = re.sub(r'<.*?>', '', body_content, flags=re.DOTALL)
                if len(body_content.strip()) < 100:
                    print(f"Page {i}: Low content length.")
                    issues_found = True
            else:
                print(f"Page {i}: Missing body tag.")
                issues_found = True

    if not issues_found:
        print("No issues found.")

audit_pages()
