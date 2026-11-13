with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix setView function
old_setview = """function setView(viewName) {
        appState.currentView = viewName;
        const custSec = document.getElementById("customerSection");
        const mgrSec = document.getElementById("managerSection");
        const roleBadge = document.getElementById("roleBadge");
        const navActions = document.getElementById("topNavActions");

        applyResortSettingsUI();

        if (viewName === "manager") {
            custSec.style.display = "none";
            mgrSec.style.display = "block";
            roleBadge.className = "role-badge role-manager";
            roleBadge.innerText = "لوحة الإدارة والمشرف";

            const adminName = appState.currentLoggedInAdmin ? appState.currentLoggedInAdmin.name : "المدير العام";
            document.getElementById("loggedManagerName").innerText = adminName;

            navActions.innerHTML = `
                <button class="btn btn-outline" style="color:white; border-color:rgba(255,255,255,0.3);" onclick="showCustomerView()">
                    👁️ منيو الزبائن
                </button>
                <button class="btn btn-danger btn-sm" onclick="managerLogout()">
                    🚪 خروج
                </button>
            `;
            renderTabs();
            renderActiveMeal();
        } else {
            custSec.style.display = "block";
            mgrSec.style.display = "none";
            roleBadge.className = "role-badge role-customer";
            roleBadge.innerText = "منيو العملاء";

            navActions.innerHTML = `
                <button class="btn btn-gold btn-sm" onclick="showManagerView()">
                    🔐 لوحة الإدارة
                </button>
            `;
            renderCustomerMenu();
            renderCategoryPills();
        }
        saveState();
    }"""

new_setview = """function setView(viewName) {
        appState.currentView = viewName;
        const custSec = document.getElementById("customerSection");
        const mgrSec = document.getElementById("managerSection");
        const roleBadge = document.getElementById("roleBadge");
        const navActions = document.getElementById("topNavActions");

        applyResortSettingsUI();

        if (viewName === "manager") {
            if (custSec) custSec.style.display = "none";
            if (mgrSec) mgrSec.style.display = "block";
            if (roleBadge) {
                roleBadge.className = "role-badge role-manager";
                roleBadge.innerText = "لوحة الإدارة والمشرف";
            }

            const adminName = appState.currentLoggedInAdmin ? appState.currentLoggedInAdmin.name : "المدير العام";
            const loggedEl = document.getElementById("loggedManagerName");
            if (loggedEl) loggedEl.innerText = adminName;

            if (navActions) {
                navActions.innerHTML = `
                    <button class="btn btn-outline" style="color:white; border-color:rgba(255,255,255,0.3);" onclick="showCustomerView()">
                        👁️ منيو الزبائن
                    </button>
                    <button class="btn btn-danger btn-sm" onclick="managerLogout()">
                        🚪 خروج
                    </button>
                `;
            }
            renderTabs();
            renderActiveMeal();
        } else {
            if (custSec) custSec.style.display = "block";
            if (mgrSec) mgrSec.style.display = "none";
            if (roleBadge) {
                roleBadge.className = "role-badge role-customer";
                roleBadge.innerText = "منيو العملاء";
            }
            if (navActions) {
                navActions.innerHTML = `
                    <button class="btn btn-gold btn-sm" onclick="showManagerView()">
                        🔐 لوحة الإدارة
                    </button>
                `;
            }
            renderCustomerMenu();
            renderCategoryPills();
            renderActivitiesUI();
            renderGalleryUI();
        }
        saveState();
    }"""

html = html.replace(old_setview, new_setview)

# 2. Fix renderCategoryPills function
old_render_pills = """    function renderCategoryPills() {
        const bar = document.getElementById("categoriesFilterBar");
        bar.innerHTML = "";

        appState.categories.forEach(cat => {
            const pill = document.createElement("div");
            const isKids = cat.name.includes("أطفال");
            const isActive = appState.selectedCategory === cat.name;
            pill.className = `category-pill ${isActive ? (isKids ? 'kids-active' : 'active') : ''}`;
            
            pill.innerHTML = `<span>${cat.icon || '🍽️'}</span> <span>${cat.name}</span>`;
            pill.onclick = () => {
                appState.selectedCategory = cat.name;
                renderCategoryPills();
                filterCustomerMenu();
            };
            bar.appendChild(pill);
        });
    }"""

