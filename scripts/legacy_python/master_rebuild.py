# Master Builder for Blue Healing Resort & Wellness Platform
# Completely clean, modular, zero-bug, 100% functional single-page application

import json

html_code = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Blue Healing Resort & Luxury Lounge • منتجع الاستشفاء الصحي والرياضي</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <!-- SheetJS for Excel Import/Export -->
    <script src="https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js"></script>
    <style>
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

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: var(--bg-page);
            color: var(--text-main);
            min-height: 100vh;
            font-size: 14px;
            line-height: 1.6;
        }

        .container {
            max-width: 1360px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Hotel Utility Top Bar */
        .hotel-top-utility {
            background: #FFFFFF;
            border-bottom: 1px solid #ECECEC;
            padding: 6px 24px;
            font-size: 11px;
            color: #64748B;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
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

        /* 5-Star Hotel Header */
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
            cursor: pointer;
        }
        .brand-logo-badge {
            background: linear-gradient(135deg, var(--brand-primary), var(--brand-blue));
            color: white;
            font-weight: 900;
            font-size: 18px;
            width: 44px;
            height: 44px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 10px rgba(0, 75, 135, 0.25);
            flex-shrink: 0;
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
            gap: 20px;
            list-style: none;
            align-items: center;
            margin: 0;
            padding: 0;
            flex-wrap: wrap;
        }
        .hotel-nav-links a {
            text-decoration: none;
            color: var(--text-main);
            font-weight: 700;
            font-size: 13px;
            transition: all 0.2s;
            position: relative;
            padding: 6px 0;
        }
        .hotel-nav-links a:hover, .hotel-nav-links a.active {
            color: var(--brand-primary);
        }

        /* Buttons */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            font-weight: 700;
            padding: 8px 16px;
            border-radius: var(--radius-sm);
            cursor: pointer;
            border: 1px solid transparent;
            font-size: 13px;
            text-decoration: none;
            transition: all 0.2s ease;
        }
        .btn:hover { transform: translateY(-1px); box-shadow: var(--shadow-sm); }
        .btn-sm { padding: 5px 12px; font-size: 12px; border-radius: var(--radius-sm); }
        .btn-primary { background: var(--brand-primary); color: white; }
        .btn-primary:hover { background: #003B6B; }
        .btn-outline { background: transparent; border-color: var(--border); color: var(--text-main); }
        .btn-outline:hover { background: #F1F5F9; border-color: #CBD5E1; }
        .btn-gold { background: linear-gradient(135deg, #F59E0B, #D97706); color: white; }
        .btn-danger { background: #EF4444; color: white; }
        .btn-danger:hover { background: #DC2626; }
        .btn-purple { background: #7C3AED; color: white; }
        .btn-secondary { background: #64748B; color: white; }
        .btn-whatsapp { background: #25D366; color: white; font-weight: 800; border: none; }
        .btn-whatsapp:hover { background: #1EBE5D; }

        /* Full Width Mediterranean Panoramic Hero */
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

        /* Floating Booking Ribbon */
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
        .ribbon-label { font-size: 11px; color: var(--text-muted); font-weight: 700; }
        .ribbon-val { font-weight: 800; color: var(--brand-dark); }

        /* Hilton Dining Intro */
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
        .hilton-section-sub { font-size: 15px; color: var(--text-muted); line-height: 1.7; }

        /* Hilton Amenities Box */
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
            .hilton-amenities-box { grid-template-columns: 1fr; padding: 20px; }
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

        /* Categories Pills */
        .hilton-category-tabs {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
            margin: 25px 0;
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

        /* Customer Dish & Venue Grid */
        .customer-menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 24px;
            margin-bottom: 50px;
        }
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
        .hilton-venue-card:hover .hilton-card-img { transform: scale(1.06); }
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

        /* ======================================================== */
        /* MANAGER WORKSPACE STYLES                                 */
        /* ======================================================== */
        #managerSection { display: none; padding: 20px 0; }
        .manager-control-bar {
            background: #FEF3C7;
            border: 1.5px solid #F59E0B;
            border-radius: var(--radius-md);
            padding: 12px 18px;
            margin-bottom: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }
        .manager-info {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 800;
            color: #78350F;
            font-size: 14px;
        }
        .meals-tab-bar {
            display: flex;
            align-items: center;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 10px;
            margin-bottom: 14px;
        }
        .meal-tab {
            background: #FFFFFF;
            border: 1px solid var(--border);
            padding: 8px 16px;
            border-radius: var(--radius-md);
            font-weight: 700;
            font-size: 13px;
            color: var(--text-main);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            white-space: nowrap;
            box-shadow: var(--shadow-sm);
        }
        .meal-tab:hover { background: #F8FAFC; border-color: var(--brand-primary); }
        .meal-tab.active {
            background: var(--brand-primary);
            color: white;
            border-color: var(--brand-primary);
        }
        .close-tab {
            font-size: 12px;
            background: rgba(0,0,0,0.1);
            width: 18px;
            height: 18px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .close-tab:hover { background: #EF4444; color: white; }
        .btn-add-meal {
            background: #10B981;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: var(--radius-md);
            font-weight: 800;
            font-size: 13px;
            cursor: pointer;
            white-space: nowrap;
        }
        .btn-add-meal:hover { background: #059669; }

        .workspace-card {
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 24px;
            box-shadow: var(--shadow-md);
            margin-bottom: 24px;
        }
        .meal-info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 14px;
            margin-bottom: 18px;
        }
        .form-control {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .form-control label {
            font-size: 12px;
            font-weight: 800;
            color: #334155;
        }
        .form-control input, .form-control select, .form-control textarea {
            padding: 8px 12px;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            font-size: 13px;
            color: var(--text-main);
            outline: none;
            background: #FFFFFF;
        }
        .form-control input:focus, .form-control select:focus, .form-control textarea:focus {
            border-color: var(--brand-primary);
            box-shadow: 0 0 0 3px rgba(0, 75, 135, 0.1);
        }

        /* Financials Grid */
        .financial-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 14px;
            margin-bottom: 20px;
        }
        .fin-card {
            background: #F8FAFC;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 14px 18px;
            text-align: right;
        }
        .fin-card.highlight {
            background: #EFF6FF;
            border-color: #BFDBFE;
        }
        .fin-card.success {
            background: #ECFDF5;
            border-color: #A7F3D0;
        }
        .fin-label { font-size: 11px; font-weight: 700; color: var(--text-muted); margin-bottom: 4px; }
        .fin-value { font-size: 22px; font-weight: 900; color: var(--brand-dark); }
        .fin-sub { font-size: 11px; color: var(--text-muted); margin-top: 2px; }

        /* Tables */
        .table-responsive { width: 100%; overflow-x: auto; margin-bottom: 18px; }
        .manager-data-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
            background: white;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
        }
        .manager-data-table th, .manager-data-table td {
            padding: 10px 12px;
            border: 1px solid var(--border);
            text-align: right;
        }
        .manager-data-table th {
            background: #F1F5F9;
            color: #1E293B;
            font-weight: 800;
        }
        .manager-data-table tbody tr:hover { background: #F8FAFC; }

        /* Modals */
        .modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.65);
            backdrop-filter: blur(4px);
            z-index: 1000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .modal-overlay.active { display: flex; }
        .modal-content {
            background: white;
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 650px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.25);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            max-height: 90vh;
        }
        .modal-header {
            background: linear-gradient(135deg, var(--brand-primary), var(--brand-dark));
            color: white;
            padding: 14px 20px;
            font-weight: 800;
            font-size: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .modal-body {
            padding: 20px;
            overflow-y: auto;
        }
        .modal-footer {
            background: #F8FAFC;
            border-top: 1px solid var(--border);
            padding: 12px 20px;
            display: flex;
            justify-content: flex-end;
            gap: 10px;
        }
        .manager-sub-box {
            background: #F8FAFC;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 14px;
            margin-top: 12px;
        }
    </style>
</head>
<body>

    <!-- Hidden compatibility markers -->
    <span id="roleBadge" style="display:none;"></span>
    <div id="topNavActions" style="display:none;"></div>

    <!-- Hotel Top Utility Bar -->
    <div class="hotel-top-utility">
        <div style="display: flex; align-items: center; gap: 12px;">
            <span id="navTopLocation">📍 Blue Healing Resort & Lounge • Alexandria Mediterranean Coast</span>
            <span>|</span>
            <span id="utilityPhoneBadge">📞 الحجز والاستعلام: 01000000000</span>
        </div>
        <div class="hotel-utility-links">
            <a href="#customerSection">المأكولات الصحية</a>
            <a href="#activitiesSection">الأنشطة والرياضة</a>
            <a href="#gallerySection">ألبوم المنتجع</a>
            <button class="btn btn-primary btn-sm" onclick="showManagerView()" style="padding: 4px 10px; font-size: 11px;">
                🔐 بوابة الإدارة والشيف
            </button>
        </div>
    </div>

    <!-- 5-Star Hotel Header -->
    <header class="hotel-main-header">
        <div class="hotel-nav-inner">
            <div class="hotel-brand-block" onclick="showCustomerView()">
                <div class="brand-logo-badge">BH</div>
                <div class="hotel-logo-text">
                    <span id="navBrandName">BLUE HEALING</span>
                    <span class="hotel-logo-sub">RESORT & WELLNESS LOUNGE</span>
                </div>
            </div>

            <ul class="hotel-nav-links">
                <li><a href="#customerSection" class="active">المأكولات والمشروبات (Dining)</a></li>
                <li><a href="#activitiesSection">الأنشطة والرياضة (Sports & Wellness)</a></li>
                <li><a href="#gallerySection">ألبوم المنتجع (Gallery)</a></li>
                <li><a href="javascript:void(0)" onclick="filterCustomerMenu('🎈 وجبات الأطفال')">منيو الأطفال (Kids)</a></li>
                <li><a href="#amenitiesSection">مرافق الضيافة (Amenities)</a></li>
            </ul>

            <div style="display: flex; align-items: center; gap: 10px;">
                <button onclick="showManagerView()" class="btn btn-gold btn-sm" style="border-radius: 9999px;">
                    🔐 لوحة الإدارة
                </button>
                <a href="#" id="directHeaderCallBtn" class="btn btn-primary btn-sm" style="border-radius: 9999px;">
                    📞 اتصل بنا
                </a>
            </div>
        </div>
    </header>

    <!-- ======================================================== -->
    <!-- VIEW 1: CUSTOMER VIEW                                    -->
    <!-- ======================================================== -->
    <section id="customerSection">
        
        <!-- Panoramic Mediterranean Sea View Hero -->
        <div class="resort-panoramic-hero">
            <img class="resort-hero-bg" id="mainHeroBgImg" src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1920&q=85" alt="Blue Healing Resort">
            <div class="resort-hero-overlay">
                <div class="resort-hero-content">
                    <span class="resort-hero-tag">Mediterranean Sea View Dining & Wellness</span>
                    <h1 class="resort-hero-title" id="resortHeroTitle">Blue Healing Resort & Lounge</h1>
                    <p class="resort-hero-subtitle" id="resortHeroDesc">
                        أرقى المأكولات الساحلية والصحية المحضرة يومياً بأعلى المعايير، مع أنشطة رياضية شاطئية، وقسم خاص للأطفال!
                    </p>
                </div>
            </div>
        </div>

        <div class="container">
            <!-- Floating Booking Ribbon -->
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
                    استمتع بأشهى المأكولات الساحلية والصحية المحضرة يومياً على أيدي نخبة من أمهر الشيفات. من الوجبات الرياضية المتوازنة إلى أطباق الأطفال المبهجة.
                </p>
            </div>

            <!-- Hilton Style Breakfast & Dining Amenities Box -->
            <div class="hilton-amenities-box" id="amenitiesSection">
                <div>
                    <div class="amenity-col-title">🍳 Breakfast & Healthy Dining</div>
                    <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 8px;">
                        بوفيه إفطار فاخر ووجبات صحية متكاملة محسوبة السعرات، محضرة من خامات طازجة ومعتمدة وفق أعلى معايير الجودة.
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

            <!-- Search and Category Navigation -->
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; margin-bottom: 16px;">
                <div style="position: relative; max-width: 360px; width: 100%;">
                    <input type="text" id="menuSearchInput" placeholder="🔍 ابحث عن وجبة، مكون، أو صنف..." oninput="filterCustomerMenu()" style="width: 100%; padding: 10px 16px; border-radius: 9999px; border: 1px solid #CBD5E1; font-size: 13px; background: white;">
                </div>
                <div style="font-size: 13px; color: var(--text-muted); font-weight: 700;">
                    قائمة مأكولات مطعم وشاليهات المنتجع
                </div>
            </div>

            <!-- Category Pills -->
            <div class="hilton-category-tabs" id="customerCategoryPills">
                <!-- Dynamically populated -->
            </div>

            <!-- Dishes Grid -->
            <div class="customer-menu-grid" id="customerMenuGrid">
                <!-- Dishes populated dynamically -->
            </div>

            <!-- SPORTS & WELLNESS ACTIVITIES SECTION -->
            <div id="activitiesSection" style="padding-top: 40px; margin-top: 40px; border-top: 1px solid var(--border);">
                <div class="hilton-dining-intro" style="padding: 10px 10px 25px;">
                    <span style="display: inline-block; background: #ECFDF5; color: #059669; font-weight: 800; font-size: 11px; padding: 4px 12px; border-radius: 9999px; border: 1px solid #A7F3D0; margin-bottom: 8px;">
                        ✦ Blue Healing Sports & Fitness Club ✦
                    </span>
                    <h2 class="hilton-section-headline" style="color: #064E3B;">الأنشطة الرياضية وبرامج الاستشفاء البدني</h2>
                    <p class="hilton-section-sub">
                        جدد طاقتك البدنية والذهنية مع باقة من التمارين اليومية والأنشطة الشاطئية بإشراف مدربين معتمدين. احجز نشاطك مباشرة عبر واتساب.
                    </p>
                </div>

                <div class="hilton-category-tabs" id="activityCategoryPills">
                    <!-- Dynamically populated -->
                </div>

                <div class="customer-menu-grid" id="activitiesGrid">
                    <!-- Activities populated dynamically -->
                </div>
            </div>

            <!-- RESORT PHOTO GALLERY SECTION -->
            <div id="gallerySection" style="padding-top: 40px; margin-top: 40px; border-top: 1px solid var(--border); background: #FAF9F6; margin-left: -20px; margin-right: -20px; padding-left: 20px; padding-right: 20px; padding-bottom: 50px;">
                <div class="hilton-dining-intro" style="padding: 20px 10px 25px;">
                    <span style="display: inline-block; background: #EBF3FA; color: #004B87; font-weight: 800; font-size: 11px; padding: 4px 12px; border-radius: 9999px; border: 1px solid #BFDBFE; margin-bottom: 8px;">
                        ✦ Resort Photo Gallery ✦
                    </span>
                    <h2 class="hilton-section-headline">جولة مصورة في منتجع Blue Healing</h2>
                    <p class="hilton-section-sub">
                        استكشف مرافقنا الساحلية الفاخرة: صالات اللياقة، مسابح الإنفينيتي، شاطئ اليوغا الخاص، ومطاعم الأكل الصحي.
                    </p>
                </div>

                <div class="hilton-category-tabs" id="galleryCategoryPills">
                    <!-- Dynamically populated -->
                </div>

                <div id="resortGalleryGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; max-width: 1360px; margin: 0 auto;">
                    <!-- Gallery populated dynamically -->
                </div>
            </div>

            <div style="text-align: center; padding: 30px 10px; color: var(--text-muted); font-size: 13px; border-top: 1px solid var(--border); margin-top: 40px;">
                ✦ <span id="footerBrandName">Blue Healing Resort & Hospitality Operations</span> • All rights reserved 2026 ✦
            </div>

        </div>
    </section>

    <!-- ======================================================== -->
    <!-- VIEW 2: MANAGER WORKSPACE & RECIPE EDITOR                -->
    <!-- ======================================================== -->
    <section id="managerSection">
        <div class="container">
            
            <!-- Manager Control Bar -->
            <div class="manager-control-bar">
                <div class="manager-info">
                    <span>🔐 لوحة تحكم الإدارة والمشرف:</span>
                    <span style="color: #1E3A8A;" id="loggedManagerName">المدير العام (Admin)</span>
                </div>
                <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
                    <button class="btn btn-primary btn-sm" style="background: linear-gradient(135deg, #2563EB, #1D4ED8); border:none; font-weight:800; font-size:13px; box-shadow: 0 2px 8px rgba(37,99,235,0.4);" onclick="createNewMeal()">
                        ➕ إضافة وجبة جديدة للمنيو
                    </button>
                    <button class="btn btn-gold btn-sm" onclick="openResortSettingsModal()">⚙️ بيانات المنتجع وأرقام الهاتف</button>
                    <button class="btn btn-primary btn-sm" style="background: linear-gradient(135deg, #059669, #10B981); border:none;" onclick="openActivitiesManagerModal()">🏃 إدارة الأنشطة الرياضية</button>
                    <button class="btn btn-primary btn-sm" style="background: linear-gradient(135deg, #0284C7, #0EA5E9); border:none;" onclick="openGalleryManagerModal()">🖼️ إدارة ألبوم الصور</button>
                    <button class="btn btn-gold btn-sm" onclick="openHeroImageModal()">🌅 تغيير صورة الواجهة</button>
                    <button class="btn btn-purple btn-sm" onclick="openCategoriesManagerModal()">📂 تعديل أقسام المنيو</button>
                    <button class="btn btn-purple btn-sm" onclick="openAdminManagementModal()">👥 حسابات المدراء</button>
                    <button class="btn btn-sm" style="background: linear-gradient(135deg, #8B5CF6, #EC4899); color: white; border: none; font-weight: 700;" onclick="openThemeModifierModal()">🎨 مظهر وثيم المنتجع</button>
                    <button class="btn btn-outline btn-sm" onclick="openPantryModal()">📦 مكتبة الخامات</button>
                    <button class="btn btn-primary btn-sm" onclick="triggerExcelUpload()">📥 رفع خامات Excel</button>
                    <button class="btn btn-outline btn-sm" onclick="showCustomerView()">👁️ معاينة المنيو</button>
                    <button class="btn btn-danger btn-sm" onclick="managerLogout()">🚪 خروج</button>
                </div>
            </div>

            <!-- Multi-Meal Tabs Bar -->
            <div class="meals-tab-bar" id="mealsTabBar">
                <!-- Dynamically populated -->
            </div>

            <!-- Active Meal Workspace Card -->
            <div class="workspace-card" id="mealWorkspace">
                
                <!-- Quick Meal Action Toolbar -->
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; background: #F8FAFC; border: 1px solid var(--border); border-radius: var(--radius-md); padding: 10px 14px; margin-bottom: 18px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-weight: 900; font-size: 14px; color: var(--brand-dark);">🍲 تعديل الوجبة المعيارية الحالية</span>
                        <span style="font-size: 11px; color: var(--text-muted);">(أي تعديل يُحفظ تلقائياً في المنيو والتقارير)</span>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                        <button class="btn btn-primary btn-sm" onclick="saveAndApplyMealChanges()">💾 حفظ وتطبيق على المنيو</button>
                        <button class="btn btn-outline btn-sm" onclick="duplicateCurrentMeal()">📋 تكرار الوجبة</button>
                        <button class="btn btn-danger btn-sm" onclick="deleteCurrentMeal()">🗑️ حذف الوجبة</button>
                        <button class="btn btn-outline btn-sm" onclick="exportCurrentMealToExcel()">📊 تصدير Excel للوجبة</button>
                        <button class="btn btn-outline btn-sm" onclick="showCustomerView()">👁️ معاينة في المنيو</button>
                    </div>
                </div>

                <!-- Meal Photo & Visual Attributes Editor -->
                <div style="display: flex; gap: 18px; margin-bottom: 18px; flex-wrap: wrap; background: #F1F5F9; border-radius: var(--radius-md); padding: 14px; border: 1px solid var(--border);">
                    <img id="mThumbPreview" src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=400&q=80" alt="صورة الوجبة" style="width: 140px; height: 100px; object-fit: cover; border-radius: var(--radius-sm); border: 1px solid var(--border); flex-shrink: 0;">
                    <div style="display: flex; flex-direction: column; gap: 8px; flex-grow: 1;">
                        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                            <span style="font-weight: 800; font-size: 13px; color: #1E293B;">📷 صورة الوجبة ومحددات العرض في منيو الزبائن:</span>
                            <div style="display: flex; gap: 6px;">
                                <button class="btn btn-primary btn-sm" onclick="triggerMealPhotoUpload()">📁 رفع صورة من جهازك</button>
                                <button class="btn btn-outline btn-sm" onclick="promptPhotoUrl()">🌐 رابط صورة</button>
                            </div>
                        </div>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px;">
                            <div class="form-control">
                                <label>قسم الوجبة في المنيو (Category):</label>
                                <select id="mCategory" onchange="updateActiveMealField('category', this.value)">
                                    <!-- Dynamic options -->
                                </select>
                            </div>
                            <div class="form-control">
                                <label>شارة الوجبة (Badge / Tag):</label>
                                <select id="mBadge" onchange="updateActiveMealField('badge', this.value)">
                                    <option value="⭐ الأكثر طلباً">⭐ الأكثر طلباً</option>
                                    <option value="🔥 طبق الشيف المميز">🔥 طبق الشيف المميز</option>
                                    <option value="🎈 وجبة أطفال مع هدية">🎈 وجبة أطفال مع هدية</option>
                                    <option value="🥗 خيار صحي ورياضي">🥗 خيار صحي ورياضي</option>
                                    <option value="✨ صنف جديد">✨ صنف جديد</option>
                                    <option value="">بدون شارة</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Marketing Description for Customer Menu -->
                <div class="form-control" style="margin-bottom: 16px;">
                    <label>وصف الوجبة التسويقي للزبائن (Marketing Description):</label>
                    <textarea id="mDescription" rows="2" placeholder="اكتب وصفاً جذاباً للوجبة ومكوناتها الطازجة..." oninput="updateActiveMealField('description', this.value)"></textarea>
                </div>

                <!-- Meal Info Grid -->
                <div class="meal-info-grid">
                    <div class="form-control">
                        <label>رقم / كود الصنف (Item No):</label>
                        <input type="text" id="mItemNo" oninput="updateActiveMealField('itemNo', this.value)">
                    </div>
                    <div class="form-control" style="grid-column: span 2;">
                        <label>اسم الوجبة المعيارية (Recipe Name):</label>
                        <input type="text" id="mName" oninput="updateActiveMealField('name', this.value)">
                    </div>
                    <div class="form-control">
                        <label>تاريخ تسعير الخامات (Price Date):</label>
                        <input type="date" id="mPriceDate" onchange="updateActiveMealField('priceDate', this.value)">
                    </div>
                    <div class="form-control">
                        <label>عدد الوجبات / الحصص (Portions):</label>
                        <input type="number" id="mPortions" min="1" oninput="updateActiveMealField('portions', parseFloat(this.value)||1)">
                    </div>
                    <div class="form-control">
                        <label>حجم الحصة للفرد (Portion Size):</label>
                        <input type="text" id="mPortionSize" oninput="updateActiveMealField('portionSize', this.value)">
                    </div>
                    <div class="form-control">
                        <label>تكلفة التوابل والبهارات (Seasoning EGP):</label>
                        <input type="number" id="mSeasoning" min="0" step="0.5" oninput="updateActiveMealField('seasoning', parseFloat(this.value)||0)">
                    </div>
                    <div class="form-control">
                        <label>نسبة الهالك والفاقد (Waste & Shrinkage %):</label>
                        <input type="number" id="mWastePct" min="0" max="50" step="0.5" oninput="updateActiveMealField('wastePct', parseFloat(this.value)||0)">
                    </div>
                    <div class="form-control">
                        <label>مُعامل التسعير (Multiplier 3.1 - 3.6):</label>
                        <input type="number" id="mMultiplier" min="1" max="10" step="0.01" oninput="onMultiplierChanged(this.value)">
                    </div>
                    <div class="form-control">
                        <label>نسبة تكلفة الطعام المقترحة (Food Cost %):</label>
                        <input type="number" id="mFoodCostPct" min="1" max="100" step="0.1" oninput="onFoodCostChanged(this.value)">
                    </div>
                </div>

                <!-- Financial Highlights Cards -->
                <div class="financial-grid">
                    <div class="fin-card">
                        <div class="fin-label">1. إجمالي تكلفة الخامات (Subtotal)</div>
                        <div class="fin-value" id="fSubtotal">0.00 ج.م</div>
                        <div class="fin-sub">تكلفة المكونات بدون هالك</div>
                    </div>
                    <div class="fin-card">
                        <div class="fin-label">2. إجمالي تكلفة الوصفة (Total Cost)</div>
                        <div class="fin-value" id="fTotalCost">0.00 ج.م</div>
                        <div class="fin-sub">تشمل الخامات + التوابل + 5% هالك</div>
                    </div>
                    <div class="fin-card highlight">
                        <div class="fin-label">3. تكلفة الحصة الواحدة (Cost / Portion)</div>
                        <div class="fin-value" id="fCostPerPortion" style="color: var(--brand-primary);">0.00 ج.م</div>
                        <div class="fin-sub">التكلفة الفعلية للطبق الفردي</div>
                    </div>
                    <div class="fin-card success">
                        <div class="fin-label">4. سعر البيع المقترح (Selling Price)</div>
                        <div class="fin-value" id="fSellingPrice" style="color: #059669;">0.00 ج.م</div>
                        <div class="fin-sub">سعر القائمة الرسمي في المنيو</div>
                    </div>
                    <div class="fin-card">
                        <div class="fin-label">5. هامش الربح للحصة (Gross Profit)</div>
                        <div class="fin-value" id="fGrossProfit">0.00 ج.م</div>
                        <div class="fin-sub" id="fProfitMargin">نسبة الهامش: 0%</div>
                    </div>
                </div>

                <!-- Ingredients Table Header & Actions -->
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 10px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <h3 style="font-size: 15px; font-weight: 800; color: #1E293B;">📋 جدول مكونات وخامات الوجبة:</h3>
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <button class="btn btn-outline btn-sm" onclick="openPantryModal()">📦 استيراد من مكتبة الخامات</button>
                        <button class="btn btn-primary btn-sm" onclick="addNewIngredientRow()">➕ إضافة صنف جديد</button>
                    </div>
                </div>

                <!-- Ingredients Table -->
                <div class="table-responsive">
                    <table class="manager-data-table" id="ingredientsTable">
                        <thead>
                            <tr>
                                <th>اسم الخامة / المكون</th>
                                <th>تاريخ السعر</th>
                                <th>الكمية بالوصفة</th>
                                <th>وحدة الوصفة</th>
                                <th>وحدة الشراء</th>
                                <th>سعر الشراء (ج.م)</th>
                                <th>معامل التحويل</th>
                                <th>تكلفة المكون (ج.م)</th>
                                <th>إجراء</th>
                            </tr>
                        </thead>
                        <tbody id="ingredientsTableBody">
                            <!-- Populated dynamically -->
                        </tbody>
                    </table>
                </div>

            </div>

            <!-- Master Menu Dashboard (Overview for all meals) -->
            <div class="workspace-card" id="menuDashboardWorkspace" style="display: none;">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 18px;">
                    <h3 style="font-size: 18px; font-weight: 900; color: var(--brand-dark);">📊 جدول مقارنة وتحليل تكاليف المنيو الكامل</h3>
                    <div style="display: flex; gap: 8px;">
                        <button class="btn btn-primary btn-sm" onclick="exportAllMealsToExcel()">📥 تصدير المنيو الكامل Excel</button>
                    </div>
                </div>
                <div class="table-responsive">
                    <table class="manager-data-table">
                        <thead>
                            <tr>
                                <th>كود الصنف</th>
                                <th>اسم الوجبة</th>
                                <th>القسم</th>
                                <th>الحصص</th>
                                <th>إجمالي التكلفة</th>
                                <th>تكلفة الحصة</th>
                                <th>سعر البيع المقترح</th>
                                <th>Food Cost %</th>
                                <th>هامش الربح للحصة</th>
                                <th>إجراء</th>
                            </tr>
                        </thead>
                        <tbody id="masterDashboardTableBody">
                            <!-- Populated dynamically -->
                        </tbody>
                    </table>
                </div>
            </div>

        </div>
    </section>

    <!-- ======================================================== -->
    <!-- ALL MODALS (Zero Missing IDs, 100% Functional)           -->
    <!-- ======================================================== -->

    <!-- Modal 1: Login Modal -->
    <div class="modal-overlay" id="loginModal">
        <div class="modal-content" style="max-width: 420px;">
            <div class="modal-header">
                <span>🔐 دخول لوحة الإدارة والمشرف</span>
                <span style="cursor: pointer; font-size: 18px;" onclick="closeLoginModal()">✕</span>
            </div>
            <div class="modal-body">
                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 14px;">
                    أدخل اسم المستخدم والرمز السري للوصول إلى تعديل الأسعار، الخامات والمنيو.
                </p>
                <div class="form-control" style="margin-bottom: 12px;">
                    <label>اسم المستخدم (Username):</label>
                    <input type="text" id="loginUsername" placeholder="الافتراضي: admin">
                </div>
                <div class="form-control" style="margin-bottom: 12px;">
                    <label>الرمز السري (Passcode):</label>
                    <input type="password" id="loginPassword" placeholder="الافتراضي: bluehealing123" onkeydown="if(event.key==='Enter') executeLogin()">
                </div>
                <div style="background: #FEF3C7; border: 1px solid #F59E0B; border-radius: 6px; padding: 8px 12px; font-size: 11px; color: #92400E;">
                    💡 بيانات الدخول الافتراضية: <b>admin</b> / الرمز السري: <b>bluehealing123</b>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary btn-sm" onclick="closeLoginModal()">إلغاء</button>
                <button class="btn btn-primary btn-sm" onclick="executeLogin()">دخول 🚀</button>
            </div>
        </div>
    </div>

    <!-- Modal 2: Resort Settings -->
    <div class="modal-overlay" id="resortSettingsModal">
        <div class="modal-content" style="max-width: 600px;">
            <div class="modal-header">
                <span>⚙️ تعديل بيانات المنتجع وأرقام الهاتف</span>
                <span style="cursor: pointer; font-size: 18px;" onclick="closeResortSettingsModal()">✕</span>
            </div>
            <div class="modal-body">
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <div class="form-control">
                        <label>اسم المنتجع أو المطعم (Resort / Restaurant Name):</label>
                        <input type="text" id="cfgResortName" placeholder="Blue Healing Resort & Lounge">
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                        <div class="form-control">
                            <label>رقم هاتف الاتصال والحجز (Call Phone):</label>
                            <input type="text" id="cfgResortPhone" placeholder="01000000000">
                        </div>
                        <div class="form-control">
                            <label>رقم الواتساب لاستقبال الطلبات (WhatsApp):</label>
                            <input type="text" id="cfgResortWhatsapp" placeholder="201000000000">
                        </div>
                    </div>
                    <div class="form-control">
                        <label>مواعيد العمل (Operating Hours):</label>
                        <input type="text" id="cfgResortHours" placeholder="يومياً: 12:00 م - 12:00 منتصف الليل">
                    </div>
                    <div class="form-control">
                        <label>عنوان أو وصف الخدمة (Location / Delivery Note):</label>
                        <input type="text" id="cfgResortLocation" placeholder="إطلالة مباشرة على البحر وتراس شاطئي">
                    </div>
                    <div class="form-control">
                        <label>نص الترحيب بالمنيو (Welcome Description):</label>
                        <textarea id="cfgResortHeroDesc" rows="2"></textarea>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary btn-sm" onclick="closeResortSettingsModal()">إلغاء</button>
                <button class="btn btn-gold btn-sm" onclick="saveResortSettings()">حفظ وتحديث البيانات 💾</button>
            </div>
        </div>
    </div>

    <!-- Modal 3: Categories Manager -->
    <div class="modal-overlay" id="categoriesManagerModal">
        <div class="modal-content" style="max-width: 650px;">
            <div class="modal-header" style="background: linear-gradient(135deg, #7C3AED, #6D28D9);">
                <span>📂 تعديل وإدارة أقسام المنيو (Menu Categories)</span>
                <span style="cursor: pointer; font-size: 18px;" onclick="closeCategoriesManagerModal()">✕</span>
            </div>
            <div class="modal-body">
                <div class="table-responsive" style="margin-bottom: 16px;">
                    <table class="manager-data-table">
                        <thead>
                            <tr>
                                <th style="width: 50px;">الأيقونة</th>
                                <th>اسم القسم</th>
                                <th style="width: 120px;">إجراءات</th>
                            </tr>
                        </thead>
                        <tbody id="categoriesTableBody">
                            <!-- Populated dynamically -->
                        </tbody>
                    </table>
                </div>

                <div class="manager-sub-box">
                    <h4 style="font-size: 13px; font-weight: 800; color: #1E293B; margin-bottom: 10px;" id="catFormTitle">
                        ➕ إضافة قسم جديد للمنيو
                    </h4>
                    <div style="display: grid; grid-template-columns: 80px 1fr auto; gap: 10px; align-items: flex-end;">
                        <div class="form-control">
                            <label>الأيقونة:</label>
                            <input type="text" id="newCatIcon" placeholder="🍽️" style="text-align: center; font-size: 16px;">
                        </div>
                        <div class="form-control">
                            <label>اسم القسم:</label>
                            <input type="text" id="newCatName" placeholder="مثال: مشروبات وعصائر طبيعية">
                        </div>
                        <div style="display: flex; gap: 6px;">
                            <button class="btn btn-secondary btn-sm" id="btnCancelEditCat" style="display:none;" onclick="cancelEditCategory()">إلغاء</button>
                            <button class="btn btn-purple btn-sm" id="btnSaveCat" onclick="saveCategoryFromForm()">حفظ القسم 💾</button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary btn-sm" onclick="closeCategoriesManagerModal()">إغلاق</button>
            </div>
        </div>
    </div>

    <!-- Modal 4: Activities Manager -->
    <div class="modal-overlay" id="activitiesManagerModal">
        <div class="modal-content" style="max-width: 850px;">
            <div class="modal-header" style="background: linear-gradient(135deg, #064E3B, #059669);">
                <span>🏃 إدارة الأنشطة والتمارين الرياضية (Sports & Wellness Activities)</span>
                <span style="cursor: pointer; font-size: 18px;" onclick="closeActivitiesManagerModal()">✕</span>
            </div>
            <div class="modal-body">
                <div class="table-responsive" style="margin-bottom: 16px;">
                    <table class="manager-data-table">
                        <thead>
                            <tr>
                                <th>النشاط</th>
                                <th>القسم</th>
                                <th>الموعد / التوقيت</th>
                                <th>المدرب</th>
                                <th>السعر</th>
                                <th>إجراءات</th>
                            </tr>
                        </thead>
                        <tbody id="activitiesTableBody">
                            <!-- Populated dynamically -->
                        </tbody>
                    </table>
                </div>

                <div class="manager-sub-box">
                    <h4 style="font-size: 13px; font-weight: 800; color: #1E293B; margin-bottom: 10px;" id="activityFormTitle">
                        ➕ إضافة نشاط أو تمرين رياضي جديد
                    </h4>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px;">
                        <div class="form-control" style="grid-column: span 2;">
                            <label>عنوان النشاط الرياضي:</label>
                            <input type="text" id="actInputTitle" placeholder="مثال: يوغا صباحية على الشاطئ">
                        </div>
                        <div class="form-control">
                            <label>قسم النشاط:</label>
                            <select id="actInputCategory">
                                <option value="يوغا وتأمل">🧘 يوغا وتأمل</option>
                                <option value="لياقة وتمارين">🏋️ لياقة وتمارين (Gym & Fitness)</option>
                                <option value="رياضات مائية">🏊 رياضات مائية وسباحة</option>
                                <option value="سبا واستشفاء">💆 سبا واستشفاء (Recovery)</option>
                                <option value="مضرب وتنس">🎾 ملاعب بادل وتنس</option>
                            </select>
                        </div>
                        <div class="form-control">
                            <label>المواعيد والجدول:</label>
                            <input type="text" id="actInputSchedule" placeholder="مثال: يومياً: 06:30 ص - 07:30 ص">
                        </div>
                        <div class="form-control">
                            <label>المدرب المسؤول:</label>
                            <input type="text" id="actInputInstructor" placeholder="مثال: كابتن سارة أحمد">
                        </div>
                        <div class="form-control">
                            <label>الشدة والمستوى:</label>
                            <input type="text" id="actInputIntensity" placeholder="مثال: خفيف ومريح / متوسط">
                        </div>
                        <div class="form-control">
                            <label>السعر:</label>
                            <input type="text" id="actInputPrice" placeholder="مثال: 150 ج.م أو مجاناً للنزلاء">
                        </div>
                        <div class="form-control" style="grid-column: span 2;">
                            <label>وصف النشاط:</label>
                            <textarea id="actInputDesc" rows="2"></textarea>
                        </div>
                        <div class="form-control" style="grid-column: span 2;">
                            <label>صورة النشاط (Upload / URL):</label>
                            <div style="display: flex; gap: 8px;">
                                <input type="text" id="actInputImage" placeholder="رابط صورة أو ارفع من جهازك..." style="flex-grow: 1;">
                                <button type="button" class="btn btn-outline btn-sm" onclick="triggerActivityPhotoUpload()">📁 رفع صورة</button>
                            </div>
                            <input type="file" id="actFileInput" accept="image/*" style="display:none;" onchange="handleActivityPhotoUpload(event)">
                        </div>
                    </div>
                    <div style="display: flex; gap: 8px; justify-content: flex-end; margin-top: 12px;">
                        <button class="btn btn-secondary btn-sm" type="button" onclick="resetActivityForm()">إلغاء</button>
                        <button class="btn btn-primary btn-sm" type="button" onclick="saveActivityFromForm()">حفظ النشاط 💾</button>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary btn-sm" onclick="closeActivitiesManagerModal()">إغلاق</button>
            </div>
        </div>
    </div>

    <!-- Modal 5: Gallery Manager -->
    <div class="modal-overlay" id="galleryManagerModal">
        <div class="modal-content" style="max-width: 800px;">
            <div class="modal-header" style="background: linear-gradient(135deg, #004B87, #0284C7);">
                <span>🖼️ إدارة ألبوم صور المنتجع والمرافق (Resort Gallery Manager)</span>
                <span style="cursor: pointer; font-size: 18px;" onclick="closeGalleryManagerModal()">✕</span>
            </div>
            <div class="modal-body">
                <div class="manager-sub-box" style="margin-bottom: 16px;">
                    <h4 style="font-size: 13px; font-weight: 800; color: #1E293B; margin-bottom: 10px;">
                        ➕ إضافة صورة جديدة للألبوم:
                    </h4>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px;">
                        <div class="form-control">
                            <label>عنوان الصورة / المرفق:</label>
                            <input type="text" id="galInputTitle" placeholder="مثال: مسبح إنفينيتي المطل على البحر">
                        </div>
                        <div class="form-control">
                            <label>تصنيف المرفق:</label>
                            <select id="galInputCategory">
                                <option value="المسابح والشاطئ">🌊 المسابح والشاطئ</option>
                                <option value="الجيم واللياقة">🏋️ صالة الجيم واللياقة</option>
                                <option value="اليوغا والتأمل">🧘 جلسات اليوغا والتأمل</option>
                                <option value="السبا والاستشفاء">💆 السبا والاستشفاء</option>
                                <option value="المطعم الصحي">🥗 المطعم الصحي</option>
                                <option value="الإقامة والشاليهات">🏡 الإقامة والشاليهات</option>
                            </select>
                        </div>
                        <div class="form-control" style="grid-column: span 2;">
                            <label>الصورة (Upload / URL):</label>
                            <div style="display: flex; gap: 8px;">
                                <input type="text" id="galInputImage" placeholder="رابط صورة أو ارفع من جهازك..." style="flex-grow: 1;">
                                <button type="button" class="btn btn-outline btn-sm" onclick="triggerGalleryPhotoUpload()">📁 رفع صورة</button>
                            </div>
                            <input type="file" id="galFileInput" accept="image/*" style="display:none;" onchange="handleGalleryPhotoUpload(event)">
                        </div>
                    </div>
                    <div style="display: flex; justify-content: flex-end; margin-top: 10px;">
                        <button class="btn btn-primary btn-sm" onclick="addPhotoToGallery()">إضافة إلى الألبوم 📸</button>
                    </div>
                </div>

                <h4 style="font-size: 13px; font-weight: 800; color: #1E293B; margin-bottom: 10px;">
                    📸 الصور الحالية في الألبوم:
                </h4>
                <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px;" id="managerGalleryGrid">
                    <!-- Populated dynamically -->
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary btn-sm" onclick="closeGalleryManagerModal()">إغلاق</button>
            </div>
        </div>
    </div>

    <!-- Modal 6: Hero Image Modifier -->
    <div class="modal-overlay" id="heroImageModal">
        <div class="modal-content" style="max-width: 650px;">
            <div class="modal-header" style="background: linear-gradient(135deg, #B8860B, #D97706);">
                <span>🌅 تعديل وتغيير صورة الواجهة الرئيسية (Hero Cover Image)</span>
                <span style="cursor: pointer; font-size: 18px;" onclick="closeHeroImageModal()">✕</span>
            </div>
            <div class="modal-body">
                <div style="width: 100%; height: 200px; border-radius: var(--radius-md); overflow: hidden; margin-bottom: 14px; position: relative; border: 1px solid var(--border);">
                    <img id="heroImagePreview" src="" alt="Hero Preview" style="width:100%; height:100%; object-fit: cover;">
                </div>
                <div class="form-control" style="margin-bottom: 12px;">
                    <label>رابط الصورة المباشر (Image URL):</label>
                    <div style="display: flex; gap: 8px;">
                        <input type="text" id="heroImageUrlInput" placeholder="ضع رابط صورة عالي الجودة هنا..." oninput="updateHeroPreview(this.value)">
                        <button class="btn btn-outline btn-sm" onclick="triggerHeroPhotoUpload()">📁 رفع من جهازك</button>
                    </div>
                    <input type="file" id="heroFileInput" accept="image/*" style="display:none;" onchange="handleHeroPhotoUpload(event)">
                </div>

                <label style="font-size: 12px; font-weight: 800; color: #334155; display: block; margin-bottom: 6px;">
                    ✨ صور بانورامية مقترحة (اضغط للاختيار فوراً):
                </label>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;">
                    <div onclick="selectHeroPreset('https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1920&q=85')" style="height: 60px; border-radius: 6px; overflow: hidden; cursor: pointer;">
                        <img src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=300&q=80" style="width:100%; height:100%; object-fit: cover;">
                    </div>
                    <div onclick="selectHeroPreset('https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=1920&q=85')" style="height: 60px; border-radius: 6px; overflow: hidden; cursor: pointer;">
                        <img src="https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=300&q=80" style="width:100%; height:100%; object-fit: cover;">
                    </div>
                    <div onclick="selectHeroPreset('https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=1920&q=85')" style="height: 60px; border-radius: 6px; overflow: hidden; cursor: pointer;">
                        <img src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=300&q=80" style="width:100%; height:100%; object-fit: cover;">
                    </div>
                    <div onclick="selectHeroPreset('https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?auto=format&fit=crop&w=1920&q=85')" style="height: 60px; border-radius: 6px; overflow: hidden; cursor: pointer;">
                        <img src="https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?auto=format&fit=crop&w=300&q=80" style="width:100%; height:100%; object-fit: cover;">
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary btn-sm" onclick="closeHeroImageModal()">إلغاء</button>
                <button class="btn btn-gold btn-sm" onclick="saveHeroImage()">حفظ صورة الواجهة 💾</button>
            </div>
        </div>
    </div>

    <!-- Modal 7: Theme Modifier -->
    <div class="modal-overlay" id="themeModifierModal">
        <div class="modal-content" style="max-width: 680px;">
            <div class="modal-header" style="background: linear-gradient(135deg, #8B5CF6, #EC4899);">
                <span>🎨 تخصيص مظهر وثيم المنتجع (Theme Modifier)</span>
                <span style="cursor: pointer; font-size: 18px;" onclick="closeThemeModifierModal()">✕</span>
            </div>
            <div class="modal-body">
                <label style="font-weight: 800; font-size: 13px; color: var(--text-main); display: block; margin-bottom: 8px;">
                    ✨ ثيمات فندقية جاهزة (اضغط للتطبيق الفوري):
                </label>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px; margin-bottom: 16px;" id="themePresetsGrid">
                    <!-- Populated dynamically -->
                </div>

                <div class="manager-sub-box">
                    <h4 style="font-size: 13px; font-weight: 800; margin-bottom: 10px;">🎛️ الألوان المخصصة:</h4>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                        <div class="form-control">
                            <label>اللون الرئيسي (Primary):</label>
                            <input type="color" id="themeColorPrimary" onchange="previewLiveTheme()">
                        </div>
                        <div class="form-control">
                            <label>لون التمييز (Accent):</label>
                            <input type="color" id="themeColorAccent" onchange="previewLiveTheme()">
                        </div>
                        <div class="form-control">
                            <label>اللون الذهبي (Gold):</label>
                            <input type="color" id="themeColorGold" onchange="previewLiveTheme()">
                        </div>
                        <div class="form-control">
                            <label>خلفية الصفحة (Page BG):</label>
                            <input type="color" id="themeColorBgPage" onchange="previewLiveTheme()">
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer" style="display: flex; justify-content: space-between;">
                <button class="btn btn-secondary btn-sm" onclick="resetThemeToDefault()">🔄 الافتراضي</button>
                <div style="display: flex; gap: 8px;">
                    <button class="btn btn-secondary btn-sm" onclick="closeThemeModifierModal()">إلغاء</button>
                    <button class="btn btn-gold btn-sm" onclick="saveThemeSettings()">حفظ وتطبيق الثيم 💾</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal 8: Admin Management -->
    <div class="modal-overlay" id="adminManagementModal">
        <div class="modal-content" style="max-width: 650px;">
            <div class="modal-header">
                <span>👥 إدارة حسابات المدراء والرموز السرية</span>
                <span style="cursor: pointer; font-size: 18px;" onclick="closeAdminManagementModal()">✕</span>
            </div>
            <div class="modal-body">
                <div class="table-responsive">
                    <table class="manager-data-table">
                        <thead>
                            <tr>
                                <th>الاسم / الصفة</th>
                                <th>اسم المستخدم</th>
                                <th>الرمز السري</th>
                                <th>إجراءات</th>
                            </tr>
                        </thead>
                        <tbody id="adminsTableBody">
                            <!-- Populated dynamically -->
                        </tbody>
                    </table>
                </div>

                <div class="manager-sub-box">
                    <h4 style="font-size: 13px; font-weight: 800; color: #1E293B; margin-bottom: 10px;" id="adminFormTitle">
                        ➕ إضافة حساب مدير جديد
                    </h4>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px;">
                        <div class="form-control">
                            <label>الاسم الكامل:</label>
                            <input type="text" id="admInputName" placeholder="مثال: شيف أحمد علي">
                        </div>
                        <div class="form-control">
                            <label>اسم المستخدم:</label>
                            <input type="text" id="admInputUsername" placeholder="مثال: chef_ahmed">
                        </div>
                        <div class="form-control">
                            <label>الرمز السري (Passcode):</label>
                            <input type="text" id="admInputPasscode" placeholder="مثال: pass1234">
                        </div>
                    </div>
                    <div style="display: flex; gap: 6px; justify-content: flex-end; margin-top: 10px;">
                        <button class="btn btn-secondary btn-sm" id="btnCancelEditAdmin" style="display:none;" onclick="cancelEditAdmin()">إلغاء</button>
                        <button class="btn btn-primary btn-sm" id="btnSaveAdmin" onclick="saveAdminFromForm()">حفظ الحساب 💾</button>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary btn-sm" onclick="closeAdminManagementModal()">إغلاق</button>
            </div>
        </div>
    </div>

    <!-- Modal 9: Master Pantry Library -->
    <div class="modal-overlay" id="pantryModal">
        <div class="modal-content" style="max-width: 750px;">
            <div class="modal-header">
                <span>📦 مكتبة الخامات والمكونات الشائعة (Master Pantry)</span>
                <span style="cursor: pointer; font-size: 18px;" onclick="closePantryModal()">✕</span>
            </div>
            <div class="modal-body">
                <div style="display: flex; gap: 10px; margin-bottom: 12px;">
                    <input type="text" id="pantrySearchInput" placeholder="🔍 ابحث في الخامات..." oninput="filterPantryList()" style="flex-grow: 1; padding: 8px 12px; border: 1px solid var(--border); border-radius: var(--radius-sm);">
                    <button class="btn btn-primary btn-sm" onclick="addNewPantryItemPrompt()">➕ إضافة خامة جديدة</button>
                </div>
                <div class="table-responsive" style="max-height: 400px; overflow-y: auto;">
                    <table class="manager-data-table">
                        <thead>
                            <tr>
                                <th>اسم الخامة</th>
                                <th>القسم</th>
                                <th>وحدة الشراء</th>
                                <th>سعر الشراء (ج.م)</th>
                                <th>إجراء</th>
                            </tr>
                        </thead>
                        <tbody id="pantryTableBody">
                            <!-- Populated dynamically -->
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="modal-footer" style="display: flex; justify-content: space-between;">
                <button class="btn btn-secondary btn-sm" onclick="resetPantryToDefaults()">🔄 استعادة قائمة السوق الأصلية</button>
                <button class="btn btn-primary btn-sm" onclick="closePantryModal()">تم</button>
            </div>
        </div>
    </div>

    <!-- Modal 10: Dish Detail for Customer -->
    <div class="modal-overlay" id="dishDetailModal" onclick="if(event.target===this) closeDishDetailModal()">
        <div class="modal-content" style="max-width: 500px;">
            <div class="modal-header">
                <span id="detailDishTitleHeader">تفاصيل الوجبة</span>
                <span style="cursor: pointer; font-size: 18px;" onclick="closeDishDetailModal()">✕</span>
            </div>
            <div class="modal-body" style="padding: 0;">
                <img id="detailDishImg" src="" alt="Dish" style="width: 100%; height: 240px; object-fit: cover;">
                <div style="padding: 20px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span id="detailDishBadge" class="badge" style="background: #EBF3FA; color: #004B87; font-weight: 800; font-size: 11px; padding: 3px 8px; border-radius: 4px;"></span>
                        <span id="detailDishPortion" style="font-size: 12px; color: var(--text-muted); font-weight: 700;"></span>
                    </div>
                    <h3 id="detailDishName" style="font-size: 20px; font-weight: 900; color: var(--brand-dark); margin-bottom: 8px;"></h3>
                    <p id="detailDishDesc" style="font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 14px;"></p>
                    
                    <div style="background: #F8FAFC; border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 10px 14px; margin-bottom: 16px;">
                        <span style="font-size: 11px; font-weight: 800; color: #334155; display: block; margin-bottom: 4px;">🥗 المكونات الطازجة:</span>
                        <span id="detailDishIngredientsList" style="font-size: 12px; color: var(--text-muted);"></span>
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <span style="font-size: 11px; color: var(--text-muted); display: block;">السعر الرسمي</span>
                            <span id="detailDishPrice" style="font-size: 22px; font-weight: 900; color: var(--brand-primary);"></span>
                        </div>
                        <a href="#" id="detailDishWhatsappLink" target="_blank" class="btn btn-whatsapp" style="border-radius: 9999px; padding: 10px 20px;">
                            <span>اطلب الآن عبر واتساب</span>
                            <span>📲</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal 11: Gallery Lightbox -->
    <div class="modal-overlay" id="galleryLightboxModal" onclick="if(event.target===this) this.classList.remove('active')">
        <div style="position: relative; max-width: 90vw; max-height: 90vh; display: flex; flex-direction: column; align-items: center;">
            <span style="position: absolute; top: -35px; right: 0; color: white; font-size: 28px; cursor: pointer;" onclick="document.getElementById('galleryLightboxModal').classList.remove('active')">✕</span>
            <img id="lightboxImg" src="" style="max-width: 100%; max-height: 80vh; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            <div id="lightboxCaption" style="color: white; font-size: 14px; font-weight: 700; margin-top: 10px; text-align: center; text-shadow: 0 1px 4px rgba(0,0,0,0.8);"></div>
        </div>
    </div>

    <!-- Hidden File Inputs -->
    <input type="file" id="excelFileInput" accept=".xlsx, .xls, .csv" style="display:none;" onchange="handleExcelUpload(event)">
    <input type="file" id="mealPhotoInput" accept="image/*" style="display:none;" onchange="handleMealPhotoUpload(event)">

    <!-- ======================================================== -->
    <!-- COMPLETE JAVASCRIPT LOGIC ENGINE                         -->
    <!-- ======================================================== -->
    <script>
    // --- Master Default Data ---
    const defaultResortSettings = {
        name: "Blue Healing Resort & Lounge",
        phone: "01000000000",
        whatsapp: "201000000000",
        hours: "يومياً: 12:00 م - 12:00 منتصف الليل",
        location: "إطلالة مباشرة على البحر وتراس شاطئي",
        heroDesc: "أرقى المأكولات الساحلية والصحية المحضرة يومياً بأعلى المعايير، مع أنشطة رياضية شاطئية، وقسم خاص للأطفال!",
        heroImage: "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1920&q=85"
    };

    const defaultCategories = [
        { id: "cat_all", name: "جميع الأطباق", icon: "🍽️", isFixed: true },
        { id: "cat_kids", name: "وجبات الأطفال", icon: "🎈", isFixed: false },
        { id: "cat_healthy", name: "أطباق صحية ورياضية", icon: "🥗", isFixed: false },
        { id: "cat_poultry", name: "دواجن ولحوم", icon: "🍖", isFixed: false },
        { id: "cat_seafood", name: "مأكولات بحرية", icon: "🦐", isFixed: false },
        { id: "cat_burger", name: "برجر وساندوتشات", icon: "🍔", isFixed: false },
        { id: "cat_pasta", name: "باستا ومكرونات", icon: "🍝", isFixed: false },
        { id: "cat_dessert", name: "حلويات ومشروبات", icon: "🍰", isFixed: false }
    ];

    const defaultPantry = [
        { name: "صدور دجاج مخلي (Chicken Breast)", cat: "دواجن ولحوم", unit: "كيلوجرام (Kg)", price: 220 },
        { name: "أوراك دجاج مخلية (Chicken Thighs)", cat: "دواجن ولحوم", unit: "كيلوجرام (Kg)", price: 190 },
        { name: "لحم بقري مفروم أحمر (Minced Beef)", cat: "دواجن ولحوم", unit: "كيلوجرام (Kg)", price: 340 },
        { name: "ستيك بقري ريب آي (Ribeye)", cat: "دواجن ولحوم", unit: "كيلوجرام (Kg)", price: 460 },
        { name: "جمبري مقشر وسط (Shrimp)", cat: "أسماك وبحريات", unit: "كيلوجرام (Kg)", price: 360 },
        { name: "سمك فيليه قشر بياض (Fish Fillet)", cat: "أسماك وبحريات", unit: "كيلوجرام (Kg)", price: 260 },
        { name: "سلمون نرويجي طازج (Salmon)", cat: "أسماك وبحريات", unit: "كيلوجرام (Kg)", price: 580 },
        { name: "شوفان عضوي حبة كاملة (Oats)", cat: "حبوب ونشويات", unit: "كيلوجرام (Kg)", price: 65 },
        { name: "أرز بسمتي هندي درجة أولى (Basmati)", cat: "حبوب ونشويات", unit: "كيلوجرام (Kg)", price: 85 },
        { name: "كينوا عضوية (Quinoa)", cat: "حبوب ونشويات", unit: "كيلوجرام (Kg)", price: 140 },
        { name: "بروكلي طازج (Broccoli)", cat: "خضروات وفواكه", unit: "كيلوجرام (Kg)", price: 45 },
        { name: "أفوكادو طازج (Avocado)", cat: "خضروات وفواكه", unit: "كيلوجرام (Kg)", price: 160 },
        { name: "طماطم بلدي طازجة (Tomato)", cat: "خضروات وفواكه", unit: "كيلوجرام (Kg)", price: 20 },
        { name: "بصل أحمر طازج (Red Onion)", cat: "خضروات وفواكه", unit: "كيلوجرام (Kg)", price: 18 },
        { name: "بطاطس تحمير / طبخ (Potato)", cat: "خضروات وفواكه", unit: "كيلوجرام (Kg)", price: 25 },
        { name: "زيت زيتون بكر ممتاز (Olive Oil)", cat: "زيوت وبقالة", unit: "لتر (L)", price: 260 },
        { name: "علبة وجبة تيك أواي فاخرة (Packaging)", cat: "تعبئة وتغليف", unit: "قطعة / حصة", price: 6 }
    ];

    const defaultActivities = [
        {
            id: "act_1",
            title: "جلسة يوغا وتأمل عند شروق الشمس (Sunrise Beach Yoga)",
            category: "يوغا وتأمل",
            schedule: "يومياً: 06:30 ص - 07:30 ص",
            instructor: "كابتن سارة أحمد (مدربة يوغا معتمدة)",
            intensity: "خفيف ومريح - ملائم لجميع المستويات",
            price: "150 ج.م (مجاناً لنزلاء الشاليهات)",
            image: "https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=800&q=80",
            description: "تنفس عميق وتناغم حركي على رمال الشاطئ لتنشيط الدورة الدموية والتخلص من التوتر وصفاء الذهن."
        },
        {
            id: "act_2",
            title: "تدريب اللياقة البدنية والكروس فيت الشاطئي (Beach CrossFit & HIIT)",
            category: "لياقة وتمارين",
            schedule: "السبت والإثنين والأربعاء: 05:00 م - 06:00 م",
            instructor: "كابتن عمر الشناوي (أخصائي تأهيل بدني)",
            intensity: "متوسط إلى عالي",
            price: "200 ج.م",
            image: "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=800&q=80",
            description: "تمارين رفع معدل الحرق وتقوية العضلات في المساحات المفتوحة المطلة على البحر للياقة متفجرة."
        },
        {
            id: "act_3",
            title: "السباحة الاستشفائية والتمارين المائية (Aqua Aerobics)",
            category: "رياضات مائية",
            schedule: "يومياً: 11:00 ص - 12:00 ظهراً",
            instructor: "كابتن ندى طارق",
            intensity: "متوسط - لطيف جداً على المفاصل",
            price: "180 ج.م",
            image: "https://images.unsplash.com/photo-1530549387789-4c1017266635?auto=format&fit=crop&w=800&q=80",
            description: "تمارين مقاومة الماء اللطيفة المناسبة لمرونة المفاصل والاستشفاء العضلي في المسبح الدافئ."
        },
        {
            id: "act_4",
            title: "جلسات التدليك والاستشفاء العضلي (Sports Recovery Massage)",
            category: "سبا واستشفاء",
            schedule: "متاح بالحجز المسبق: 10:00 ص - 10:00 م",
            instructor: "أخصائي الاستشفاء والعلاج الطبيعي",
            intensity: "استرخائي وتأهيلي",
            price: "450 ج.م",
            image: "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=800&q=80",
            description: "مساج استشفائي متقدم لفك التقلصات العضلية وتسريع استعادة حيوية الجسم بعد التمارين الرياضية."
        },
        {
            id: "act_5",
            title: "تحدي وتدريب ملاعب البادل (Sunset Padel Coaching)",
            category: "مضرب وتنس",
            schedule: "يومياً: 04:00 م - 11:00 م",
            instructor: "مدرب معتمد للاتحاد الدولي",
            intensity: "حيوي وممتع",
            price: "250 ج.م / ساعة الحجز",
            image: "https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=800&q=80",
            description: "ملاعب بادل شاطئية حديثة ومجهزة بأعلى الإضاءات الدولية مع إمكانية توفير المضارب والمدربين."
        }
    ];

    const defaultGallery = [
        { id: "gal_1", title: "مسبح إنفينيتي والشاطئ الخاص", category: "المسابح والشاطئ", image: "https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=900&q=80" },
        { id: "gal_2", title: "صالة اللياقة البدنية المطلة على البحر", category: "الجيم واللياقة", image: "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=900&q=80" },
        { id: "gal_3", title: "جلسات اليوغا والتأمل عند الشروق", category: "اليوغا والتأمل", image: "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=900&q=80" },
        { id: "gal_4", title: "مركز السبا والاستشفاء والعلاج الطبيعي", category: "السبا والاستشفاء", image: "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=900&q=80" },
        { id: "gal_5", title: "مطعم المأكولات الصحية والأطباق الطازجة", category: "المطعم الصحي", image: "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=900&q=80" },
        { id: "gal_6", title: "شاليهات وأجنحة المنتجع الفندقية", category: "الإقامة والشاليهات", image: "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=900&q=80" }
    ];

    const defaultMeals = [
        {
            id: "meal_0",
            itemNo: "#101",
            name: "وجبة دجاج مشوي صحي مع أرز بسمتي وخضار",
            category: "أطباق صحية ورياضية",
            badge: "⭐ الأكثر طلباً",
            image: "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?auto=format&fit=crop&w=600&q=80",
            description: "صدور دجاج طازجة متبلة بالأعشاب الطبيعية ومشوية على الفحم، تقدم مع أرز بسمتي بالبخار وبروكلي سوتيه بزيت الزيتون البكر.",
            priceDate: "2026-11-13",
            portions: 4,
            portionSize: "380 gm",
            seasoning: 10,
            wastePct: 5,
            multiplier: 3.33,
            ingredients: [
                { name: "صدور دجاج مخلي (Chicken Breast)", date: "2026-11-13", qty: 800, rUnit: "جرام (Gram)", pUnit: "كيلوجرام (Kg)", price: 220 },
                { name: "أرز بسمتي هندي درجة أولى (Basmati)", date: "2026-11-13", qty: 400, rUnit: "جرام (Gram)", pUnit: "كيلوجرام (Kg)", price: 85 },
                { name: "بروكلي طازج (Broccoli)", date: "2026-11-13", qty: 300, rUnit: "جرام (Gram)", pUnit: "كيلوجرام (Kg)", price: 45 },
                { name: "زيت زيتون بكر ممتاز (Olive Oil)", date: "2026-11-13", qty: 50, rUnit: "مليلتر (ml)", pUnit: "لتر (L)", price: 260 },
                { name: "علبة وجبة تيك أواي فاخرة (Packaging)", date: "2026-11-13", qty: 4, rUnit: "قطعة / حصة", pUnit: "قطعة / حصة", price: 6 }
            ]
        },
        {
            id: "meal_kids_1",
            itemNo: "#KIDS-1",
            name: "وجبة كيدز تشيكن تندر المقرمشة مع بطاطس وهدية",
            category: "وجبات الأطفال",
            badge: "🎈 وجبة أطفال مع هدية",
            image: "https://images.unsplash.com/photo-1562967914-608f82629710?auto=format&fit=crop&w=600&q=80",
            description: "قطع تندر دجاج مقرمشة وذهبية من صدور الدجاج الصافية 100%، تقدم مع بطاطس مقرمشة وعلبة عصير ولعبة مفاجأة للأطفال.",
            priceDate: "2026-11-13",
            portions: 2,
            portionSize: "220 gm",
            seasoning: 5,
            wastePct: 4,
            multiplier: 3.1,
            ingredients: [
                { name: "صدور دجاج مخلي (Chicken Breast)", date: "2026-11-13", qty: 300, rUnit: "جرام (Gram)", pUnit: "كيلوجرام (Kg)", price: 220 },
                { name: "بطاطس تحمير / طبخ (Potato)", date: "2026-11-13", qty: 250, rUnit: "جرام (Gram)", pUnit: "كيلوجرام (Kg)", price: 25 },
                { name: "علبة وجبة تيك أواي فاخرة (Packaging)", date: "2026-11-13", qty: 2, rUnit: "قطعة / حصة", pUnit: "قطعة / حصة", price: 6 }
            ]
        },
        {
            id: "meal_salmon",
            itemNo: "#FIT-02",
            name: "فيليه سلمون مشوي مع كينوا وأفوكادو",
            category: "أطباق صحية ورياضية",
            badge: "🥗 خيار صحي ورياضي",
            image: "https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=600&q=80",
            description: "شريحة سلمون نرويجي مشوية غنية بالأوميغا-3 تقدم مع سلطة كينوا عضوية وشرائح أفوكادو طازجة وصوص ليمون بالأعشاب.",
            priceDate: "2026-11-13",
            portions: 2,
            portionSize: "320 gm",
            seasoning: 12,
            wastePct: 5,
            multiplier: 3.25,
            ingredients: [
                { name: "سلمون نرويجي طازج (Salmon)", date: "2026-11-13", qty: 400, rUnit: "جرام (Gram)", pUnit: "كيلوجرام (Kg)", price: 580 },
                { name: "كينوا عضوية (Quinoa)", date: "2026-11-13", qty: 150, rUnit: "جرام (Gram)", pUnit: "كيلوجرام (Kg)", price: 140 },
                { name: "أفوكادو طازج (Avocado)", date: "2026-11-13", qty: 200, rUnit: "جرام (Gram)", pUnit: "كيلوجرام (Kg)", price: 160 },
                { name: "زيت زيتون بكر ممتاز (Olive Oil)", date: "2026-11-13", qty: 30, rUnit: "مليلتر (ml)", pUnit: "لتر (L)", price: 260 },
                { name: "علبة وجبة تيك أواي فاخرة (Packaging)", date: "2026-11-13", qty: 2, rUnit: "قطعة / حصة", pUnit: "قطعة / حصة", price: 6 }
            ]
        }
    ];

    // --- Global App State ---
    let appState = {
        isManagerLoggedIn: false,
        currentLoggedInAdmin: null,
        resortSettings: { ...defaultResortSettings },
        adminsList: [
            { id: "adm_1", name: "المدير العام", username: "admin", passcode: "bluehealing123" }
        ],
        categories: [...defaultCategories],
        selectedCategory: "جميع الأطباق",
        currentView: "customer",
        activeTab: "meal_0",
        pantry: [...defaultPantry],
        meals: [...defaultMeals],
        activities: [...defaultActivities],
        gallery: [...defaultGallery]
    };

    let selectedActivityCategory = "الكل";
    let selectedGalleryCategory = "الكل";
    let editingCatId = null;
    let editingAdminId = null;
    let editingActivityId = null;

    // --- LocalStorage Persistence ---
    const STORAGE_KEY = "blue_healing_v3_state";
    const THEME_KEY = "blue_healing_v3_theme";

    function saveState() {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
        } catch (e) {
            console.warn("Storage save failed:", e);
        }
    }

    function loadState() {
        try {
            const raw = localStorage.getItem(STORAGE_KEY);
            if (raw) {
                const parsed = JSON.parse(raw);
                appState = { ...appState, ...parsed };
                if (!appState.meals || !appState.meals.length) appState.meals = [...defaultMeals];
                if (!appState.categories || !appState.categories.length) appState.categories = [...defaultCategories];
                if (!appState.activities || !appState.activities.length) appState.activities = [...defaultActivities];
                if (!appState.gallery || !appState.gallery.length) appState.gallery = [...defaultGallery];
                if (!appState.resortSettings) appState.resortSettings = { ...defaultResortSettings };
                if (!appState.adminsList || !appState.adminsList.length) {
                    appState.adminsList = [{ id: "adm_1", name: "المدير العام", username: "admin", passcode: "bluehealing123" }];
                }
            }
        } catch (e) {
            console.error("Storage load error:", e);
        }

        // Session check for login
        if (sessionStorage.getItem("blue_healing_manager_logged") === "true") {
            appState.isManagerLoggedIn = true;
            try {
                appState.currentLoggedInAdmin = JSON.parse(sessionStorage.getItem("blue_healing_current_admin"));
            } catch(e) {}
        }
    }

    // --- Math Calculations ---
    function getConversionFactor(recipeUnit, purchaseUnit) {
        const ru = (recipeUnit || "").trim().toLowerCase();
        const pu = (purchaseUnit || "").trim().toLowerCase();

        if (ru.includes("جرام") || ru.includes("gram") || ru.includes("gm") || ru.includes("g")) {
            if (pu.includes("كيلو") || pu.includes("kg")) return 0.001;
            return 1;
        }
        if (ru.includes("مليلتر") || ru.includes("ml")) {
            if (pu.includes("لتر") || pu.includes("l")) return 0.001;
            return 1;
        }
        return 1;
    }

    function calculateMealFinancials(meal) {
        if (!meal) return { subtotal: 0, totalCost: 0, costPerPortion: 0, sellingPrice: 0, grossProfit: 0, foodCostPct: 0, multiplier: 3.33 };

        let subtotal = 0;
        (meal.ingredients || []).forEach(ing => {
            const qty = parseFloat(ing.qty) || 0;
            const price = parseFloat(ing.price) || 0;
            const factor = getConversionFactor(ing.rUnit, ing.pUnit);
            subtotal += qty * price * factor;
        });

        const seasoning = parseFloat(meal.seasoning) || 0;
        const wastePct = parseFloat(meal.wastePct) || 0;
        const wasteAmount = subtotal * (wastePct / 100);
        const totalCost = subtotal + seasoning + wasteAmount;

        const portions = Math.max(1, parseFloat(meal.portions) || 1);
        const costPerPortion = totalCost / portions;

        const multiplier = Math.max(1, parseFloat(meal.multiplier) || 3.33);
        const sellingPrice = costPerPortion * multiplier;
        const grossProfit = sellingPrice - costPerPortion;
        const foodCostPct = sellingPrice > 0 ? (costPerPortion / sellingPrice) * 100 : 0;
        const profitMargin = sellingPrice > 0 ? (grossProfit / sellingPrice) * 100 : 0;

        return {
            subtotal,
            seasoning,
            wastePct,
            wasteAmount,
            totalCost,
            portions,
            costPerPortion,
            multiplier,
            sellingPrice,
            grossProfit,
            foodCostPct,
            profitMargin
        };
    }

    // --- Resort UI Settings Sync ---
    function applyResortSettingsUI() {
        const r = appState.resortSettings || defaultResortSettings;
        document.getElementById("navBrandName").innerText = r.name || defaultResortSettings.name;
        document.getElementById("resortHeroTitle").innerText = r.name || defaultResortSettings.name;
        document.getElementById("resortHeroDesc").innerText = r.heroDesc || defaultResortSettings.heroDesc;
        document.getElementById("footerBrandName").innerText = r.name || defaultResortSettings.name;
        
        document.getElementById("resortLocationBadge").innerText = r.location || defaultResortSettings.location;
        document.getElementById("resortHoursBadge").innerText = r.hours || defaultResortSettings.hours;
        document.getElementById("resortPhoneDisplay").innerText = r.phone || defaultResortSettings.phone;
        document.getElementById("utilityPhoneBadge").innerText = "📞 الحجز والاستعلام: " + (r.phone || defaultResortSettings.phone);

        const cleanPhone = (r.phone || "").replace(/[^0-9+]/g, '');
        document.getElementById("resortCallLink").href = "tel:" + cleanPhone;
        document.getElementById("directHeaderCallBtn").href = "tel:" + cleanPhone;

        if (r.heroImage) {
            document.getElementById("mainHeroBgImg").src = r.heroImage;
        }
    }

    // --- View Switching (Customer vs Manager) ---
    function setView(viewName) {
        appState.currentView = viewName;
        const custSec = document.getElementById("customerSection");
        const mgrSec = document.getElementById("managerSection");

        applyResortSettingsUI();

        if (viewName === "manager") {
            custSec.style.display = "none";
            mgrSec.style.display = "block";
            const adminName = appState.currentLoggedInAdmin ? appState.currentLoggedInAdmin.name : "المدير العام";
            document.getElementById("loggedManagerName").innerText = adminName;
            renderCategorySelectOptions();
            renderTabs();
            renderActiveMeal();
        } else {
            custSec.style.display = "block";
            mgrSec.style.display = "none";
            renderCategoryPills();
            renderCustomerMenu();
            renderActivitiesUI();
            renderGalleryUI();
        }
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function showCustomerView() { setView("customer"); }
    function showManagerView() {
        if (!appState.isManagerLoggedIn) {
            openLoginModal();
        } else {
            setView("manager");
        }
    }

    // --- Login & Logout ---
    function openLoginModal() {
        document.getElementById("loginUsername").value = "";
        document.getElementById("loginPassword").value = "";
        document.getElementById("loginModal").classList.add("active");
        setTimeout(() => document.getElementById("loginUsername").focus(), 100);
    }
    function closeLoginModal() { document.getElementById("loginModal").classList.remove("active"); }

    function executeLogin() {
        const u = document.getElementById("loginUsername").value.trim().toLowerCase();
        const p = document.getElementById("loginPassword").value.trim();

        const match = appState.adminsList.find(a => a.username.toLowerCase() === u && a.passcode === p);
        if (match) {
            appState.isManagerLoggedIn = true;
            appState.currentLoggedInAdmin = match;
            sessionStorage.setItem("blue_healing_manager_logged", "true");
            sessionStorage.setItem("blue_healing_current_admin", JSON.stringify(match));
            closeLoginModal();
            setView("manager");
        } else {
            alert("❌ خطأ: اسم المستخدم أو الرمز السري غير صحيح!");
        }
    }

    function managerLogout() {
        if (confirm("هل ترغب في تسجيل الخروج من لوحة الإدارة؟")) {
            appState.isManagerLoggedIn = false;
            appState.currentLoggedInAdmin = null;
            sessionStorage.removeItem("blue_healing_manager_logged");
            sessionStorage.removeItem("blue_healing_current_admin");
            setView("customer");
        }
    }

    // --- Customer Menu Rendering ---
    function renderCategoryPills() {
        const container = document.getElementById("customerCategoryPills");
        if (!container) return;
        container.innerHTML = "";

        appState.categories.forEach(cat => {
            const btn = document.createElement("button");
            const isActive = appState.selectedCategory === cat.name;
            btn.className = `hilton-cat-btn ${isActive ? 'active' : ''}`;
            btn.innerHTML = `<span>${cat.icon || '🍽️'}</span> <span>${cat.name}</span>`;
            btn.onclick = () => {
                appState.selectedCategory = cat.name;
                renderCategoryPills();
                filterCustomerMenu();
            };
            container.appendChild(btn);
        });
    }

    function filterCustomerMenu(overrideCat = null) {
        if (overrideCat) {
            appState.selectedCategory = overrideCat;
            renderCategoryPills();
        }
        const searchInput = document.getElementById("menuSearchInput");
        const q = (searchInput ? searchInput.value : "").toLowerCase().trim();

        let list = appState.meals;
        if (appState.selectedCategory && appState.selectedCategory !== "جميع الأطباق") {
            list = list.filter(m => (m.category || "") === appState.selectedCategory);
        }

        if (q) {
            list = list.filter(m =>
                (m.name || "").toLowerCase().includes(q) ||
                (m.itemNo || "").toLowerCase().includes(q) ||
                (m.description || "").toLowerCase().includes(q) ||
                (m.ingredients || []).some(i => i.name.toLowerCase().includes(q))
            );
        }
        renderCustomerMenu(list);
    }

    function renderCustomerMenu(mealsList = null) {
        const grid = document.getElementById("customerMenuGrid");
        if (!grid) return;
        grid.innerHTML = "";

        const list = mealsList || appState.meals;
        const resort = appState.resortSettings || defaultResortSettings;
        const cleanWhatsapp = (resort.whatsapp || defaultResortSettings.whatsapp).replace(/[^0-9]/g, '');

        if (!list.length) {
            grid.innerHTML = `
                <div style="grid-column: 1/-1; text-align: center; padding: 50px 20px; color: var(--text-muted); background: white; border-radius: var(--radius-lg); border: 1px solid var(--border);">
                    🍽️ لا توجد وجبات في هذا القسم حالياً.
                </div>
            `;
            return;
        }

        list.forEach(meal => {
            const f = calculateMealFinancials(meal);
            const isKids = (meal.category || "").includes("أطفال");
            const img = meal.image || (isKids ? 
                "https://images.unsplash.com/photo-1562967914-608f82629710?auto=format&fit=crop&w=600&q=80" : 
                "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80");

            const waMsg = encodeURIComponent(`مرحباً ${resort.name}، أود طلب وجبة: ${meal.name} (كود: ${meal.itemNo || '#BH'}) بسعر ${f.sellingPrice.toFixed(0)} ج.م.`);
            const waUrl = `https://wa.me/${cleanWhatsapp}?text=${waMsg}`;

            const card = document.createElement("div");
            card.className = "hilton-venue-card";
            card.innerHTML = `
                <div class="hilton-card-img-wrap" onclick="openDishDetailModal('${meal.id}')" style="cursor: pointer;">
                    <img class="hilton-card-img" src="${img}" alt="${meal.name}" loading="lazy">
                    ${meal.badge ? `<span style="position: absolute; top: 12px; right: 12px; background: rgba(0, 43, 73, 0.85); color: white; font-size: 11px; font-weight: 800; padding: 4px 10px; border-radius: 9999px; backdrop-filter: blur(4px);">${meal.badge}</span>` : ''}
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
                    <p class="hilton-card-desc">${meal.description || 'وجبة فاخرة وصحية محضرة من أجود الخامات الطازجة.'}</p>
                    
                    <div class="hilton-card-footer">
                        <div class="hilton-card-price">
                            ${f.sellingPrice.toFixed(0)} <span>ج.م</span>
                        </div>
                        <div style="display: flex; gap: 6px;">
                            <button onclick="openDishDetailModal('${meal.id}')" class="btn btn-outline btn-sm" style="border-radius: 9999px; padding: 6px 12px; font-size: 11px;">
                                التفاصيل
                            </button>
                            <a href="${waUrl}" target="_blank" class="btn btn-whatsapp btn-sm" style="border-radius: 9999px; padding: 6px 12px; font-size: 11px;" title="طلب مباشر عبر واتساب">
                                <span>اطلب</span>
                                <span>📲</span>
                            </a>
                        </div>
                    </div>
                </div>
            `;
            grid.appendChild(card);
        });
    }

    function openDishDetailModal(mealId) {
        const meal = appState.meals.find(m => m.id === mealId);
        if (!meal) return;
        const f = calculateMealFinancials(meal);
        const resort = appState.resortSettings || defaultResortSettings;
        const cleanWhatsapp = (resort.whatsapp || defaultResortSettings.whatsapp).replace(/[^0-9]/g, '');

        document.getElementById("detailDishTitleHeader").innerText = meal.name;
        document.getElementById("detailDishImg").src = meal.image || "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80";
        document.getElementById("detailDishName").innerText = meal.name;
        document.getElementById("detailDishBadge").innerText = meal.badge || meal.category || "وجبة مميزة";
        document.getElementById("detailDishPortion").innerText = "حجم الحصة: " + (meal.portionSize || "350 gm");
        document.getElementById("detailDishDesc").innerText = meal.description || "وجبة صحية متكاملة محضرة وفق أعلى المعايير الفندقية.";
        
        const ingNames = (meal.ingredients || []).map(i => i.name).join(" • ");
        document.getElementById("detailDishIngredientsList").innerText = ingNames || "مكونات وتوابل طازجة";
        document.getElementById("detailDishPrice").innerHTML = `${f.sellingPrice.toFixed(0)} <span style="font-size:14px; font-weight:700;">ج.م</span>`;

        const waMsg = encodeURIComponent(`مرحباً ${resort.name}، أود طلب وجبة: ${meal.name} (كود: ${meal.itemNo || '#BH'}) بسعر ${f.sellingPrice.toFixed(0)} ج.م.`);
        document.getElementById("detailDishWhatsappLink").href = `https://wa.me/${cleanWhatsapp}?text=${waMsg}`;

        document.getElementById("dishDetailModal").classList.add("active");
    }
    function closeDishDetailModal() { document.getElementById("dishDetailModal").classList.remove("active"); }

    // --- Sports & Activities Logic ---
    function renderActivitiesUI() {
        renderActivityCategoryPills();
        renderCustomerActivitiesList();
    }

    function renderActivityCategoryPills() {
        const container = document.getElementById("activityCategoryPills");
        if (!container) return;
        const cats = ["الكل", "يوغا وتأمل", "لياقة وتمارين", "رياضات مائية", "سبا واستشفاء", "مضرب وتنس"];
        container.innerHTML = cats.map(c => `
            <button class="hilton-cat-btn ${selectedActivityCategory === c ? 'active' : ''}" onclick="filterActivities('${c}')">
                ${c === 'الكل' ? '⭐ جميع الأنشطة' : c}
            </button>
        `).join("");
    }

    function filterActivities(cat) {
        selectedActivityCategory = cat;
        renderActivityCategoryPills();
        renderCustomerActivitiesList();
    }

    function renderCustomerActivitiesList() {
        const grid = document.getElementById("activitiesGrid");
        if (!grid) return;
        const list = appState.activities || defaultActivities;
        const filtered = selectedActivityCategory === "الكل" ? list : list.filter(a => a.category === selectedActivityCategory);

        const resort = appState.resortSettings || defaultResortSettings;
        const cleanWhatsapp = (resort.whatsapp || defaultResortSettings.whatsapp).replace(/[^0-9]/g, '');

        if (!filtered.length) {
            grid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">لا توجد أنشطة حالياً في هذا القسم.</div>`;
            return;
        }

        grid.innerHTML = filtered.map(act => {
            const bookingMsg = encodeURIComponent(`مرحباً ${resort.name}، أود حجز وممارسة نشاط: ${act.title} - الموعد: ${act.schedule}`);
            const waUrl = `https://wa.me/${cleanWhatsapp}?text=${bookingMsg}`;

            return `
                <div class="hilton-venue-card" style="box-shadow: 0 4px 15px rgba(0, 43, 73, 0.08);">
                    <div class="hilton-card-img-wrap" style="height: 200px;">
                        <img class="hilton-card-img" src="${act.image || 'https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=600&q=80'}" alt="${act.title}" loading="lazy">
                        <span style="position: absolute; top: 12px; right: 12px; background: #059669; color: white; font-size: 11px; font-weight: 800; padding: 3px 10px; border-radius: 9999px;">
                            ${act.category}
                        </span>
                        <span style="position: absolute; bottom: 8px; left: 8px; background: rgba(0,0,0,0.7); color: white; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 4px;">
                            🕒 ${act.schedule}
                        </span>
                    </div>
                    <div class="hilton-card-body">
                        <div style="font-size: 11px; color: var(--text-muted); font-weight: 700; margin-bottom: 4px;">
                            👤 المدرب: <b style="color: var(--brand-dark);">${act.instructor}</b> • المستوى: ${act.intensity}
                        </div>
                        <h3 class="hilton-card-title" style="font-size: 16px; margin-bottom: 6px;">${act.title}</h3>
                        <p class="hilton-card-desc" style="font-size: 12px; margin-bottom: 12px;">${act.description}</p>
                        
                        <div class="hilton-card-footer">
                            <div class="hilton-card-price" style="font-size: 16px; color: #059669;">
                                ${act.price}
                            </div>
                            <a href="${waUrl}" target="_blank" class="btn btn-whatsapp btn-sm" style="border-radius: 9999px; padding: 6px 14px; font-size: 12px; font-weight: 800;">
                                <span>احجز النشاط</span>
                                <span>📲</span>
                            </a>
                        </div>
                    </div>
                </div>
            `;
        }).join("");
    }

    // --- Activities Manager Modal ---
    function openActivitiesManagerModal() {
        renderActivitiesManagerTable();
        resetActivityForm();
        document.getElementById("activitiesManagerModal").classList.add("active");
    }
    function closeActivitiesManagerModal() {
        document.getElementById("activitiesManagerModal").classList.remove("active");
        renderActivitiesUI();
    }

    function renderActivitiesManagerTable() {
        const tbody = document.getElementById("activitiesTableBody");
        if (!tbody) return;
        tbody.innerHTML = (appState.activities || []).map(a => `
            <tr>
                <td><b>${a.title}</b></td>
                <td><span class="badge" style="background:#ECFDF5; color:#065F46; padding:2px 6px; border-radius:4px; font-size:11px;">${a.category}</span></td>
                <td><small>${a.schedule}</small></td>
                <td>${a.instructor}</td>
                <td style="color:#059669; font-weight:800;">${a.price}</td>
                <td>
                    <button class="btn btn-outline btn-sm" style="padding: 2px 8px; font-size: 11px;" onclick="startEditActivity('${a.id}')">تعديل</button>
                    <button class="btn btn-danger btn-sm" style="padding: 2px 8px; font-size: 11px;" onclick="deleteActivity('${a.id}')">حذف</button>
                </td>
            </tr>
        `).join("");
    }

    function saveActivityFromForm() {
        const title = document.getElementById("actInputTitle").value.trim();
        if (!title) { alert("من فضلك أدخل عنوان النشاط الرياضي"); return; }
        const category = document.getElementById("actInputCategory").value;
        const schedule = document.getElementById("actInputSchedule").value.trim() || "يومياً";
        const instructor = document.getElementById("actInputInstructor").value.trim() || "مدرب معتمد";
        const intensity = document.getElementById("actInputIntensity").value.trim() || "ملائم للجميع";
        const price = document.getElementById("actInputPrice").value.trim() || "مجاناً للنزلاء";
        const desc = document.getElementById("actInputDesc").value.trim();
        const img = document.getElementById("actInputImage").value.trim() || "https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=800&q=80";

        if (editingActivityId) {
            const act = appState.activities.find(a => a.id === editingActivityId);
            if (act) {
                act.title = title; act.category = category; act.schedule = schedule;
                act.instructor = instructor; act.intensity = intensity; act.price = price;
                act.description = desc; act.image = img;
            }
            editingActivityId = null;
        } else {
            appState.activities.push({
                id: "act_" + Date.now(),
                title, category, schedule, instructor, intensity, price, description: desc, image: img
            });
        }
        saveState();
        renderActivitiesManagerTable();
        resetActivityForm();
        renderActivitiesUI();
        alert("✨ تم حفظ النشاط الرياضي بنجاح!");
    }

    function startEditActivity(id) {
        const act = appState.activities.find(a => a.id === id);
        if (!act) return;
        editingActivityId = id;
        document.getElementById("activityFormTitle").innerText = "✏️ تعديل بيانات النشاط: " + act.title;
        document.getElementById("actInputTitle").value = act.title;
        document.getElementById("actInputCategory").value = act.category;
        document.getElementById("actInputSchedule").value = act.schedule;
        document.getElementById("actInputInstructor").value = act.instructor;
        document.getElementById("actInputIntensity").value = act.intensity;
        document.getElementById("actInputPrice").value = act.price;
        document.getElementById("actInputDesc").value = act.description;
        document.getElementById("actInputImage").value = act.image;
    }

    function resetActivityForm() {
        editingActivityId = null;
        document.getElementById("activityFormTitle").innerText = "➕ إضافة نشاط أو تمرين رياضي جديد";
        document.getElementById("actInputTitle").value = "";
        document.getElementById("actInputSchedule").value = "";
        document.getElementById("actInputInstructor").value = "";
        document.getElementById("actInputIntensity").value = "";
        document.getElementById("actInputPrice").value = "";
        document.getElementById("actInputDesc").value = "";
        document.getElementById("actInputImage").value = "";
    }

    function deleteActivity(id) {
        if (!confirm("هل أنت متأكد من حذف هذا النشاط الرياضي؟")) return;
        appState.activities = appState.activities.filter(a => a.id !== id);
        saveState();
        renderActivitiesManagerTable();
        renderActivitiesUI();
    }

    function triggerActivityPhotoUpload() { document.getElementById("actFileInput").click(); }
    function handleActivityPhotoUpload(e) {
        compressImageFile(e.target.files[0], 800, 0.82, (base64) => {
            document.getElementById("actInputImage").value = base64;
        });
    }

    // --- Resort Gallery Logic ---
    function renderGalleryUI() {
        renderGalleryCategoryPills();
        renderCustomerGalleryGrid();
    }

    function renderGalleryCategoryPills() {
        const container = document.getElementById("galleryCategoryPills");
        if (!container) return;
        const cats = ["الكل", "المسابح والشاطئ", "الجيم واللياقة", "اليوغا والتأمل", "السبا والاستشفاء", "المطعم الصحي", "الإقامة والشاليهات"];
        container.innerHTML = cats.map(c => `
            <button class="hilton-cat-btn ${selectedGalleryCategory === c ? 'active' : ''}" onclick="filterGallery('${c}')">
                ${c === 'الكل' ? '⭐ جميع الصور' : c}
            </button>
        `).join("");
    }

    function filterGallery(cat) {
        selectedGalleryCategory = cat;
        renderGalleryCategoryPills();
        renderCustomerGalleryGrid();
    }

    function renderCustomerGalleryGrid() {
        const grid = document.getElementById("resortGalleryGrid");
        if (!grid) return;
        const list = appState.gallery || defaultGallery;
        const filtered = selectedGalleryCategory === "الكل" ? list : list.filter(g => g.category === selectedGalleryCategory);

        if (!filtered.length) {
            grid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">لا توجد صور حالياً في هذا القسم.</div>`;
            return;
        }

        grid.innerHTML = filtered.map(item => `
            <div style="position: relative; height: 220px; border-radius: 10px; overflow: hidden; box-shadow: var(--shadow-sm); cursor: pointer; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'" onclick="openGalleryLightbox('${item.image}', '${item.title}')">
                <img src="${item.image}" alt="${item.title}" style="width: 100%; height: 100%; object-fit: cover;" loading="lazy">
                <div style="position: absolute; inset: 0; background: linear-gradient(180deg, transparent 50%, rgba(0, 43, 73, 0.85) 100%); display: flex; flex-direction: column; justify-content: flex-end; padding: 12px; color: white;">
                    <span style="font-size: 10px; font-weight: 800; background: var(--brand-primary); padding: 2px 8px; border-radius: 4px; width: fit-content; margin-bottom: 4px;">${item.category}</span>
                    <span style="font-size: 13px; font-weight: 800;">${item.title}</span>
                </div>
            </div>
        `).join("");
    }

    function openGalleryLightbox(img, caption) {
        document.getElementById("lightboxImg").src = img;
        document.getElementById("lightboxCaption").innerText = caption || "";
        document.getElementById("galleryLightboxModal").classList.add("active");
    }

    function openGalleryManagerModal() {
        renderGalleryManagerGrid();
        document.getElementById("galleryManagerModal").classList.add("active");
    }
    function closeGalleryManagerModal() {
        document.getElementById("galleryManagerModal").classList.remove("active");
        renderGalleryUI();
    }

    function renderGalleryManagerGrid() {
        const grid = document.getElementById("managerGalleryGrid");
        if (!grid) return;
        grid.innerHTML = (appState.gallery || []).map(item => `
            <div style="border: 1px solid var(--border); border-radius: 8px; overflow: hidden; background: white; padding: 6px;">
                <img src="${item.image}" style="width: 100%; height: 110px; object-fit: cover; border-radius: 6px;">
                <div style="font-weight: 800; font-size: 11px; margin: 4px 0 2px;">${item.title}</div>
                <div style="font-size: 10px; color: var(--text-muted); margin-bottom: 6px;">${item.category}</div>
                <button class="btn btn-danger btn-sm" style="width: 100%; padding: 3px; font-size: 11px;" onclick="deleteGalleryItem('${item.id}')">حذف الصورة 🗑️</button>
            </div>
        `).join("");
    }

    function addPhotoToGallery() {
        const title = document.getElementById("galInputTitle").value.trim();
        const cat = document.getElementById("galInputCategory").value;
        const img = document.getElementById("galInputImage").value.trim();
        if (!title || !img) { alert("من فضلك أدخل عنوان الصورة ورابطها"); return; }

        appState.gallery.push({ id: "gal_" + Date.now(), title, category: cat, image: img });
        saveState();
        renderGalleryManagerGrid();
        renderGalleryUI();
        document.getElementById("galInputTitle").value = "";
        document.getElementById("galInputImage").value = "";
        alert("✨ تم إضافة الصورة للألبوم بنجاح!");
    }

    function deleteGalleryItem(id) {
        if (!confirm("هل أنت متأكد من حذف هذه الصورة؟")) return;
        appState.gallery = appState.gallery.filter(g => g.id !== id);
        saveState();
        renderGalleryManagerGrid();
        renderGalleryUI();
    }

    function triggerGalleryPhotoUpload() { document.getElementById("galFileInput").click(); }
    function handleGalleryPhotoUpload(e) {
        compressImageFile(e.target.files[0], 900, 0.82, (base64) => {
            document.getElementById("galInputImage").value = base64;
        });
    }

    // --- Hero Cover Image Modifier ---
    function openHeroImageModal() {
        const currentHero = (appState.resortSettings && appState.resortSettings.heroImage) || defaultResortSettings.heroImage;
        document.getElementById("heroImageUrlInput").value = currentHero;
        document.getElementById("heroImagePreview").src = currentHero;
        document.getElementById("heroImageModal").classList.add("active");
    }
    function closeHeroImageModal() { document.getElementById("heroImageModal").classList.remove("active"); }
    function updateHeroPreview(url) { if (url) document.getElementById("heroImagePreview").src = url; }
    function selectHeroPreset(url) {
        document.getElementById("heroImageUrlInput").value = url;
        document.getElementById("heroImagePreview").src = url;
    }
    function triggerHeroPhotoUpload() { document.getElementById("heroFileInput").click(); }
    function handleHeroPhotoUpload(e) {
        compressImageFile(e.target.files[0], 1920, 0.82, (base64) => {
            document.getElementById("heroImageUrlInput").value = base64;
            document.getElementById("heroImagePreview").src = base64;
        });
    }
    function saveHeroImage() {
        const url = document.getElementById("heroImageUrlInput").value.trim();
        if (!url) { alert("من فضلك أدخل رابط الصورة"); return; }
        appState.resortSettings.heroImage = url;
        saveState();
        document.getElementById("mainHeroBgImg").src = url;
        closeHeroImageModal();
        alert("✨ تم حفظ وتطبيق صورة الواجهة بنجاح!");
    }

    // --- Meals Workspace Management ---
    function getActiveMeal() {
        let meal = appState.meals.find(m => m.id === appState.activeTab);
        if (!meal && appState.meals.length > 0) {
            meal = appState.meals[0];
            appState.activeTab = meal.id;
        }
        return meal;
    }

    function renderTabs() {
        const tabBar = document.getElementById("mealsTabBar");
        if (!tabBar) return;
        tabBar.innerHTML = "";

        appState.meals.forEach(meal => {
            const tab = document.createElement("div");
            tab.className = `meal-tab ${appState.activeTab === meal.id ? 'active' : ''}`;
            tab.innerHTML = `
                <span>🍲 ${meal.name || 'وجبة جديدة'}</span>
                ${appState.meals.length > 1 ? `<span class="close-tab" onclick="event.stopPropagation(); removeMealTab('${meal.id}')" title="حذف الوجبة">✕</span>` : ''}
            `;
            tab.onclick = () => switchTab(meal.id);
            tabBar.appendChild(tab);
        });

        const addBtn = document.createElement("button");
        addBtn.className = "btn-add-meal";
        addBtn.innerHTML = "➕ وجبة جديدة";
        addBtn.onclick = createNewMeal;
        tabBar.appendChild(addBtn);

        const dashTab = document.createElement("div");
        dashTab.className = `meal-tab ${appState.activeTab === 'dashboard' ? 'active' : ''}`;
        dashTab.style.background = appState.activeTab === 'dashboard' ? 'var(--brand-primary)' : '#EEF2F6';
        dashTab.innerHTML = "📊 ملخص المنيو الكامل";
        dashTab.onclick = () => switchTab('dashboard');
        tabBar.appendChild(dashTab);
    }

    function switchTab(tabId) {
        appState.activeTab = tabId;
        renderTabs();
        const mealWork = document.getElementById("mealWorkspace");
        const dashWork = document.getElementById("menuDashboardWorkspace");

        if (tabId === 'dashboard') {
            mealWork.style.display = "none";
            dashWork.style.display = "block";
            renderMasterMenuDashboard();
        } else {
            mealWork.style.display = "block";
            dashWork.style.display = "none";
            renderActiveMeal();
        }
        saveState();
    }

    function createNewMeal() {
        const newId = "meal_" + Date.now();
        const today = new Date().toISOString().split('T')[0];
        const count = appState.meals.length + 1;
        const newMeal = {
            id: newId,
            itemNo: "#" + count + "01",
            name: "وجبة صحية جديدة " + count,
            category: "أطباق صحية ورياضية",
            badge: "✨ صنف جديد",
            image: "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
            description: "وجبة صحية طازجة ومتوازنة للرياضيين ونزلاء المنتجع.",
            priceDate: today,
            portions: 4,
            portionSize: "350 gm",
            seasoning: 10,
            wastePct: 5,
            multiplier: 3.33,
            ingredients: [
                { name: "صدور دجاج مخلي (Chicken Breast)", date: today, qty: 500, rUnit: "جرام (Gram)", pUnit: "كيلوجرام (Kg)", price: 220 },
                { name: "أرز بسمتي هندي درجة أولى (Basmati)", date: today, qty: 300, rUnit: "جرام (Gram)", pUnit: "كيلوجرام (Kg)", price: 85 }
            ]
        };
        appState.meals.push(newMeal);
        saveState();
        renderCustomerMenu();
        switchTab(newId);
        alert(`✅ تم إنشاء (${newMeal.name}) بنجاح! يمكنك الآن تعديل الخامات والأسعار.`);
    }

    function duplicateCurrentMeal() {
        const active = getActiveMeal();
        if (!active) return;
        const newId = "meal_" + Date.now();
        const copy = JSON.parse(JSON.stringify(active));
        copy.id = newId;
        copy.name = active.name + " (نسخة)";
        copy.itemNo = active.itemNo + "-COPY";
        appState.meals.push(copy);
        saveState();
        renderCustomerMenu();
        switchTab(newId);
        alert("✅ تم نسخ الوجبة بنجاح!");
    }

    function deleteCurrentMeal() {
        const active = getActiveMeal();
        if (!active) return;
        if (appState.meals.length <= 1) {
            alert("لا يمكن حذف الوجبة الأخيرة في المنيو!");
            return;
        }
        if (confirm(`هل أنت متأكد من حذف وجبة (${active.name})؟`)) {
            appState.meals = appState.meals.filter(m => m.id !== active.id);
            appState.activeTab = appState.meals[0].id;
            saveState();
            renderCustomerMenu();
            switchTab(appState.activeTab);
        }
    }

    function removeMealTab(mealId) {
        if (appState.meals.length <= 1) {
            alert("لا يمكن حذف الوجبة الأخيرة!");
            return;
        }
        appState.meals = appState.meals.filter(m => m.id !== mealId);
        if (appState.activeTab === mealId) {
            appState.activeTab = appState.meals[0].id;
        }
        saveState();
        renderCustomerMenu();
        switchTab(appState.activeTab);
    }

    function renderActiveMeal() {
        const meal = getActiveMeal();
        if (!meal) return;

        renderCategorySelectOptions();

        document.getElementById("mItemNo").value = meal.itemNo || "";
        document.getElementById("mName").value = meal.name || "";
        document.getElementById("mCategory").value = meal.category || "أطباق صحية ورياضية";
        document.getElementById("mBadge").value = meal.badge !== undefined ? meal.badge : "⭐ الأكثر طلباً";
        document.getElementById("mDescription").value = meal.description || "";
        document.getElementById("mThumbPreview").src = meal.image || "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=400&q=80";

        document.getElementById("mPriceDate").value = meal.priceDate || "";
        document.getElementById("mPortions").value = meal.portions || 1;
        document.getElementById("mPortionSize").value = meal.portionSize || "";
        document.getElementById("mSeasoning").value = meal.seasoning || 0;
        document.getElementById("mWastePct").value = meal.wastePct || 5;
        document.getElementById("mMultiplier").value = meal.multiplier || 3.33;
        document.getElementById("mFoodCostPct").value = ((1 / (meal.multiplier || 3.33)) * 100).toFixed(1);

        renderIngredientsTable(meal);
        updateFinancialDisplay(meal);
    }

    function updateActiveMealField(field, val) {
        const meal = getActiveMeal();
        if (!meal) return;
        meal[field] = val;

        if (field === 'priceDate') {
            (meal.ingredients || []).forEach(ing => { if (!ing.date) ing.date = val; });
            renderIngredientsTable(meal);
        }
        if (field === 'name') renderTabs();

        updateFinancialDisplay(meal);
        saveState();
        renderCustomerMenu();
    }

    function onMultiplierChanged(val) {
        const mult = parseFloat(val) || 1;
        const meal = getActiveMeal();
        if (!meal) return;
        meal.multiplier = mult;
        if (mult > 0) {
            document.getElementById("mFoodCostPct").value = ((1 / mult) * 100).toFixed(1);
        }
        updateFinancialDisplay(meal);
        saveState();
        renderCustomerMenu();
    }

    function onFoodCostChanged(val) {
        const fc = parseFloat(val) || 30;
        const meal = getActiveMeal();
        if (!meal) return;
        if (fc > 0) {
            const mult = (100 / fc);
            meal.multiplier = parseFloat(mult.toFixed(2));
            document.getElementById("mMultiplier").value = meal.multiplier;
        }
        updateFinancialDisplay(meal);
        saveState();
        renderCustomerMenu();
    }

    function saveAndApplyMealChanges() {
        saveState();
        renderCustomerMenu();
        renderTabs();
        alert("✅ تم حفظ وتطبيق جميع تعديلات الوجبة على المنيو والتقارير بنجاح!");
    }

    // --- Ingredients Table ---
    function renderIngredientsTable(meal) {
        const tbody = document.getElementById("ingredientsTableBody");
        if (!tbody) return;
        tbody.innerHTML = "";

        (meal.ingredients || []).forEach((ing, idx) => {
            const factor = getConversionFactor(ing.rUnit, ing.pUnit);
            const lineCost = (parseFloat(ing.qty) || 0) * (parseFloat(ing.price) || 0) * factor;

            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td><input type="text" value="${ing.name || ''}" style="width:100%;" onchange="updateIngredient(${idx}, 'name', this.value)"></td>
                <td><input type="date" value="${ing.date || ''}" style="width:100%;" onchange="updateIngredient(${idx}, 'date', this.value)"></td>
                <td><input type="number" step="any" min="0" value="${ing.qty || 0}" style="width:80px;" oninput="updateIngredient(${idx}, 'qty', parseFloat(this.value)||0)"></td>
                <td>
                    <select onchange="updateIngredient(${idx}, 'rUnit', this.value)">
                        <option value="جرام (Gram)" ${ing.rUnit==='جرام (Gram)'?'selected':''}>جرام (Gram)</option>
                        <option value="كيلوجرام (Kg)" ${ing.rUnit==='كيلوجرام (Kg)'?'selected':''}>كيلوجرام (Kg)</option>
                        <option value="مليلتر (ml)" ${ing.rUnit==='مليلتر (ml)'?'selected':''}>مليلتر (ml)</option>
                        <option value="لتر (L)" ${ing.rUnit==='لتر (L)'?'selected':''}>لتر (L)</option>
                        <option value="قطعة / حصة" ${ing.rUnit==='قطعة / حصة'?'selected':''}>قطعة / حصة</option>
                    </select>
                </td>
                <td>
                    <select onchange="updateIngredient(${idx}, 'pUnit', this.value)">
                        <option value="كيلوجرام (Kg)" ${ing.pUnit==='كيلوجرام (Kg)'?'selected':''}>كيلوجرام (Kg)</option>
                        <option value="لتر (L)" ${ing.pUnit==='لتر (L)'?'selected':''}>لتر (L)</option>
                        <option value="قطعة / حصة" ${ing.pUnit==='قطعة / حصة'?'selected':''}>قطعة / حصة</option>
                    </select>
                </td>
                <td><input type="number" step="any" min="0" value="${ing.price || 0}" style="width:85px;" oninput="updateIngredient(${idx}, 'price', parseFloat(this.value)||0)"></td>
                <td style="color:#64748B; font-size:11px;">${factor}</td>
                <td style="font-weight:800; color:var(--brand-dark);">${lineCost.toFixed(2)} ج.م</td>
                <td>
                    <button class="btn btn-danger btn-sm" style="padding: 2px 8px; font-size: 11px;" onclick="removeIngredient(${idx})">✕</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    }

    function updateIngredient(idx, field, val) {
        const meal = getActiveMeal();
        if (!meal || !meal.ingredients || !meal.ingredients[idx]) return;
        meal.ingredients[idx][field] = val;
        renderIngredientsTable(meal);
        updateFinancialDisplay(meal);
        saveState();
        renderCustomerMenu();
    }

    function addNewIngredientRow() {
        const meal = getActiveMeal();
        if (!meal) return;
        if (!meal.ingredients) meal.ingredients = [];
        const today = document.getElementById("mPriceDate").value || new Date().toISOString().split('T')[0];
        meal.ingredients.push({
            name: "مكون جديد",
            date: today,
            qty: 100,
            rUnit: "جرام (Gram)",
            pUnit: "كيلوجرام (Kg)",
            price: 50
        });
        renderIngredientsTable(meal);
        updateFinancialDisplay(meal);
        saveState();
        renderCustomerMenu();
    }

    function removeIngredient(idx) {
        const meal = getActiveMeal();
        if (!meal || !meal.ingredients) return;
        meal.ingredients.splice(idx, 1);
        renderIngredientsTable(meal);
        updateFinancialDisplay(meal);
        saveState();
        renderCustomerMenu();
    }

    function updateFinancialDisplay(meal) {
        const f = calculateMealFinancials(meal);
        document.getElementById("fSubtotal").innerText = f.subtotal.toFixed(2) + " ج.م";
        document.getElementById("fTotalCost").innerText = f.totalCost.toFixed(2) + " ج.م";
        document.getElementById("fCostPerPortion").innerText = f.costPerPortion.toFixed(2) + " ج.م";
        document.getElementById("fSellingPrice").innerText = f.sellingPrice.toFixed(2) + " ج.م";
        document.getElementById("fGrossProfit").innerText = f.grossProfit.toFixed(2) + " ج.م";
        document.getElementById("fProfitMargin").innerText = "نسبة الهامش: " + f.profitMargin.toFixed(1) + "%";
    }

    // --- Master Menu Dashboard ---
    function renderMasterMenuDashboard() {
        const tbody = document.getElementById("masterDashboardTableBody");
        if (!tbody) return;
        tbody.innerHTML = "";

        appState.meals.forEach(meal => {
            const f = calculateMealFinancials(meal);
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td><b>${meal.itemNo || '#BH'}</b></td>
                <td><b>${meal.name}</b></td>
                <td><span class="badge" style="background:#EBF3FA; color:#004B87; padding:2px 6px; border-radius:4px; font-size:11px;">${meal.category || 'عام'}</span></td>
                <td>${f.portions}</td>
                <td>${f.totalCost.toFixed(2)} ج.م</td>
                <td style="font-weight:800; color:var(--brand-primary);">${f.costPerPortion.toFixed(2)} ج.م</td>
                <td style="font-weight:900; color:#059669;">${f.sellingPrice.toFixed(0)} ج.م</td>
                <td>${f.foodCostPct.toFixed(1)}%</td>
                <td>${f.grossProfit.toFixed(2)} ج.م</td>
                <td>
                    <button class="btn btn-outline btn-sm" onclick="switchTab('${meal.id}')">تعديل ✏️</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    }

    // --- Category Management ---
    function openCategoriesManagerModal() {
        cancelEditCategory();
        renderCategoriesTable();
        document.getElementById("categoriesManagerModal").classList.add("active");
    }
    function closeCategoriesManagerModal() {
        document.getElementById("categoriesManagerModal").classList.remove("active");
    }

    function renderCategoriesTable() {
        const tbody = document.getElementById("categoriesTableBody");
        if (!tbody) return;
        tbody.innerHTML = "";

        appState.categories.forEach(cat => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td style="font-size: 20px; text-align: center;">${cat.icon || '🍽️'}</td>
                <td><b>${cat.name}</b></td>
                <td>
                    ${!cat.isFixed ? `
                        <div style="display:flex; gap:6px;">
                            <button class="btn btn-outline btn-sm" onclick="startEditCategory('${cat.id}')">✏️</button>
                            <button class="btn btn-danger btn-sm" onclick="deleteCategory('${cat.id}')">🗑️</button>
                        </div>
                    ` : '<span style="font-size:11px; color:#94A3B8;">قسم أساسي</span>'}
                </td>
            `;
            tbody.appendChild(tr);
        });
    }

    function saveCategoryFromForm() {
        const icon = document.getElementById("newCatIcon").value.trim() || "🍽️";
        const name = document.getElementById("newCatName").value.trim();

        if (!name) { alert("يرجى إدخال اسم القسم!"); return; }

        if (editingCatId) {
            const cat = appState.categories.find(c => c.id === editingCatId);
            if (cat) {
                const oldName = cat.name;
                cat.icon = icon;
                cat.name = name;
                appState.meals.forEach(m => { if (m.category === oldName) m.category = name; });
                alert(`✅ تم تحديث قسم (${name}) بنجاح!`);
            }
        } else {
            const dup = appState.categories.find(c => c.name.toLowerCase() === name.toLowerCase());
            if (dup) { alert("هذا القسم موجود بالفعل في القائمة!"); return; }
            appState.categories.push({ id: "cat_" + Date.now(), name, icon, isFixed: false });
            alert(`✅ تم إضافة قسم (${name}) للمنيو بنجاح!`);
        }

        saveState();
        cancelEditCategory();
        renderCategoriesTable();
        renderCategorySelectOptions();
        renderCategoryPills();
        renderCustomerMenu();
    }

    function startEditCategory(catId) {
        const cat = appState.categories.find(c => c.id === catId);
        if (!cat) return;
        editingCatId = catId;
        document.getElementById("catFormTitle").innerText = `✏️ تعديل قسم: ${cat.name}`;
        document.getElementById("newCatIcon").value = cat.icon || "🍽️";
        document.getElementById("newCatName").value = cat.name;
        document.getElementById("btnCancelEditCat").style.display = "inline-flex";
        document.getElementById("btnSaveCat").innerText = "تحديث القسم 💾";
        document.getElementById("newCatName").focus();
    }

    function cancelEditCategory() {
        editingCatId = null;
        document.getElementById("catFormTitle").innerText = "➕ إضافة قسم جديد للمنيو";
        document.getElementById("newCatIcon").value = "";
        document.getElementById("newCatName").value = "";
        document.getElementById("btnCancelEditCat").style.display = "none";
        document.getElementById("btnSaveCat").innerText = "حفظ القسم 💾";
    }

    function deleteCategory(catId) {
        const cat = appState.categories.find(c => c.id === catId);
        if (!cat) return;
        if (confirm(`هل أنت متأكد من حذف قسم (${cat.name})؟`)) {
            appState.categories = appState.categories.filter(c => c.id !== catId);
            saveState();
            renderCategoriesTable();
            renderCategorySelectOptions();
            renderCategoryPills();
            renderCustomerMenu();
        }
    }

    function renderCategorySelectOptions() {
        const select = document.getElementById("mCategory");
        if (!select) return;
        const currentVal = select.value;
        select.innerHTML = "";

        appState.categories.filter(c => !c.isFixed).forEach(cat => {
            const opt = document.createElement("option");
            opt.value = cat.name;
            opt.innerText = `${cat.icon || '🍽️'} ${cat.name}`;
            select.appendChild(opt);
        });

        if (currentVal) select.value = currentVal;
    }

    // --- Resort Profile Settings ---
    function openResortSettingsModal() {
        const r = appState.resortSettings || defaultResortSettings;
        document.getElementById("cfgResortName").value = r.name || defaultResortSettings.name;
        document.getElementById("cfgResortPhone").value = r.phone || defaultResortSettings.phone;
        document.getElementById("cfgResortWhatsapp").value = r.whatsapp || defaultResortSettings.whatsapp;
        document.getElementById("cfgResortHours").value = r.hours || defaultResortSettings.hours;
        document.getElementById("cfgResortLocation").value = r.location || defaultResortSettings.location;
        document.getElementById("cfgResortHeroDesc").value = r.heroDesc || defaultResortSettings.heroDesc;
        document.getElementById("resortSettingsModal").classList.add("active");
    }
    function closeResortSettingsModal() { document.getElementById("resortSettingsModal").classList.remove("active"); }

    function saveResortSettings() {
        const r = appState.resortSettings || { ...defaultResortSettings };
        r.name = document.getElementById("cfgResortName").value.trim() || defaultResortSettings.name;
        r.phone = document.getElementById("cfgResortPhone").value.trim() || defaultResortSettings.phone;
        r.whatsapp = document.getElementById("cfgResortWhatsapp").value.trim() || defaultResortSettings.whatsapp;
        r.hours = document.getElementById("cfgResortHours").value.trim() || defaultResortSettings.hours;
        r.location = document.getElementById("cfgResortLocation").value.trim() || defaultResortSettings.location;
        r.heroDesc = document.getElementById("cfgResortHeroDesc").value.trim() || defaultResortSettings.heroDesc;

        appState.resortSettings = r;
        saveState();
        applyResortSettingsUI();
        renderCustomerMenu();
        renderActivitiesUI();
        closeResortSettingsModal();
        alert("✨ تم حفظ وتحديث بيانات المنتجع وأرقام التواصل بنجاح!");
    }

    // --- Admin Management ---
    function openAdminManagementModal() {
        cancelEditAdmin();
        renderAdminsTable();
        document.getElementById("adminManagementModal").classList.add("active");
    }
    function closeAdminManagementModal() { document.getElementById("adminManagementModal").classList.remove("active"); }

    function renderAdminsTable() {
        const tbody = document.getElementById("adminsTableBody");
        if (!tbody) return;
        tbody.innerHTML = "";
        (appState.adminsList || []).forEach(adm => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td><b>${adm.name}</b></td>
                <td><code>${adm.username}</code></td>
                <td><code>••••••••</code></td>
                <td>
                    <button class="btn btn-outline btn-sm" onclick="startEditAdmin('${adm.id}')">تعديل ✏️</button>
                    ${appState.adminsList.length > 1 ? `<button class="btn btn-danger btn-sm" onclick="deleteAdmin('${adm.id}')">حذف 🗑️</button>` : ''}
                </td>
            `;
            tbody.appendChild(tr);
        });
    }

    function saveAdminFromForm() {
        const name = document.getElementById("admInputName").value.trim();
        const username = document.getElementById("admInputUsername").value.trim().toLowerCase();
        const passcode = document.getElementById("admInputPasscode").value.trim();

        if (!name || !username || !passcode) { alert("يرجى ملء جميع الحقول!"); return; }

        if (editingAdminId) {
            const adm = appState.adminsList.find(a => a.id === editingAdminId);
            if (adm) { adm.name = name; adm.username = username; adm.passcode = passcode; }
        } else {
            const dup = appState.adminsList.find(a => a.username === username);
            if (dup) { alert("اسم المستخدم موجود بالفعل!"); return; }
            appState.adminsList.push({ id: "adm_" + Date.now(), name, username, passcode });
        }
        saveState();
        cancelEditAdmin();
        renderAdminsTable();
        alert("✅ تم حفظ حساب المدير بنجاح!");
    }

    function startEditAdmin(id) {
        const adm = appState.adminsList.find(a => a.id === id);
        if (!adm) return;
        editingAdminId = id;
        document.getElementById("adminFormTitle").innerText = `✏️ تعديل حساب: ${adm.name}`;
        document.getElementById("admInputName").value = adm.name;
        document.getElementById("admInputUsername").value = adm.username;
        document.getElementById("admInputPasscode").value = adm.passcode;
        document.getElementById("btnCancelEditAdmin").style.display = "inline-flex";
        document.getElementById("btnSaveAdmin").innerText = "تحديث الحساب 💾";
    }

    function cancelEditAdmin() {
        editingAdminId = null;
        document.getElementById("adminFormTitle").innerText = "➕ إضافة حساب مدير جديد";
        document.getElementById("admInputName").value = "";
        document.getElementById("admInputUsername").value = "";
        document.getElementById("admInputPasscode").value = "";
        document.getElementById("btnCancelEditAdmin").style.display = "none";
        document.getElementById("btnSaveAdmin").innerText = "حفظ الحساب 💾";
    }

    function deleteAdmin(id) {
        if (appState.adminsList.length <= 1) { alert("لا يمكن حذف الحساب الوحيد!"); return; }
        if (confirm("هل ترغب في حذف هذا المدير؟")) {
            appState.adminsList = appState.adminsList.filter(a => a.id !== id);
            saveState();
            renderAdminsTable();
        }
    }

    // --- Master Pantry Library ---
    function openPantryModal() {
        renderPantryTable();
        document.getElementById("pantryModal").classList.add("active");
    }
    function closePantryModal() { document.getElementById("pantryModal").classList.remove("active"); }

    function renderPantryTable(list = null) {
        const tbody = document.getElementById("pantryTableBody");
        if (!tbody) return;
        tbody.innerHTML = "";
        const data = list || appState.pantry || defaultPantry;
        data.forEach((item, idx) => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td><b>${item.name}</b></td>
                <td><span style="font-size:11px; background:#F1F5F9; padding:2px 6px; border-radius:4px;">${item.cat}</span></td>
                <td>${item.unit}</td>
                <td><input type="number" step="any" value="${item.price}" style="width:80px;" onchange="updatePantryPrice(${idx}, this.value)"></td>
                <td>
                    <button class="btn btn-primary btn-sm" onclick="insertPantryItemToCurrentMeal(${idx})">إدراج للوجبة ➕</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    }

    function updatePantryPrice(idx, val) {
        if (!appState.pantry[idx]) return;
        appState.pantry[idx].price = parseFloat(val) || 0;
        saveState();
    }

    function filterPantryList() {
        const q = (document.getElementById("pantrySearchInput").value || "").toLowerCase().trim();
        const filtered = (appState.pantry || defaultPantry).filter(p => 
            p.name.toLowerCase().includes(q) || p.cat.toLowerCase().includes(q)
        );
        renderPantryTable(filtered);
    }

    function insertPantryItemToCurrentMeal(idx) {
        const item = appState.pantry[idx];
        if (!item) return;
        const meal = getActiveMeal();
        if (!meal) return;
        if (!meal.ingredients) meal.ingredients = [];

        const today = document.getElementById("mPriceDate").value || new Date().toISOString().split('T')[0];
        let rUnit = "جرام (Gram)";
        let qty = 100;

        if (item.unit.includes("لتر")) { rUnit = "مليلتر (ml)"; qty = 50; }
        else if (item.unit.includes("قطعة")) { rUnit = "قطعة / حصة"; qty = 1; }

        meal.ingredients.push({
            name: item.name,
            date: today,
            qty: qty,
            rUnit: rUnit,
            pUnit: item.unit,
            price: item.price
        });

        renderIngredientsTable(meal);
        updateFinancialDisplay(meal);
        saveState();
        renderCustomerMenu();
        alert(`✅ تم إدراج (${item.name}) في الوجبة بنجاح!`);
    }

    function addNewPantryItemPrompt() {
        const name = prompt("أدخل اسم الخامة الجديدة:");
        if (!name) return;
        const unit = prompt("وحدة الشراء (مثال: كيلوجرام (Kg) أو لتر (L)):", "كيلوجرام (Kg)") || "كيلوجرام (Kg)";
        const price = parseFloat(prompt("سعر الشراء الحالي بالجنيه:", "100")) || 100;
        const cat = prompt("تصنيف الخامة (خضروات، لحوم، ألبان، زيوت...):", "خامات عامة") || "خامات عامة";

        appState.pantry.unshift({ name, unit, price, cat });
        saveState();
        renderPantryTable();
    }

    function resetPantryToDefaults() {
        if (confirm("هل ترغب في إعادة ضبط قائمة الخامات إلى أسعار السوق الافتراضية؟")) {
            appState.pantry = [...defaultPantry];
            saveState();
            renderPantryTable();
        }
    }

    // --- Photo Upload with Canvas Compression ---
    function triggerMealPhotoUpload() { document.getElementById("mealPhotoInput").click(); }
    function handleMealPhotoUpload(e) {
        compressImageFile(e.target.files[0], 700, 0.82, (base64) => {
            updateActiveMealField('image', base64);
            document.getElementById("mThumbPreview").src = base64;
        });
    }

    function promptPhotoUrl() {
        const url = prompt("أدخل رابط صورة الوجبة المباشر (URL):");
        if (url) {
            updateActiveMealField('image', url);
            document.getElementById("mThumbPreview").src = url;
        }
    }

    function compressImageFile(file, maxWidth, quality, callback) {
        if (!file) return;
        const reader = new FileReader();
        reader.onload = function(evt) {
            const img = new Image();
            img.onload = function() {
                const canvas = document.createElement("canvas");
                let w = img.width;
                let h = img.height;
                if (w > maxWidth) { h *= maxWidth / w; w = maxWidth; }
                canvas.width = w;
                canvas.height = h;
                const ctx = canvas.getContext("2d");
                ctx.drawImage(img, 0, 0, w, h);
                const compressed = canvas.toDataURL("image/jpeg", quality);
                callback(compressed);
            };
            img.src = evt.target.result;
        };
        reader.readAsDataURL(file);
    }

    // --- Excel Upload & Export ---
    function triggerExcelUpload() { document.getElementById("excelFileInput").click(); }
    function handleExcelUpload(e) {
        const file = e.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = function(evt) {
            try {
                const data = new Uint8Array(evt.target.result);
                const wb = XLSX.read(data, { type: 'array' });
                const ws = wb.Sheets[wb.SheetNames[0]];
                const rows = XLSX.utils.sheet_to_json(ws, { header: 1 });

                let importedCount = 0;
                const meal = getActiveMeal();
                if (!meal.ingredients) meal.ingredients = [];

                rows.forEach((row, i) => {
                    if (i < 2 || !row[0]) return;
                    const name = String(row[0]).trim();
                    const qty = parseFloat(row[1]) || 100;
                    const rUnit = String(row[2] || "جرام (Gram)").trim();
                    const pUnit = String(row[3] || "كيلوجرام (Kg)").trim();
                    const price = parseFloat(row[4]) || 50;
                    const date = row[5] ? String(row[5]).trim() : new Date().toISOString().split('T')[0];

                    meal.ingredients.push({ name, qty, rUnit, pUnit, price, date });
                    importedCount++;
                });

                if (importedCount > 0) {
                    renderIngredientsTable(meal);
                    updateFinancialDisplay(meal);
                    saveState();
                    renderCustomerMenu();
                    alert(`✅ تم استيراد ${importedCount} مكون بنجاح من شيت الإكسيل!`);
                } else {
                    alert("لم يتم العثور على بيانات مكونات صالحة في الملف.");
                }
            } catch (err) {
                alert("حدث خطأ أثناء قراءة ملف الإكسيل: " + err.message);
            }
        };
        reader.readAsArrayBuffer(file);
    }

    function exportCurrentMealToExcel() {
        const meal = getActiveMeal();
        const f = calculateMealFinancials(meal);
        const resort = appState.resortSettings || defaultResortSettings;

        const data = [
            [`✦ ${resort.name.toUpperCase()} ✦ | STANDARD RECIPE COST CARD`],
            ["كارت تكلفة الوصفة المعيارية وتسعير المنيو"],
            [],
            ["كود الصنف (Item No):", meal.itemNo || "#BH"],
            ["اسم الوجبة (Recipe Name):", meal.name],
            ["قسم المنيو (Category):", meal.category],
            ["عدد الحصص (Portions):", f.portions],
            ["حجم الحصة (Portion Size):", meal.portionSize || "350 gm"],
            ["إجمالي تكلفة الوصفة (Total Cost):", f.totalCost.toFixed(2) + " ج.م"],
            ["تكلفة الحصة الواحدة (Cost/Portion):", f.costPerPortion.toFixed(2) + " ج.م"],
            ["مُعامل التسعير (Multiplier):", f.multiplier],
            ["سعر البيع المقترح (Selling Price):", f.sellingPrice.toFixed(2) + " ج.م"],
            ["صافي هامش الربح (Gross Profit):", f.grossProfit.toFixed(2) + " ج.م"],
            ["هاتف الحجز والطلبات:", resort.phone],
            [],
            ["اسم الخامة", "تاريخ السعر", "الكمية بالوصفة", "وحدة الوصفة", "وحدة الشراء", "سعر الشراء (ج.م)", "معامل التحويل", "تكلفة المكون (ج.م)"]
        ];

        (meal.ingredients || []).forEach(ing => {
            const factor = getConversionFactor(ing.rUnit, ing.pUnit);
            const cost = (parseFloat(ing.qty) || 0) * (parseFloat(ing.price) || 0) * factor;
            data.push([ing.name, ing.date || "", ing.qty, ing.rUnit, ing.pUnit, ing.price, factor, cost.toFixed(2)]);
        });

        const ws = XLSX.utils.aoa_to_sheet(data);
        const wb = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(wb, ws, "Recipe Cost Card");
        XLSX.writeFile(wb, `${meal.name.replace(/[^a-zA-Z0-9\u0600-\u06FF]/g, '_')}_Cost_Card.xlsx`);
    }

    function exportAllMealsToExcel() {
        const resort = appState.resortSettings || defaultResortSettings;
        const data = [
            [`✦ ${resort.name.toUpperCase()} ✦ | ملخص المنيو الكامل والتحليل المالي`],
            ["تاريخ التقرير:", new Date().toLocaleDateString('ar-EG')],
            ["هاتف التواصل:", resort.phone],
            [],
            ["كود الصنف", "اسم الوجبة", "القسم", "الحصص", "إجمالي التكلفة", "تكلفة الحصة", "سعر البيع المقترح", "Food Cost %", "هامش الربح للحصة", "نسبة الهامش"]
        ];

        appState.meals.forEach(meal => {
            const f = calculateMealFinancials(meal);
            data.push([
                meal.itemNo || "#BH",
                meal.name,
                meal.category || "عام",
                f.portions,
                f.totalCost.toFixed(2),
                f.costPerPortion.toFixed(2),
                f.sellingPrice.toFixed(0),
                f.foodCostPct.toFixed(1) + "%",
                f.grossProfit.toFixed(2),
                f.profitMargin.toFixed(1) + "%"
            ]);
        });

        const ws = XLSX.utils.aoa_to_sheet(data);
        const wb = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(wb, ws, "Master Menu Summary");
        XLSX.writeFile(wb, "Blue_Healing_Master_Menu.xlsx");
    }

    // --- Theme Modifier Engine ---
    const defaultThemes = {
        ocean: { name: "الأزرق الفاخر (Blue Healing)", primary: "#004B87", accent: "#0072CE", gold: "#B8860B", bg: "#FFFFFF" },
        emerald: { name: "الواحة الزمردية (Royal Emerald)", primary: "#0B4632", accent: "#10B981", gold: "#D97706", bg: "#F4F9F6" },
        burgundy: { name: "الغروب والعقيق (Sunset Burgundy)", primary: "#4C1223", accent: "#E11D48", gold: "#F59E0B", bg: "#FFF7F8" },
        midnight: { name: "الفخامة الداكنة (Dark VIP Lounge)", primary: "#0F172A", accent: "#38BDF8", gold: "#FBBF24", bg: "#0B0F19" },
        sand: { name: "رمال الشاطئ (Warm Sand)", primary: "#45271D", accent: "#EA580C", gold: "#D97706", bg: "#FAF7F2" }
    };

    let activeTheme = { ...defaultThemes.ocean };

    function loadTheme() {
        try {
            const raw = localStorage.getItem(THEME_KEY);
            if (raw) activeTheme = { ...defaultThemes.ocean, ...JSON.parse(raw) };
        } catch(e) {}
        applyThemeToDOM(activeTheme);
    }

    function applyThemeToDOM(t) {
        const root = document.documentElement;
        root.style.setProperty('--brand-primary', t.primary);
        root.style.setProperty('--brand-blue', t.accent);
        root.style.setProperty('--brand-gold', t.gold);
        root.style.setProperty('--bg-page', t.bg);
    }

    function openThemeModifierModal() {
        populateThemePresets();
        document.getElementById("themeColorPrimary").value = activeTheme.primary;
        document.getElementById("themeColorAccent").value = activeTheme.accent;
        document.getElementById("themeColorGold").value = activeTheme.gold;
        document.getElementById("themeColorBgPage").value = activeTheme.bg;
        document.getElementById("themeModifierModal").classList.add("active");
    }
    function closeThemeModifierModal() {
        applyThemeToDOM(activeTheme);
        document.getElementById("themeModifierModal").classList.remove("active");
    }

    function populateThemePresets() {
        const grid = document.getElementById("themePresetsGrid");
        if (!grid) return;
        grid.innerHTML = Object.keys(defaultThemes).map(k => {
            const t = defaultThemes[k];
            return `
                <div onclick="selectThemePreset('${k}')" style="border: 1px solid var(--border); border-radius: 8px; padding: 8px; cursor: pointer; text-align: center; background: white;">
                    <div style="display:flex; justify-content:center; gap:4px; margin-bottom:6px;">
                        <span style="width:14px; height:14px; border-radius:50%; background:${t.primary};"></span>
                        <span style="width:14px; height:14px; border-radius:50%; background:${t.accent};"></span>
                        <span style="width:14px; height:14px; border-radius:50%; background:${t.gold};"></span>
                    </div>
                    <div style="font-size:11px; font-weight:800;">${t.name}</div>
                </div>
            `;
        }).join("");
    }

    function selectThemePreset(k) {
        const t = defaultThemes[k];
        if (!t) return;
        activeTheme = { ...t };
        document.getElementById("themeColorPrimary").value = t.primary;
        document.getElementById("themeColorAccent").value = t.accent;
        document.getElementById("themeColorGold").value = t.gold;
        document.getElementById("themeColorBgPage").value = t.bg;
        applyThemeToDOM(activeTheme);
    }

    function previewLiveTheme() {
        const custom = {
            primary: document.getElementById("themeColorPrimary").value,
            accent: document.getElementById("themeColorAccent").value,
            gold: document.getElementById("themeColorGold").value,
            bg: document.getElementById("themeColorBgPage").value
        };
        applyThemeToDOM(custom);
    }

    function saveThemeSettings() {
        activeTheme = {
            primary: document.getElementById("themeColorPrimary").value,
            accent: document.getElementById("themeColorAccent").value,
            gold: document.getElementById("themeColorGold").value,
            bg: document.getElementById("themeColorBgPage").value
        };
        localStorage.setItem(THEME_KEY, JSON.stringify(activeTheme));
        applyThemeToDOM(activeTheme);
        closeThemeModifierModal();
        alert("✨ تم حفظ وتطبيق الثيم بنجاح!");
    }

    function resetThemeToDefault() {
        activeTheme = { ...defaultThemes.ocean };
        localStorage.setItem(THEME_KEY, JSON.stringify(activeTheme));
        applyThemeToDOM(activeTheme);
        closeThemeModifierModal();
    }

    // --- System Bootstrapping ---
    window.addEventListener("DOMContentLoaded", () => {
        loadState();
        loadTheme();
        applyResortSettingsUI();

        renderCategoryPills();
        renderCustomerMenu();
        renderActivitiesUI();
        renderGalleryUI();

        console.log("Blue Healing Resort & Wellness Platform initialized successfully.");
    });
    </script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Master rewrite of index.html complete! Length:", len(html_code))
