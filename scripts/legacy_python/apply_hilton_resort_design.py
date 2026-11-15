import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Define the Mediterranean Luxury Resort CSS and Layout
hilton_theme_css = """
        /* ======================================================== */
        /* HILTON LUXURY 5-STAR MEDITERRANEAN RESORT STYLING       */
        /* ======================================================== */
        :root {
            --brand-dark: #002B49;
            --brand-primary: #004B87;
            --brand-blue: #0072CE;
            --brand-cyan: #0284C7;
            --brand-gold: #B8860B;
            --brand-gold-light: #FBF6EB;
            --brand-sand: #F7F5F2;
            --brand-sand-dark: #ECE7DE;
            --greek-blue: #005A9C;
            --greek-blue-light: #EBF3FA;
            --kids-pink: #E11D48;
            --kids-pink-bg: #FFF1F2;
            --success: #059669;
            --success-light: #ECFDF5;
            --danger: #DC2626;
            --danger-light: #FEF2F2;
            --bg-page: #FFFFFF;
            --bg-card: #FFFFFF;
            --border: #E2E8F0;
            --text-main: #1A202C;
            --text-muted: #5A6A80;
            --radius-lg: 12px;
            --radius-md: 8px;
            --radius-sm: 6px;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
            --shadow-md: 0 4px 12px rgba(0, 43, 73, 0.08);
            --shadow-lg: 0 12px 28px rgba(0, 43, 73, 0.12);
            --shadow-hover: 0 16px 36px rgba(0, 43, 73, 0.16);
        }

        body {
            background-color: var(--bg-page);
            color: var(--text-main);
            min-height: 100vh;
            padding: 0;
            margin: 0;
            font-size: 14px;
            line-height: 1.6;
            background-image: none;
        }

        .container {
            max-width: 1360px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* 5-Star Hotel Top Utility Bar */
        .hotel-top-utility {
            background: #FFFFFF;
            border-bottom: 1px solid #ECECEC;
            padding: 6px 24px;
            font-size: 11px;
            color: #64748B;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .hotel-utility-links {
            display: flex;
            gap: 16px;
            align-items: center;
        }
        .hotel-utility-links a {
            color: #475569;
            text-decoration: none;
            transition: color 0.2s;
        }
        .hotel-utility-links a:hover {
            color: var(--brand-primary);
        }

        /* Hilton-style Clean Luxury Header */
        .hotel-main-header {
            background: #FFFFFF;
            border-bottom: 1px solid #E2E8F0;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        .hotel-nav-inner {
            max-width: 1360px;
            margin: 0 auto;
            padding: 14px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }
        .hotel-brand-block {
            display: flex;
            align-items: center;
            gap: 14px;
        }
        .hotel-logo-text {
            font-size: 22px;
            font-weight: 900;
            letter-spacing: 2px;
            color: var(--brand-dark);
            text-transform: uppercase;
            display: flex;
            flex-direction: column;
            line-height: 1.1;
        }
        .hotel-logo-sub {
            font-size: 10px;
            letter-spacing: 3px;
            color: var(--brand-gold);
            font-weight: 700;
            margin-top: 2px;
        }
        .hotel-nav-links {
            display: flex;
            gap: 22px;
            list-style: none;
            align-items: center;
            margin: 0;
            padding: 0;
        }
        .hotel-nav-links a {
            text-decoration: none;
            color: var(--text-main);
            font-weight: 700;
            font-size: 13px;
            letter-spacing: 0.5px;
            transition: all 0.2s;
            position: relative;
            padding: 6px 0;
        }
        .hotel-nav-links a:hover, .hotel-nav-links a.active {
            color: var(--brand-primary);
        }
        .hotel-nav-links a.active::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: var(--brand-primary);
        }

        /* Panoramic Mediterranean Sea View Hero */
        .resort-panoramic-hero {
            position: relative;
            width: 100%;
            height: 520px;
            max-height: 75vh;
            overflow: hidden;
            background-color: #002B49;
        }
        .resort-hero-bg {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center 38%;
            filter: brightness(0.92);
            transition: transform 6s ease-out;
        }
        .resort-panoramic-hero:hover .resort-hero-bg {
            transform: scale(1.03);
        }
        .resort-hero-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(0, 43, 73, 0.25) 0%, rgba(0, 43, 73, 0.65) 100%);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 40px 30px;
            color: white;
        }
        .resort-hero-content {
            max-width: 1360px;
            margin: 0 auto;
            width: 100%;
        }
        .resort-hero-tag {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.35);
            padding: 5px 14px;
            border-radius: 9999px;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1px;
            margin-bottom: 12px;
            text-transform: uppercase;
        }
        .resort-hero-title {
            font-size: 38px;
            font-weight: 900;
            letter-spacing: -0.5px;
            line-height: 1.2;
            margin-bottom: 8px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        .resort-hero-subtitle {
            font-size: 16px;
            font-weight: 500;
            color: rgba(255, 255, 255, 0.92);
            max-width: 750px;
            margin-bottom: 20px;
            line-height: 1.5;
            text-shadow: 0 1px 6px rgba(0,0,0,0.4);
        }

        /* Floating Booking & Info Ribbon */
        .resort-info-ribbon {
            background: white;
            border-radius: var(--radius-md);
            box-shadow: 0 10px 25px rgba(0, 43, 73, 0.15);
            padding: 14px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 16px;
            color: var(--text-main);
            border: 1px solid #E2E8F0;
            margin-top: -30px;
            position: relative;
            z-index: 10;
        }
        .ribbon-item {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 13px;
        }
        .ribbon-icon {
            width: 38px;
            height: 38px;
            border-radius: 8px;
            background: var(--greek-blue-light);
            color: var(--brand-primary);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            flex-shrink: 0;
        }
        .ribbon-label {
            font-size: 11px;
            color: var(--text-muted);
            font-weight: 700;
        }
        .ribbon-val {
            font-weight: 800;
            color: var(--brand-dark);
        }

        /* Hilton Dining & Drinks Editorial Section */
        .hilton-dining-intro {
            text-align: center;
            padding: 50px 20px 25px;
            max-width: 850px;
            margin: 0 auto;
        }
        .hilton-section-headline {
            font-size: 32px;
            font-weight: 900;
            color: var(--brand-dark);
            margin-bottom: 12px;
            letter-spacing: -0.5px;
        }
        .hilton-section-sub {
            font-size: 15px;
            color: var(--text-muted);
            line-height: 1.7;
        }

        /* Hilton Dining Amenities & Breakfast Box */
        .hilton-amenities-box {
            background: var(--brand-sand);
            border-radius: var(--radius-lg);
            padding: 28px 32px;
            margin: 25px auto 40px;
            border: 1px solid var(--brand-sand-dark);
            display: grid;
            grid-template-columns: 1fr 1.5fr;
            gap: 30px;
        }
        @media (max-width: 850px) {
            .hilton-amenities-box {
                grid-template-columns: 1fr;
                padding: 20px;
            }
        }
        .amenity-col-title {
            font-size: 16px;
            font-weight: 900;
            color: var(--brand-dark);
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .amenity-items-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }
        .amenity-badge {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13px;
            font-weight: 700;
            color: #334155;
        }

        /* Hilton-style Menu Categories Tabs */
        .hilton-category-tabs {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
            margin: 30px 0 25px;
            padding: 0 10px;
        }
        .hilton-cat-btn {
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            padding: 10px 18px;
            border-radius: 9999px;
            font-size: 13px;
            font-weight: 800;
            color: #334155;
            cursor: pointer;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        }
        .hilton-cat-btn:hover {
            border-color: var(--brand-primary);
            color: var(--brand-primary);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 75, 135, 0.12);
        }
        .hilton-cat-btn.active {
            background: var(--brand-primary);
            color: white;
            border-color: var(--brand-primary);
            box-shadow: 0 4px 12px rgba(0, 75, 135, 0.25);
        }

        /* 5-Star Hotel Dish & Venue Cards */
        .hilton-venue-card {
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
            position: relative;
        }
        .hilton-venue-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-hover);
            border-color: #CBD5E1;
        }
        .hilton-card-img-wrap {
            position: relative;
            width: 100%;
            height: 220px;
            overflow: hidden;
            background: #F1F5F9;
        }
        .hilton-card-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }
        .hilton-venue-card:hover .hilton-card-img {
            transform: scale(1.06);
        }
        .hilton-card-body {
            padding: 18px 20px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }
        .hilton-card-tag {
            font-size: 11px;
            font-weight: 800;
            color: var(--brand-primary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 6px;
        }
        .hilton-card-title {
            font-size: 18px;
            font-weight: 900;
            color: var(--brand-dark);
            margin-bottom: 6px;
            line-height: 1.3;
        }
        .hilton-card-desc {
            font-size: 12.5px;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 14px;
            flex-grow: 1;
        }
        .hilton-card-footer {
            border-top: 1px solid #F1F5F9;
            padding-top: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .hilton-card-price {
            font-size: 19px;
            font-weight: 900;
            color: var(--brand-primary);
        }
        .hilton-card-price span {
            font-size: 12px;
            font-weight: 700;
            color: var(--text-muted);
        }
"""