new_render_pills = """    function renderCategoryPills() {
        const bar = document.getElementById("customerCategoryPills") || document.getElementById("categoriesFilterBar");
        if (!bar) return;
        bar.innerHTML = "";

        appState.categories.forEach(cat => {
            const pill = document.createElement("button");
            const isKids = cat.name.includes("أطفال");
            const isActive = appState.selectedCategory === cat.name;
            pill.className = `hilton-cat-btn ${isActive ? 'active' : ''}`;
            
            pill.innerHTML = `<span>${cat.icon || '🍽️'}</span> <span>${cat.name}</span>`;
            pill.onclick = () => {
                appState.selectedCategory = cat.name;
                renderCategoryPills();
                filterCustomerMenu();
            };
            bar.appendChild(pill);
        });
    }"""

html = html.replace(old_render_pills, new_render_pills)

# 3. Fix filterCustomerMenu function
old_filter = """function filterCustomerMenu() {
        const q = (document.getElementById("customerSearchInput").value || "").toLowerCase().trim();"""

new_filter = """function filterCustomerMenu(overrideCategory = null) {
        if (overrideCategory) {
            appState.selectedCategory = overrideCategory;
            renderCategoryPills();
        }
        const searchInput = document.getElementById("menuSearchInput") || document.getElementById("customerSearchInput");
        const q = (searchInput && searchInput.value ? searchInput.value : "").toLowerCase().trim();"""

html = html.replace(old_filter, new_filter)

# 4. Enhance updateActiveMealField to re-render properly
old_update_meal = """function updateActiveMealField(field, val) {
        const meal = getActiveMeal();
        meal[field] = val;
        if (field === 'priceDate') {
            (meal.ingredients || []).forEach(ing => {
                if (!ing.date) ing.date = val;
            });
            renderIngredientsTable(meal);
        }
        updateFinancialDisplay(meal);
        saveState();
    }"""

new_update_meal = """function updateActiveMealField(field, val) {
        const meal = getActiveMeal();
        meal[field] = val;
        if (field === 'priceDate') {
            (meal.ingredients || []).forEach(ing => {
                if (!ing.date) ing.date = val;
            });
            renderIngredientsTable(meal);
        }
        if (field === 'name') {
            renderTabs();
        }
        updateFinancialDisplay(meal);
        saveState();
        renderCustomerMenu();
    }

    function saveAndApplyMealChanges() {
        saveState();
        renderCustomerMenu();
        renderTabs();
        alert("✅ تم حفظ وتحديث بيانات الوجبة في منيو العملاء بنجاح!");
    }"""

html = html.replace(old_update_meal, new_update_meal)

# 5. Add prominent "➕ إضافة وجبة جديدة" and Action Toolbar in Manager View
manager_control_target = '<div style="display: flex; gap: 8px; flex-wrap: wrap;">'
manager_new_btn = """<div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
                <button class="btn btn-primary btn-sm" style="background: linear-gradient(135deg, #2563EB, #1D4ED8); border:none; font-weight:800; font-size:13px; box-shadow: 0 2px 8px rgba(37,99,235,0.4);" onclick="createNewMeal()">
                    ➕ إضافة وجبة جديدة للمنيو
                </button>"""

if 'createNewMeal()' not in html.split('manager-control-bar')[1].split('mealsTabBar')[0]:
    html = html.replace(manager_control_target, manager_new_btn, 1)

# 6. Add Meal Action Toolbar right above the active meal workspace
target_workspace_inner = '<div class="workspace-card" id="mealWorkspace">'
workspace_toolbar_html = """<div class="workspace-card" id="mealWorkspace">
            
            <!-- Quick Meal Action Toolbar -->
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; background: #F8FAFC; border: 1px solid var(--border); border-radius: var(--radius-md); padding: 10px 14px; margin-bottom: 16px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-weight: 900; font-size: 14px; color: var(--brand-dark);">🍲 تعديل الوجبة المعيارية الحالية</span>
                    <span style="font-size: 11px; color: var(--text-muted);">(أي تعديل يُحفظ تلقائياً في المنيو)</span>
                </div>
                <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                    <button class="btn btn-primary btn-sm" onclick="saveAndApplyMealChanges()">💾 حفظ وتطبيق على المنيو</button>
                    <button class="btn btn-outline btn-sm" onclick="duplicateCurrentMeal()">📋 تكرار الوجبة</button>
                    <button class="btn btn-danger btn-sm" onclick="deleteCurrentMeal()">🗑️ حذف الوجبة</button>
                    <button class="btn btn-outline btn-sm" onclick="showCustomerView()">👁️ معاينة في المنيو</button>
                </div>
            </div>"""

if 'Quick Meal Action Toolbar' not in html:
    html = html.replace(target_workspace_inner, workspace_toolbar_html, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed setView, renderCategoryPills, filterCustomerMenu, and added meal management action toolbar!")
