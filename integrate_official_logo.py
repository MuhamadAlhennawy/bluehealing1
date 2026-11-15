import base64
import re

# Read the logo image and convert to base64 Data URI
with open("logo.jpg", "rb") as f:
    b64_data = base64.b64encode(f.read()).decode("utf-8")

logo_data_uri = f"data:image/jpeg;base64,{b64_data}"

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Favicon in <head>
favicon_tag = f'<link rel="icon" type="image/jpeg" href="{logo_data_uri}">'
if 'rel="icon"' not in html:
    html = html.replace('<title>', favicon_tag + '\n    <title>')

# 2. Add brand-logo-img styling to <style>
logo_css = """
        .brand-logo-img {
            width: 50px;
            height: 50px;
            border-radius: 12px;
            object-fit: cover;
            box-shadow: 0 4px 12px rgba(0, 43, 73, 0.15);
            border: 1.5px solid #E2E8F0;
            background: #FFFFFF;
            flex-shrink: 0;
            transition: transform 0.3s ease;
        }
        .brand-logo-img:hover { transform: scale(1.05); }

        .wellness-pillars-bar {
            background: linear-gradient(135deg, #002B49 0%, #004B87 100%);
            border-radius: var(--radius-lg);
            padding: 24px 28px;
            color: white;
            margin: 30px auto;
            box-shadow: var(--shadow-md);
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
        }
        .pillar-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 6px;
            flex: 1;
            min-width: 110px;
        }
        .pillar-icon {
            font-size: 24px;
            background: rgba(255, 255, 255, 0.15);
            width: 46px;
            height: 46px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(255, 255, 255, 0.25);
        }
        .pillar-title {
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 0.3px;
        }
        .pillar-desc {
            font-size: 10px;
            color: #CBD5E1;
            line-height: 1.3;
        }
"""
html = html.replace('.brand-logo-badge {', logo_css + '\n        .brand-logo-badge {')

# 3. Replace the placeholder BH div in the header with the official logo
old_logo_markup = '<div class="brand-logo-badge">BH</div>'
new_logo_markup = f'<img class="brand-logo-img" src="{logo_data_uri}" alt="Blue Healing Official Logo" id="mainHeaderLogo">'
html = html.replace(old_logo_markup, new_logo_markup)

# 4. Also add the logo in the Manager Control Bar
old_mgr_info = '<div class="manager-info">\n                    <span>🔐 لوحة تحكم الإدارة والمشرف:</span>'
new_mgr_info = f"""<div class="manager-info" style="gap: 12px;">
                    <img src="{logo_data_uri}" alt="Logo" style="width: 36px; height: 36px; border-radius: 8px; border: 1px solid #F59E0B; background: white; object-fit: cover;">
                    <span>🔐 لوحة تحكم الإدارة والمشرف:</span>"""
html = html.replace(old_mgr_info, new_mgr_info)

# 5. Add the 5 Wellness Pillars Bar under the Hilton Amenities Box in Customer View
wellness_pillars_html = f"""
            <!-- 5 Wellness Pillars of Blue Healing (Matching Official Logo Icons) -->
            <div class="wellness-pillars-bar">
                <div style="display: flex; align-items: center; gap: 14px; border-left: 1px solid rgba(255,255,255,0.2); padding-left: 20px;">
                    <img src="{logo_data_uri}" alt="Blue Healing Logo" style="width: 60px; height: 60px; border-radius: 12px; background: white; padding: 4px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
                    <div>
                        <div style="font-size: 11px; font-weight: 800; color: #F59E0B; letter-spacing: 1px;">THE 5 PILLARS OF HEALTH</div>
                        <div style="font-size: 15px; font-weight: 900;">ركائز الاستشفاء والعافية الخمسة</div>
                    </div>
                </div>

                <div class="pillar-item">
                    <div class="pillar-icon">📵</div>
                    <div class="pillar-title">ديتوكس رقمي</div>
                    <div class="pillar-desc">Digital Detox والتخلص من التوتر الذهني</div>
                </div>

                <div class="pillar-item">
                    <div class="pillar-icon">⏳</div>
                    <div class="pillar-title">نحت وشد القوام</div>
                    <div class="pillar-desc">Body Sculpting & Toning بحصص يومية</div>
                </div>

                <div class="pillar-item">
                    <div class="pillar-icon">⚖️</div>
                    <div class="pillar-title">توازن الوزن الصحي</div>
                    <div class="pillar-desc">Weight Management ومتابعة مستمرة</div>
                </div>

                <div class="pillar-item">
                    <div class="pillar-icon">☕🚫</div>
                    <div class="pillar-title">تنقية الجسم والسموم</div>
                    <div class="pillar-desc">Cleansing & Detox وتجديد النشاط الحيوي</div>
                </div>

                <div class="pillar-item">
                    <div class="pillar-icon">🛡️🥗</div>
                    <div class="pillar-title">تغذية وقائية ذكية</div>
                    <div class="pillar-desc">Protective Nutrition ووجبات عضوية طازجة</div>
                </div>
            </div>
"""

amenities_end = '<!-- Search and Category Navigation -->'
if 'class="wellness-pillars-bar"' not in html:
    html = html.replace(amenities_end, wellness_pillars_html + '\n            ' + amenities_end)

# 6. Store official logo in JavaScript state for future references
html = html.replace('const defaultResortSettings = {', f'const OFFICIAL_LOGO_URI = "{logo_data_uri}";\n    const defaultResortSettings = {{')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Official logo integrated into index.html successfully!")
