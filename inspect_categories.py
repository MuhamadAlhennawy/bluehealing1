with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Let's inspect categories functions
def show_func(name):
    idx = text.find(f'function {name}')
    if idx != -1:
        print(f"\n==================== {name} ====================")
        print(text[idx:idx+1500])

show_func('openCategoriesManagerModal')
show_func('saveCategoryFromForm')
show_func('startEditCategory')
show_func('deleteCategory')
show_func('renderCategorySelectOptions')
show_func('renderCategoryPills')
