with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

if 'id="roleBadge"' not in html:
    html = html.replace('<header class="hotel-main-header">', '<span id="roleBadge" style="display:none;"></span>\n    <header class="hotel-main-header">')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Added hidden roleBadge element for full backwards-compatibility!")
