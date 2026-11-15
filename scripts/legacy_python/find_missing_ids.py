with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find all document.getElementById("...")
get_ids = re.findall(r'document\.getElementById\(["\']([^"\']+)["\']\)', text)
unique_get_ids = set(get_ids)

# Find all id="..." in HTML
html_ids = set(re.findall(r'id=["\']([^"\']+)["\']', text))

missing_ids = []
for gid in sorted(unique_get_ids):
    if gid not in html_ids:
        missing_ids.append(gid)

print("Total getElementById calls:", len(get_ids))
print("Unique IDs queried in JS:", len(unique_get_ids))
print("Missing IDs that DO NOT exist in HTML:")
for mid in missing_ids:
    print(f"  - '{mid}'")
