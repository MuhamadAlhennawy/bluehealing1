with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for test_id in ['topNavActions', 'roleBadge', 'categoriesFilterBar', 'customerSearchInput', 'menuSearchInput', 'customerCategoryPills']:
    count_html = text.count(f'id="{test_id}"')
    count_js = text.count(f'getElementById("{test_id}")') + text.count(f"getElementById('{test_id}')")
    print(f"ID '{test_id}': in HTML = {count_html}, in JS = {count_js}")
