import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern_setview = r'function setView\(viewName\) \{[\s\S]*?saveState\(\);\s*\}'

new_setview_code = """function setView(viewName) {
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
            renderCategorySelectOptions();
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

html, n = re.subn(pattern_setview, new_setview_code, html, count=1)
print(f"Replaced setView count: {n}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
