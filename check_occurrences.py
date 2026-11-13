with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for test_id in ['roleBadge', 'categoriesFilterBar', 'customerSearchInput']:
    matches = [m.start() for m in re.finditer(test_id, text)]
    print(f"\nOccurrences of '{test_id}': {len(matches)}")
    for m in matches:
        start = max(0, m - 40)
        end = min(len(text), m + 80)
        print("  ...", text[start:end].replace('\n', ' '), "...")
