with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

def show_func(name):
    idx = text.find(f'function {name}')
    if idx != -1:
        print(f"\n==================== {name} ====================")
        print(text[idx:idx+900])

show_func('showManagerView')
show_func('openLoginModal')
show_func('executeLogin')
