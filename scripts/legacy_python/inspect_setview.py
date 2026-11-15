with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find('function setView')
if idx != -1:
    print(text[idx:idx+1200])
