import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS variables to support dynamic themes cleanly
# Replace top-navbar background and restaurant-cover-banner background to use var(--brand-dark), var(--brand-primary), etc.
old_navbar_bg = "background: linear-gradient(135deg, #0B132B 0%, #1C2541 60%, #1E3A8A 100%);"
new_navbar_bg = "background: linear-gradient(135deg, var(--brand-dark) 0%, var(--brand-primary) 60%, var(--brand-blue) 100%);"
html = html.replace(old_navbar_bg, new_navbar_bg)

old_cover_bg = "background: linear-gradient(rgba(11, 19, 43, 0.82), rgba(11, 19, 43, 0.90)),"
new_cover_bg = "background: linear-gradient(var(--cover-overlay-1, rgba(11, 19, 43, 0.82)), var(--cover-overlay-2, rgba(11, 19, 43, 0.90))),"
html = html.replace(old_cover_bg, new_cover_bg)

# 2. Add Theme Modifier Button in Manager Control Bar
target_btn = '<button class="btn btn-gold btn-sm" onclick="openResortSettingsModal()">⚙️ بيانات المنتجع وأرقام الهاتف</button>'
theme_btn = '<button class="btn btn-sm" style="background: linear-gradient(135deg, #8B5CF6, #EC4899); color: white; border: none; font-weight: 700; box-shadow: 0 2px 6px rgba(139, 92, 246, 0.35);" onclick="openThemeModifierModal()">🎨 مظهر وثيم المنتجع (Theme)</button>\n                ' + target_btn
if "openThemeModifierModal()" not in html:
    html = html.replace(target_btn, theme_btn, 1)