# Let's check if the custom CSS is already injected, if not replace the root styles
if "HILTON LUXURY 5-STAR MEDITERRANEAN RESORT STYLING" not in html:
    html = html.replace("<style>\n        :root {", "<style>\n" + hilton_theme_css + "\n        /* Base Root fallback */\n        :root {")

# Next: Update the Customer View Header to match the Hilton Resort Screenshot
hilton_header_html = """
    <!-- Hilton Style 5-Star Utility Bar -->
    <div class="hotel-top-utility">
        <div style="display: flex; align-items: center; gap: 12px;">
            <span>📍 Blue Healing Resort & Lounge • Alexandria Coast</span>
            <span>|</span>
            <span id="utilityPhoneBadge">📞 الحجز والاستعلام: 01000000000</span>
        </div>
        <div class="hotel-utility-links">
            <a href="#customerSection">قائمة المأكولات</a>
            <a href="#amenitiesSection">مرافق الضيافة</a>
            <button class="btn btn-primary btn-sm" onclick="showManagerView()" style="padding: 4px 10px; font-size: 11px;">
                🔐 بوابة الإدارة والشيف
            </button>
        </div>
    </div>

    <!-- Hilton Style Main Header -->
    <header class="hotel-main-header">
        <div class="hotel-nav-inner">
            <div class="hotel-brand-block">
                <div class="brand-logo-badge" style="background: linear-gradient(135deg, #004B87, #0072CE); width: 44px; height: 44px; border-radius: 10px;">BH</div>
                <div class="hotel-logo-text">
                    <span id="navBrandName">BLUE HEALING</span>
                    <span class="hotel-logo-sub">RESORT & LUXURY LOUNGE</span>
                </div>
            </div>

            <ul class="hotel-nav-links">
                <li><a href="#customerSection" class="active">المأكولات والمشروبات (Dining)</a></li>
                <li><a href="#amenitiesSection">المرافق الفندقية (Amenities)</a></li>
                <li><a href="javascript:void(0)" onclick="filterCustomerMenu('🎈 وجبات الأطفال')">منيو الأطفال (Kids Menu)</a></li>
                <li><a href="javascript:void(0)" onclick="openResortContactInfo()">معلومات الحجز (Info)</a></li>
            </ul>

            <div style="display: flex; align-items: center; gap: 10px;">
                <a href="#customerSection" class="btn btn-outline btn-sm" style="border-radius: 9999px;">تصفح المنيو</a>
                <a href="#" id="directHeaderCallBtn" class="btn btn-primary btn-sm" style="border-radius: 9999px;">📞 اتصل بنا</a>
            </div>
        </div>
    </header>
"""

