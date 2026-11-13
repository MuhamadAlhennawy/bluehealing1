with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

def show_func(name):
    idx = text.find(f'function {name}')
    if idx != -1:
        print(f"\n==================== {name} ====================")
        print(text[idx:idx+1200])

show_func('filterCustomerMenu')
show_func('renderActiveMeal')
show_func('renderTabs')
show_func('createNewMeal')