# 3. Add Theme Modifier Modal HTML before modal-overlay id="pantryModal"
theme_modal_html = """<!-- Modal 7: Theme & Appearance Modifier -->
<div class="modal-overlay" id="themeModifierModal">
    <div class="modal-content" style="max-width: 720px;">
        <div class="modal-header" style="background: linear-gradient(135deg, var(--brand-primary), var(--brand-dark));">
            <span>🎨 تخصيص مظهر وثيم المنتجع والمنيو (Theme Modifier)</span>
            <span style="cursor: pointer; font-size: 18px;" onclick="closeThemeModifierModal()">✕</span>
        </div>
        <div class="modal-body" style="max-height: 80vh; overflow-y: auto;">
            <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 14px;">
                اختر ثيماً فاخراً جاهزاً يطابق هوية منتجعك، أو قم بتخصيص لوحة الألوان بكل حرية لتغيير مظهر المنيو ولوحة الإدارة فوراً.
            </p>

            <!-- Presets Section -->
            <div style="margin-bottom: 18px;">
                <label style="font-weight: 800; font-size: 13px; color: var(--text-main); display: block; margin-bottom: 8px;">
                    ✨ ثيمات فندقية فاخرة جاهزة (Click to apply):
                </label>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px;" id="themePresetsGrid">
                    <!-- Presets rendered dynamically -->
                </div>
            </div>

            <!-- Custom Color Pickers -->
            <div class="manager-sub-box" style="margin-bottom: 16px;">
                <h4 style="font-size: 13px; font-weight: 800; color: var(--text-main); margin-bottom: 10px;">
                    🎛️ تخصيص الألوان الدقيقة (Custom Color Palette):
                </h4>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
                    <div class="form-control">
                        <label>اللون الرئيسي للعلامة (Primary):</label>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <input type="color" id="themeColorPrimary" onchange="previewLiveTheme()">
                            <input type="text" id="themeTextPrimary" style="font-family: monospace; font-size: 12px;" oninput="syncColorInput('Primary', this.value)">
                        </div>
                    </div>
                    <div class="form-control">
                        <label>لون التمييز والأزرار (Accent):</label>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <input type="color" id="themeColorAccent" onchange="previewLiveTheme()">
                            <input type="text" id="themeTextAccent" style="font-family: monospace; font-size: 12px;" oninput="syncColorInput('Accent', this.value)">
                        </div>
                    </div>
                    <div class="form-control">
                        <label>اللون الذهبي / النجوم والأسعار (Gold):</label>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <input type="color" id="themeColorGold" onchange="previewLiveTheme()">
                            <input type="text" id="themeTextGold" style="font-family: monospace; font-size: 12px;" oninput="syncColorInput('Gold', this.value)">
                        </div>
                    </div>
                    <div class="form-control">
                        <label>اللون الداكن للهيدر (Dark Tone):</label>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <input type="color" id="themeColorDark" onchange="previewLiveTheme()">
                            <input type="text" id="themeTextDark" style="font-family: monospace; font-size: 12px;" oninput="syncColorInput('Dark', this.value)">
                        </div>
                    </div>
                    <div class="form-control">
                        <label>خلفية الصفحة (Page BG):</label>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <input type="color" id="themeColorBgPage" onchange="previewLiveTheme()">
                            <input type="text" id="themeTextBgPage" style="font-family: monospace; font-size: 12px;" oninput="syncColorInput('BgPage', this.value)">
                        </div>
                    </div>
                    <div class="form-control">
                        <label>خلفية الكروت (Card BG):</label>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <input type="color" id="themeColorBgCard" onchange="previewLiveTheme()">
                            <input type="text" id="themeTextBgCard" style="font-family: monospace; font-size: 12px;" oninput="syncColorInput('BgCard', this.value)">
                        </div>
                    </div>
                </div>
            </div>

            <!-- Live Mini Preview -->
            <div style="border: 2px dashed var(--border); border-radius: var(--radius-md); padding: 14px; background: var(--bg-page);">
                <span style="font-size: 12px; font-weight: 800; color: var(--text-muted); display: block; margin-bottom: 8px;">
                    👁️ معاينة حية سريعة لبطاقات المنيو (Live Preview):
                </span>
                <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
                    <div style="background: var(--bg-card); padding: 12px 16px; border-radius: var(--radius-md); border: 1px solid var(--border); box-shadow: var(--shadow-sm); display: flex; align-items: center; gap: 10px;">
                        <div style="width: 36px; height: 36px; border-radius: 8px; background: linear-gradient(135deg, var(--brand-primary), var(--brand-blue)); color: white; display: flex; align-items: center; justify-content: center; font-weight: 800;">BH</div>
                        <div>
                            <div style="font-weight: 800; font-size: 13px; color: var(--text-main);">عنوان الوجبة التجريبي</div>
                            <div style="font-size: 11px; color: var(--text-muted);">وصف الطبق الفاخر</div>
                        </div>
                        <span style="font-weight: 800; font-size: 14px; color: var(--brand-gold); margin-right: 10px;">185 ج.م</span>
                        <span style="background: var(--brand-cyan); color: #082F49; font-weight: 800; font-size: 10px; padding: 2px 6px; border-radius: 4px;">شارة</span>
                    </div>
                    <button class="btn btn-primary btn-sm">زر رئيسي</button>
                    <button class="btn btn-whatsapp btn-sm">واتساب 📲</button>
                </div>
            </div>
        </div>
        <div class="modal-footer" style="display: flex; justify-content: space-between;">
            <button class="btn btn-secondary btn-sm" onclick="resetThemeToDefault()">🔄 استعادة الثيم الافتراضي</button>
            <div style="display: flex; gap: 8px;">
                <button class="btn btn-secondary btn-sm" onclick="closeThemeModifierModal()">إلغاء</button>
                <button class="btn btn-gold btn-sm" onclick="saveThemeSettings()">حفظ وتطبيق الثيم للجميع 💾</button>
            </div>
        </div>
    </div>
</div>

"""

if 'id="themeModifierModal"' not in html:
    html = html.replace('<div class="modal-overlay" id="pantryModal">', theme_modal_html + '<div class="modal-overlay" id="pantryModal">', 1)