# Replace the old top navbar with the new Hilton hotel header
old_navbar_pattern = r'<div class="top-navbar">[\s\S]*?</div>\s*</div>'
if '<div class="hotel-top-utility">' not in html:
    html = re.sub(r'<div class="top-navbar">[\s\S]*?</div>\s*</div>', hilton_header_html, html, count=1)

# Next: Transform the Customer Section Hero & Dining Intro
hilton_hero_html = """
    <!-- ======================================================== -->
    <!-- VIEW 1: CUSTOMER VIEW - HILTON MEDITERRANEAN RESORT      -->
    <!-- ======================================================== -->
    <section id="customerSection">
        
        <!-- Panoramic Mediterranean Sea View Hero (Matching Hilton Screenshot) -->
        <div class="resort-panoramic-hero">
            <img class="resort-hero-bg" src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1920&q=85" alt="Blue Healing Mediterranean Resort Dining">
            <div class="resort-hero-overlay">
                <div class="resort-hero-content">
                    <span class="resort-hero-tag">Mediterranean Sea View Dining & Lounge</span>
                    <h1 class="resort-hero-title" id="resortHeroTitle">Blue Healing Resort & Lounge</h1>
                    <p class="resort-hero-subtitle" id="resortHeroDesc">
                        أرقى المأكولات الساحلية والعالمية المحضرة يومياً بأعلى المعايير الفندقية، مع إطلالة بحرية خلابة، وقسم خاص وممتع للأطفال!
                    </p>
                </div>
            </div>
        </div>

        <div class="container">
            <!-- Floating Booking & Info Ribbon -->
            <div class="resort-info-ribbon">
                <div class="ribbon-item">
                    <div class="ribbon-icon">📍</div>
                    <div>
                        <div class="ribbon-label">الموقع والإطلالة</div>
                        <div class="ribbon-val" id="resortLocationBadge">إطلالة مباشرة على البحر وتراس شاطئي</div>
                    </div>
                </div>
                <div class="ribbon-item">
                    <div class="ribbon-icon">🕒</div>
                    <div>
                        <div class="ribbon-label">أوقات العمل اليومية</div>
                        <div class="ribbon-val" id="resortHoursBadge">يومياً: 12:00 م - 12:00 منتصف الليل</div>
                    </div>
                </div>
                <div class="ribbon-item">
                    <div class="ribbon-icon">🎈</div>
                    <div>
                        <div class="ribbon-label">قسم الأطفال</div>
                        <div class="ribbon-val">وجبات أطفال مع ألعاب وهدايا</div>
                    </div>
                </div>
                <div class="ribbon-item">
                    <div class="ribbon-icon">📞</div>
                    <div>
                        <div class="ribbon-label">خدمة العملاء والطلبات</div>
                        <a href="#" id="resortCallLink" style="text-decoration:none; color:inherit;">
                            <div class="ribbon-val" id="resortPhoneDisplay">01000000000</div>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Hilton Editorial Intro: Dining and drinks -->
            <div class="hilton-dining-intro" id="diningSectionIntro">
                <h2 class="hilton-section-headline">Dining and drinks</h2>
                <p class="hilton-section-sub">
                    Experience exquisite coastal gastronomy, authentic flavors, and panoramic Mediterranean sea views at Blue Healing. From gourmet dinners to cheerful kids meals, our hospitality team is dedicated to your ultimate culinary satisfaction.
                </p>
            </div>

            <!-- Hilton Style Breakfast & Dining Amenities Box -->
            <div class="hilton-amenities-box" id="amenitiesSection">
                <div>
                    <div class="amenity-col-title">🍳 Breakfast & Fine Dining</div>
                    <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 8px;">
                        بوفيه إفطار فاخر ووجبات متكاملة محضرة من خامات طازجة ومعتمدة وفق أعلى معايير الجودة العالمية.
                    </p>
                    <span style="font-size: 12px; font-weight: 800; color: var(--brand-primary);">
                        خدمة الغرف والشاليهات متاحة يومياً على مدار 24 ساعة
                    </span>
                </div>
                <div>
                    <div class="amenity-col-title">✨ Dining Amenities & Services</div>
                    <div class="amenity-items-grid">
                        <div class="amenity-badge">🌊 إطلالة بانورامية على البحر</div>
                        <div class="amenity-badge">🏖️ جلسات شاطئية وتراس راقٍ</div>
                        <div class="amenity-badge">🎈 منيو خاص بالأطفال وهدايا</div>
                        <div class="amenity-badge">🛎️ توصيل فندقي للشاليهات</div>
                        <div class="amenity-badge">☕ بار قهوة ومشروبات منعشة</div>
                        <div class="amenity-badge">📲 طلب فوري مباشر عبر واتساب</div>
                    </div>
                </div>
            </div>

            <!-- Search and Filter Bar -->
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; margin-bottom: 20px;">
                <div style="position: relative; max-width: 360px; width: 100%;">
                    <input type="text" id="menuSearchInput" placeholder="🔍 ابحث عن وجبة، مكون، أو صنف..." oninput="filterCustomerMenu()" style="width: 100%; padding: 10px 16px; border-radius: 9999px; border: 1px solid #CBD5E1; font-size: 13px; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.04);">
                </div>
                <div style="font-size: 13px; color: var(--text-muted); font-weight: 700;">
                    أطباق مطعم وشاليهات المنتجع
                </div>
            </div>

            <!-- Categories Tabs (Pills) -->
            <div class="hilton-category-tabs" id="customerCategoryPills">
                <!-- Dynamically rendered -->
            </div>
"""

