with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re

scripts = re.findall(r'<script[\s\S]*?</script>', text)
print(f"Scripts count: {len(scripts)}")
js_code = scripts[1].replace("<script>", "").replace("</script>", "")

print("JS Code size in bytes:", len(js_code))

# Check critical functions
essential_functions = [
    "loadState", "saveState", "calculateMealFinancials", "applyResortSettingsUI",
    "setView", "showCustomerView", "showManagerView", "executeLogin", "managerLogout",
    "renderCategoryPills", "filterCustomerMenu", "renderCustomerMenu", "openDishDetailModal",
    "renderActivitiesUI", "renderGalleryUI", "createNewMeal", "duplicateCurrentMeal",
    "deleteCurrentMeal", "renderTabs", "switchTab", "renderActiveMeal", "updateActiveMealField",
    "saveAndApplyMealChanges", "renderIngredientsTable", "updateIngredient", "addNewIngredientRow",
    "removeIngredient", "updateFinancialDisplay", "renderMasterMenuDashboard",
    "openCategoriesManagerModal", "saveCategoryFromForm", "deleteCategory",
    "openResortSettingsModal", "saveResortSettings", "openActivitiesManagerModal",
    "saveActivityFromForm", "openGalleryManagerModal", "addPhotoToGallery",
    "openHeroImageModal", "saveHeroImage", "openThemeModifierModal", "saveThemeSettings",
    "openAdminManagementModal", "saveAdminFromForm", "openPantryModal",
    "insertPantryItemToCurrentMeal", "exportCurrentMealToExcel", "exportAllMealsToExcel"
]

missing_funcs = []
for fn in essential_functions:
    if f"function {fn}" not in js_code:
        missing_funcs.append(fn)

if missing_funcs:
    print("❌ Missing functions:", missing_funcs)
else:
    print("✅ All essential functions (total 48) are present and defined cleanly!")