# 4. Add JavaScript Theme Logic
theme_js = """
    // ========================================================
    // THEME PRESETS & MODIFIER SYSTEM
    // ========================================================
    const THEME_STORAGE_KEY = "bluehealing_theme_config";

    const defaultThemePresets = {
        ocean: {
            id: "ocean",
            name: "الأزرق الفاخر (Blue Healing)",
            subtitle: "الهوية الرسمية الكلاسيكية للمنتجع",
            primary: "#1C2541",
            blue: "#2563EB",
            cyan: "#06B6D4",
            gold: "#D97706",
            dark: "#0B132B",
            bgPage: "#F8FAFC",
            bgCard: "#FFFFFF",
            textMain: "#0F172A",
            textMuted: "#64748B",
            border: "#E2E8F0"
        },
        emerald: {
            id: "emerald",
            name: "الواحة الزمردية (Royal Emerald)",
            subtitle: "أناقة الطبيعة والمنتجعات الصحية الخضراء",
            primary: "#0B4632",
            blue: "#059669",
            cyan: "#10B981",
            gold: "#D97706",
            dark: "#062C1E",
            bgPage: "#F4F9F6",
            bgCard: "#FFFFFF",
            textMain: "#0A261D",
            textMuted: "#4B6B5F",
            border: "#D1E7DD"
        },
        burgundy: {
            id: "burgundy",
            name: "الغروب والعقيق (Sunset Burgundy)",
            subtitle: "أجواء العشاء الرومانسية الفاخرة",
            primary: "#4C1223",
            blue: "#9F1239",
            cyan: "#E11D48",
            gold: "#F59E0B",
            dark: "#2A0914",
            bgPage: "#FFF7F8",
            bgCard: "#FFFFFF",
            textMain: "#2E0A16",
            textMuted: "#7C4E5E",
            border: "#FCE7EC"
        },
        midnight: {
            id: "midnight",
            name: "الفخامة الداكنة (Dark Obsidian VIP)",
            subtitle: "مود عصري ولاونج ليلي متميز",
            primary: "#151F33",
            blue: "#38BDF8",
            cyan: "#0EA5E9",
            gold: "#FBBF24",
            dark: "#070B14",
            bgPage: "#0A0F1D",
            bgCard: "#111827",
            textMain: "#F8FAFC",
            textMuted: "#94A3B8",
            border: "#1F2937"
        },
        warm_sand: {
            id: "warm_sand",
            name: "رمال الشاطئ الدافئة (Boho Sand)",
            subtitle: "طابع بوهو وريفي شاطئي دافئ",
            primary: "#45271D",
            blue: "#B45309",
            cyan: "#EA580C",
            gold: "#D97706",
            dark: "#291811",
            bgPage: "#FAF7F2",
            bgCard: "#FFFFFF",
            textMain: "#2A1810",
            textMuted: "#6B584E",
            border: "#E9DFD5"
        }
    };

    let activeTheme = { ...defaultThemePresets.ocean };

    function loadSavedTheme() {
        try {
            const saved = localStorage.getItem(THEME_STORAGE_KEY);
            if (saved) {
                const parsed = JSON.parse(saved);
                activeTheme = { ...defaultThemePresets.ocean, ...parsed };
            }
        } catch (e) {
            console.error("Failed to load theme:", e);
        }
        applyThemeToDOM(activeTheme);
    }

    function applyThemeToDOM(theme) {
        const root = document.documentElement;
        root.style.setProperty('--brand-primary', theme.primary);
        root.style.setProperty('--brand-blue', theme.blue);
        root.style.setProperty('--brand-cyan', theme.cyan);
        root.style.setProperty('--brand-gold', theme.gold);
        root.style.setProperty('--brand-dark', theme.dark);
        root.style.setProperty('--bg-page', theme.bgPage);
        root.style.setProperty('--bg-card', theme.bgCard);
        root.style.setProperty('--text-main', theme.textMain);
        root.style.setProperty('--text-muted', theme.textMuted);
        root.style.setProperty('--border', theme.border || '#E2E8F0');
    }

    function openThemeModifierModal() {
        populateThemePresetsUI();
        syncThemePickersFromActive();
        document.getElementById("themeModifierModal").classList.add("active");
    }

    function closeThemeModifierModal() {
        // Revert to activeTheme in case user previewed without saving
        applyThemeToDOM(activeTheme);
        document.getElementById("themeModifierModal").classList.remove("active");
    }

    function populateThemePresetsUI() {
        const grid = document.getElementById("themePresetsGrid");
        if (!grid) return;
        grid.innerHTML = "";

        Object.keys(defaultThemePresets).forEach(key => {
            const p = defaultThemePresets[key];
            const isCurrent = activeTheme.id === p.id;
            const card = document.createElement("div");
            card.style.cssText = `
                border: 2px solid ${isCurrent ? 'var(--brand-cyan)' : 'var(--border)'};
                border-radius: var(--radius-md);
                padding: 10px;
                background: ${p.bgCard};
                cursor: pointer;
                transition: all 0.2s;
                position: relative;
                box-shadow: ${isCurrent ? '0 0 0 2px var(--brand-cyan)' : 'var(--shadow-sm)'};
            `;
            card.onclick = () => selectThemePreset(key);

            card.innerHTML = `
                <div style="display: flex; gap: 4px; margin-bottom: 6px;">
                    <div style="width: 18px; height: 18px; border-radius: 50%; background: ${p.dark}; border: 1px solid rgba(255,255,255,0.4);"></div>
                    <div style="width: 18px; height: 18px; border-radius: 50%; background: ${p.primary};"></div>
                    <div style="width: 18px; height: 18px; border-radius: 50%; background: ${p.cyan};"></div>
                    <div style="width: 18px; height: 18px; border-radius: 50%; background: ${p.gold};"></div>
                </div>
                <div style="font-weight: 800; font-size: 11px; color: ${p.textMain}; margin-bottom: 2px;">${p.name}</div>
                <div style="font-size: 9px; color: ${p.textMuted}; line-height: 1.2;">${p.subtitle}</div>
                ${isCurrent ? '<span style="position: absolute; top: 4px; left: 4px; font-size: 11px;">✔️</span>' : ''}
            `;
            grid.appendChild(card);
        });
    }

    function selectThemePreset(key) {
        const preset = defaultThemePresets[key];
        if (!preset) return;
        activeTheme = { ...preset };
        syncThemePickersFromActive();
        applyThemeToDOM(activeTheme);
        populateThemePresetsUI();
    }

    function syncThemePickersFromActive() {
        setPickerVal("themeColorPrimary", "themeTextPrimary", activeTheme.primary);
        setPickerVal("themeColorAccent", "themeTextAccent", activeTheme.cyan);
        setPickerVal("themeColorGold", "themeTextGold", activeTheme.gold);
        setPickerVal("themeColorDark", "themeTextDark", activeTheme.dark);
        setPickerVal("themeColorBgPage", "themeTextBgPage", activeTheme.bgPage);
        setPickerVal("themeColorBgCard", "themeTextBgCard", activeTheme.bgCard);
    }

    function setPickerVal(pickerId, textId, val) {
        const p = document.getElementById(pickerId);
        const t = document.getElementById(textId);
        if (p) p.value = val;
        if (t) t.value = val;
    }

    function syncColorInput(field, val) {
        if (/^#[0-9A-Fa-f]{6}$/.test(val)) {
            const picker = document.getElementById("themeColor" + field);
            if (picker) picker.value = val;
            previewLiveTheme();
        }
    }

    function previewLiveTheme() {
        const customTheme = {
            id: "custom",
            name: "ثيم مخصص",
            subtitle: "ألوان مخصصة من لوحة الإدارة",
            primary: document.getElementById("themeColorPrimary").value,
            blue: document.getElementById("themeColorPrimary").value,
            cyan: document.getElementById("themeColorAccent").value,
            gold: document.getElementById("themeColorGold").value,
            dark: document.getElementById("themeColorDark").value,
            bgPage: document.getElementById("themeColorBgPage").value,
            bgCard: document.getElementById("themeColorBgCard").value,
            textMain: isColorDark(document.getElementById("themeColorBgCard").value) ? "#F8FAFC" : "#0F172A",
            textMuted: isColorDark(document.getElementById("themeColorBgCard").value) ? "#94A3B8" : "#64748B",
            border: isColorDark(document.getElementById("themeColorBgCard").value) ? "#2D3748" : "#E2E8F0"
        };
        document.getElementById("themeTextPrimary").value = customTheme.primary;
        document.getElementById("themeTextAccent").value = customTheme.cyan;
        document.getElementById("themeTextGold").value = customTheme.gold;
        document.getElementById("themeTextDark").value = customTheme.dark;
        document.getElementById("themeTextBgPage").value = customTheme.bgPage;
        document.getElementById("themeTextBgCard").value = customTheme.bgCard;

        applyThemeToDOM(customTheme);
    }

    function isColorDark(hex) {
        if (!hex || hex.length < 7) return false;
        const r = parseInt(hex.slice(1, 3), 16);
        const g = parseInt(hex.slice(3, 5), 16);
        const b = parseInt(hex.slice(5, 7), 16);
        const luminance = (0.299 * r + 0.587 * g + 0.114 * b);
        return luminance < 128;
    }

    function saveThemeSettings() {
        const themeToSave = {
            id: activeTheme.id || "custom",
            name: activeTheme.name || "ثيم مخصص",
            primary: document.getElementById("themeColorPrimary").value,
            blue: document.getElementById("themeColorPrimary").value,
            cyan: document.getElementById("themeColorAccent").value,
            gold: document.getElementById("themeColorGold").value,
            dark: document.getElementById("themeColorDark").value,
            bgPage: document.getElementById("themeColorBgPage").value,
            bgCard: document.getElementById("themeColorBgCard").value,
            textMain: isColorDark(document.getElementById("themeColorBgCard").value) ? "#F8FAFC" : "#0F172A",
            textMuted: isColorDark(document.getElementById("themeColorBgCard").value) ? "#94A3B8" : "#64748B",
            border: isColorDark(document.getElementById("themeColorBgCard").value) ? "#2D3748" : "#E2E8F0"
        };

        activeTheme = themeToSave;
        localStorage.setItem(THEME_STORAGE_KEY, JSON.stringify(activeTheme));
        applyThemeToDOM(activeTheme);
        closeThemeModifierModal();
        alert("✨ تم حفظ وتطبيق الثيم الجديد بنجاح على المنيو ولوحة التحكم!");
    }

    function resetThemeToDefault() {
        if (confirm("هل ترغب في العودة إلى ثيم Blue Healing الافتراضي؟")) {
            activeTheme = { ...defaultThemePresets.ocean };
            localStorage.setItem(THEME_STORAGE_KEY, JSON.stringify(activeTheme));
            applyThemeToDOM(activeTheme);
            syncThemePickersFromActive();
            populateThemePresetsUI();
        }
    }
"""

if "THEME_STORAGE_KEY" not in html:
    # Inject into init or script start
    html = html.replace("<script>\n    const segmentColors =", "<script>\n" + theme_js + "\n    const segmentColors =", 1)

# Ensure loadSavedTheme() is called in DOMContentLoaded
if "loadSavedTheme();" not in html:
    html = html.replace("window.addEventListener('DOMContentLoaded', () => {", "window.addEventListener('DOMContentLoaded', () => {\n        loadSavedTheme();", 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated successfully with Theme Modifier!")
