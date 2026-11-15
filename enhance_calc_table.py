import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace renderIngredientsTable and updateIngredient with smooth, high-precision live updates
old_render_block = """    // --- Ingredients Table ---
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
    }"""

new_render_block = """    // --- Ingredients Table with Live Non-Destructive Calculation ---
    function renderIngredientsTable(meal) {
        const tbody = document.getElementById("ingredientsTableBody");
        if (!tbody) return;
        tbody.innerHTML = "";

        let subtotal = 0;
        (meal.ingredients || []).forEach((ing, idx) => {
            const factor = getConversionFactor(ing.rUnit, ing.pUnit);
            const lineCost = (parseFloat(ing.qty) || 0) * (parseFloat(ing.price) || 0) * factor;
            subtotal += lineCost;

            const tr = document.createElement("tr");
            tr.id = `ingRow_${idx}`;
            tr.innerHTML = `
                <td style="min-width: 220px;">
                    <input type="text" id="ingName_${idx}" value="${ing.name || ''}" style="width:100%; text-align:right; font-weight:700;" onchange="updateIngredientField(${idx}, 'name', this.value)">
                </td>
                <td style="min-width: 140px;">
                    <input type="date" id="ingDate_${idx}" value="${ing.date || ''}" style="width:100%; font-size:12px;" onchange="updateIngredientField(${idx}, 'date', this.value)">
                </td>
                <td style="min-width: 90px;">
                    <input type="number" step="any" min="0" id="ingQty_${idx}" value="${ing.qty || 0}" style="width:100%; text-align:center; font-weight:800;" oninput="onLiveIngredientInput(${idx})">
                </td>
                <td style="min-width: 130px;">
                    <select id="ingRUnit_${idx}" onchange="onIngredientUnitChange(${idx})" style="width:100%;">
                        <option value="جرام (Gram)" ${ing.rUnit==='جرام (Gram)'?'selected':''}>جرام (Gram)</option>
                        <option value="كيلوجرام (Kg)" ${ing.rUnit==='كيلوجرام (Kg)'?'selected':''}>كيلوجرام (Kg)</option>
                        <option value="مليلتر (ml)" ${ing.rUnit==='مليلتر (ml)'?'selected':''}>مليلتر (ml)</option>
                        <option value="لتر (L)" ${ing.rUnit==='لتر (L)'?'selected':''}>لتر (L)</option>
                        <option value="قطعة / حصة" ${ing.rUnit==='قطعة / حصة'?'selected':''}>قطعة / حصة</option>
                    </select>
                </td>
                <td style="min-width: 130px;">
                    <select id="ingPUnit_${idx}" onchange="onIngredientUnitChange(${idx})" style="width:100%;">
                        <option value="كيلوجرام (Kg)" ${ing.pUnit==='كيلوجرام (Kg)'?'selected':''}>كيلوجرام (Kg)</option>
                        <option value="لتر (L)" ${ing.pUnit==='لتر (L)'?'selected':''}>لتر (L)</option>
                        <option value="قطعة / حصة" ${ing.pUnit==='قطعة / حصة'?'selected':''}>قطعة / حصة</option>
                    </select>
                </td>
                <td style="min-width: 95px;">
                    <input type="number" step="any" min="0" id="ingPrice_${idx}" value="${ing.price || 0}" style="width:100%; text-align:center; font-weight:800;" oninput="onLiveIngredientInput(${idx})">
                </td>
                <td id="ingFactor_${idx}" style="color:#004B87; font-weight:800; font-family:monospace; text-align:center;">${factor}</td>
                <td id="ingCost_${idx}" style="font-weight:900; color:var(--brand-dark); text-align:center; min-width:110px;">${lineCost.toFixed(2)} ج.م</td>
                <td style="text-align:center; width:50px;">
                    <button class="btn btn-danger btn-sm" style="padding: 4px 8px; font-size: 11px;" onclick="removeIngredient(${idx})" title="حذف هذا المكون">✕</button>
                </td>
            `;
            tbody.appendChild(tr);
        });

        // Add summary row at the bottom of the table
        const tfoot = document.getElementById("ingredientsTableFoot");
        if (tfoot) {
            const f = calculateMealFinancials(meal);
            tfoot.innerHTML = `
                <tr style="background: #F1F5F9; font-weight: 800;">
                    <td colspan="6" style="text-align: left; padding: 10px 14px; color: var(--brand-dark);">
                        إجمالي تكلفة الخامات المباشرة (Subtotal):
                    </td>
                    <td colspan="3" style="text-align: center; color: var(--brand-primary); font-size: 16px; font-weight: 900;" id="tableSubtotalDisplay">
                        ${f.subtotal.toFixed(2)} ج.م
                    </td>
                </tr>
            `;
        }
    }

    function onLiveIngredientInput(idx) {
        const meal = getActiveMeal();
        if (!meal || !meal.ingredients || !meal.ingredients[idx]) return;

        const qtyEl = document.getElementById(`ingQty_${idx}`);
        const priceEl = document.getElementById(`ingPrice_${idx}`);
        const costEl = document.getElementById(`ingCost_${idx}`);

        const qty = parseFloat(qtyEl ? qtyEl.value : 0) || 0;
        const price = parseFloat(priceEl ? priceEl.value : 0) || 0;

        meal.ingredients[idx].qty = qty;
        meal.ingredients[idx].price = price;

        const factor = getConversionFactor(meal.ingredients[idx].rUnit, meal.ingredients[idx].pUnit);
        const lineCost = qty * price * factor;

        if (costEl) costEl.innerText = lineCost.toFixed(2) + " ج.م";

        updateFinancialDisplay(meal);
        const subDisplay = document.getElementById("tableSubtotalDisplay");
        if (subDisplay) {
            const f = calculateMealFinancials(meal);
            subDisplay.innerText = f.subtotal.toFixed(2) + " ج.م";
        }
        saveState();
        renderCustomerMenu();
    }

    function onIngredientUnitChange(idx) {
        const meal = getActiveMeal();
        if (!meal || !meal.ingredients || !meal.ingredients[idx]) return;

        const rUnitEl = document.getElementById(`ingRUnit_${idx}`);
        const pUnitEl = document.getElementById(`ingPUnit_${idx}`);
        const factorEl = document.getElementById(`ingFactor_${idx}`);
        const costEl = document.getElementById(`ingCost_${idx}`);

        if (rUnitEl) meal.ingredients[idx].rUnit = rUnitEl.value;
        if (pUnitEl) meal.ingredients[idx].pUnit = pUnitEl.value;

        const factor = getConversionFactor(meal.ingredients[idx].rUnit, meal.ingredients[idx].pUnit);
        if (factorEl) factorEl.innerText = factor;

        const qty = parseFloat(meal.ingredients[idx].qty) || 0;
        const price = parseFloat(meal.ingredients[idx].price) || 0;
        const lineCost = qty * price * factor;

        if (costEl) costEl.innerText = lineCost.toFixed(2) + " ج.م";

        updateFinancialDisplay(meal);
        const subDisplay = document.getElementById("tableSubtotalDisplay");
        if (subDisplay) {
            const f = calculateMealFinancials(meal);
            subDisplay.innerText = f.subtotal.toFixed(2) + " ج.م";
        }
        saveState();
        renderCustomerMenu();
    }

    function updateIngredientField(idx, field, val) {
        const meal = getActiveMeal();
        if (!meal || !meal.ingredients || !meal.ingredients[idx]) return;
        meal.ingredients[idx][field] = val;
        saveState();
    }"""

html = html.replace(old_render_block, new_render_block)

# Add tfoot to ingredientsTable in HTML
old_table = """                    <table class="manager-data-table" id="ingredientsTable">
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
                    </table>"""

new_table = """                    <table class="manager-data-table" id="ingredientsTable">
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
                        <tfoot id="ingredientsTableFoot">
                            <!-- Populated with live subtotal -->
                        </tfoot>
                    </table>"""

html = html.replace(old_table, new_table)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated renderIngredientsTable with live seamless input and calculation!")
