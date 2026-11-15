with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script[\s\S]*?</script>', text)
js_code = scripts[1].replace('<script>', '').replace('</script>', '')

print("Total JS characters:", len(js_code))

# Check functions related to adding meals and editing categories
check_funcs = [
    'createNewMeal',
    'duplicateCurrentMeal',
    'deleteCurrentMeal',
    'openCategoriesManagerModal',
    'closeCategoriesManagerModal',
    'renderCategoriesTable',
    'saveCategoryFromForm',
    'deleteCategory',
    'updateActiveMealField',
    'renderCustomerMenu',
    'renderTabs',
    'renderActiveMeal'
]

for fn in check_funcs:
    count = js_code.count(f'function {fn}')
    print(f'function {fn}: {count}')

# Check for undefined variables or broken replacements
# Let's inspect where createNewMeal is defined
idx = js_code.find('function createNewMeal')
if idx != -1:
    print("\n--- createNewMeal definition ---")
    print(js_code[idx:idx+600])

idx_cat = js_code.find('function openCategoriesManagerModal')
if idx_cat != -1:
    print("\n--- openCategoriesManagerModal definition ---")
    print(js_code[idx_cat:idx_cat+600])