# Replace old hero and intro inside customerSection
customer_section_start = '<section id="customerSection">'
customer_grid_start = '<div class="customer-menu-grid"'

if 'class="resort-panoramic-hero"' not in html:
    pattern_customer = r'<section id="customerSection">[\s\S]*?<div class="customer-menu-grid"'
    html = re.sub(pattern_customer, hilton_hero_html + '\n        <!-- Dishes Grid -->\n        <div class="customer-menu-grid"', html, count=1)

# Update renderCustomerMenu to use the Hilton Venue Card styling
old_card_render_start = 'const card = document.createElement("div");'
old_card_class = 'card.className = `dish-card'

# Let's replace the card template inside renderCustomerMenu
hilton_card_code = """
            const card = document.createElement("div");
            card.className = `hilton-venue-card ${isKidsMeal ? 'kids-card' : ''}`;
            card.id = `dish_${meal.id}`;

            const whatsappText = encodeURIComponent(`مرحباً ${resort.name}، أود طلب وجبة: ${meal.name} (كود: ${meal.itemNo}) بسعر ${f.sellingPrice.toFixed(0)} ج.م.`);
            const whatsappUrl = `https://wa.me/${cleanWhatsapp}?text=${whatsappText}`;

            card.innerHTML = `
                <div class="hilton-card-img-wrap" onclick="openDishDetailModal('${meal.id}')" style="cursor: pointer;">
                    <img class="hilton-card-img" src="${imgUrl}" alt="${meal.name}" loading="lazy">
                    ${meal.badge ? `<span class="badge ${isKidsMeal ? 'badge-kids' : 'badge-special'}" style="position: absolute; top: 12px; right: 12px;">${meal.badge}</span>` : ''}
                    <span style="position: absolute; bottom: 8px; left: 8px; background: rgba(0,0,0,0.65); color: white; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 4px; backdrop-filter: blur(4px);">
                        ${meal.category || 'وجبة رئيسية'}
                    </span>
                </div>
                <div class="hilton-card-body">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 4px;">
                        <span class="hilton-card-tag">${meal.itemNo || '#BH'} • ${meal.portionSize || 'حصة فردية'}</span>
                        <span style="color: #F59E0B; font-size: 12px; font-weight: 800;">★ 4.9</span>
                    </div>
                    <h3 class="hilton-card-title" onclick="openDishDetailModal('${meal.id}')" style="cursor: pointer;">${meal.name}</h3>
                    <p class="hilton-card-desc">${meal.description || 'وجبة فاخرة محضرة من أفضل المكونات الطازجة.'}</p>
                    
                    <div class="hilton-card-footer">
                        <div class="hilton-card-price">
                            ${f.sellingPrice.toFixed(0)} <span>ج.م</span>
                        </div>
                        <div style="display: flex; gap: 6px;">
                            <button onclick="openDishDetailModal('${meal.id}')" class="btn btn-outline btn-sm" style="border-radius: 9999px; padding: 6px 12px; font-size: 11px;">
                                التفاصيل
                            </button>
                            <a href="${whatsappUrl}" target="_blank" class="btn btn-whatsapp btn-sm" style="border-radius: 9999px; padding: 6px 12px; font-size: 11px;" title="طلب مباشر عبر واتساب">
                                <span>اطلب</span>
                                <span>📲</span>
                            </a>
                        </div>
                    </div>
                </div>
            `;
"""

# Let's replace the card generation block cleanly
pattern_card = r'const card = document\.createElement\("div"\);[\s\S]*?card\.innerHTML = `[\s\S]*?`;'
html = re.sub(pattern_card, hilton_card_code.strip(), html, count=1)

# Update applyResortSettingsUI to sync utility bar and direct call links
phone_sync_js = """
        const utilPhone = document.getElementById("utilityPhoneBadge");
        if (utilPhone) utilPhone.innerText = "📞 الحجز والاستعلام: " + (resort.phone || "01000000000");
        const dirCall = document.getElementById("directHeaderCallBtn");
        if (dirCall) dirCall.href = "tel:" + (resort.phone || "").replace(/[^0-9+]/g, '');
"""
if 'utilityPhoneBadge' not in html:
    html = html.replace('document.getElementById("resortPhoneDisplay").innerText = resort.phone || defaultResortSettings.phone;', 'document.getElementById("resortPhoneDisplay").innerText = resort.phone || defaultResortSettings.phone;\n' + phone_sync_js)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html redesigned to 5-Star Hilton Mediterranean Resort aesthetic successfully!")
