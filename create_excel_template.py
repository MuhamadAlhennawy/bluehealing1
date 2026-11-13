import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime

def build_recipe_sheet(filename="Standard_Recipe_Cost_Card.xlsx"):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Blue Healing Recipe Card"
    ws.views.sheetView[0].showGridLines = True
    
    # Fonts
    brand_font = Font(name="Arial", size=11, bold=True, color="93C5FD")
    title_font = Font(name="Arial", size=16, bold=True, color="FFFFFF")
    header_font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    bold_font = Font(name="Arial", size=10, bold=True, color="111827")
    normal_font = Font(name="Arial", size=10, color="1F2937")
    kpi_val_font = Font(name="Arial", size=11, bold=True, color="1E3A8A")
    price_val_font = Font(name="Arial", size=13, bold=True, color="065F46")
    
    # Fills (Blue Healing Palette: Deep Navy & Royal & Cyan accents)
    navy_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid") # Dark Navy
    royal_fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid") # Royal Blue
    header_fill = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
    soft_blue_fill = PatternFill(start_color="EFF6FF", end_color="EFF6FF", fill_type="solid")
    soft_green_fill = PatternFill(start_color="ECFDF5", end_color="ECFDF5", fill_type="solid")
    summary_fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    warning_fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
    
    # Borders
    thin_line = Side(border_style="thin", color="CBD5E1")
    double_bottom = Side(border_style="double", color="0F172A")
    
    border_all = Border(left=thin_line, right=thin_line, top=thin_line, bottom=thin_line)
    border_total = Border(left=thin_line, right=thin_line, top=thin_line, bottom=double_bottom)
    
    # Row 1: Brand Banner "BLUE HEALING"
    ws.merge_cells("A1:H1")
    ws["A1"] = "✦ BLUE HEALING ✦ | CULINARY OPERATIONS & MENU ENGINEERING"
    ws["A1"].font = brand_font
    ws["A1"].fill = navy_fill
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 25
    
    # Row 2: Main Title
    ws.merge_cells("A2:H2")
    ws["A2"] = "كارت تكلفة الوصفة المعيارية - STANDARD RECIPE COST CARD"
    ws["A2"].font = title_font
    ws["A2"].fill = royal_fill
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 35

    current_date = datetime.now().strftime("%Y-%m-%d")

    # Meal Info / Metadata Block
    info_labels = [
        ("A4", "B4", "1. Item No. (رقم الصنف):", "#101"),
        ("A5", "B5", "Meal Name (اسم الوجبة):", "وجبة دجاج مشوي مع أرز بسمتي"),
        ("A6", "B6", "2. No. of Portions (عدد الوجبات):", 4),
        ("A7", "B7", "3. Size of Portion (حجم الحصة):", "350 gm"),
        ("A8", "B8", "تاريخ تسعير الخامات (Price Date):", current_date),
        ("A9", "B9", "4. Cost / Portion (تكلفة الوجبة الواحدة):", "=H21/B6"),
        ("A10", "B10", "5. Food Cost % (نسبة تكلفة الطعام):", 0.30),
        ("A11", "B11", "Pricing Multiplier (مُعامل الضرب 3.1 - 3.6):", 3.33),
        ("A12", "B12", "6. Selling Price / Portion (سعر البيع المقترح):", "=B9*B11"),
        ("A13", "B13", "Team / فريق العمل:", "Blue Healing"),
    ]
    
    for lbl_c, val_c, label, val in info_labels:
        ws[lbl_c] = label
        ws[lbl_c].font = bold_font
        ws[lbl_c].fill = soft_blue_fill
        ws[lbl_c].alignment = Alignment(horizontal="left", vertical="center")
        ws[lbl_c].border = border_all
        
        ws[val_c] = val
        ws[val_c].font = kpi_val_font if lbl_c in ["A9", "A12"] else normal_font
        ws[val_c].border = border_all
        ws[val_c].alignment = Alignment(horizontal="center", vertical="center")
        
        if lbl_c == "A10":
            ws[val_c].number_format = "0.0%"
        elif lbl_c in ["A9", "A12"]:
            ws[val_c].number_format = '#,##0.00 "L.E"'
            if lbl_c == "A12":
                ws[val_c].font = price_val_font
                ws[val_c].fill = soft_green_fill
        elif lbl_c == "A13":
            ws[val_c].font = Font(name="Arial", size=10, bold=True, color="1E3A8A")
            ws[val_c].fill = soft_blue_fill
            
    for r in range(4, 14):
        ws.row_dimensions[r].height = 23
    
    # Table Header (Row 15 & 16)
    # Merged headers
    ws.merge_cells("A15:A16")
    ws["A15"] = "Ingredients\nالمكونات"
    
    ws.merge_cells("B15:B16")
    ws["B15"] = "Price Date\nتاريخ السعر"
    
    ws.merge_cells("C15:D15")
    ws["C15"] = "Recipe\nمقادير الوصفة"
    ws["C16"] = "Qty (الكمية)"
    ws["D16"] = "Unit (الوحدة)"
    
    ws.merge_cells("E15:F15")
    ws["E15"] = "Price / Unit\nسعر الشراء"
    ws["E16"] = "Unit (الوحدة)"
    ws["F16"] = "Price L.E (السعر)"
    
    ws.merge_cells("G15:G16")
    ws["G15"] = "Conversion\nمعامل التحويل"
    
    ws.merge_cells("H15:H16")
    ws["H15"] = "Cost L.E\nالتكلفة الإجمالية"
    
    header_cells = ["A15", "B15", "C15", "D15", "E15", "F15", "G15", "H15", "C16", "D16", "E16", "F16"]
    for c_ref in header_cells:
        cell = ws[c_ref]
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border_all
    
    ws.row_dimensions[15].height = 24
    ws.row_dimensions[16].height = 22

    # Sample Ingredients Data (Rows 17 to 20)
    sample_data = [
        ("صدور دجاج مخلي (Chicken Breast)", "2026-11-12", 800, "Gram", "Kg", 220.0, 1000),
        ("أرز بسمتي هندي (Basmati Rice)", "2026-11-10", 400, "Gram", "Kg", 85.0, 1000),
        ("زيت طهي / سمن (Cooking Oil)", "2026-11-08", 60, "ml", "L", 70.0, 1000),
        ("خضروات مشكلة (Vegetables)", "2026-11-13", 300, "Gram", "Kg", 25.0, 1000),
    ]
    
    start_row = 17
    for i, item in enumerate(sample_data):
        r = start_row + i
        ws[f"A{r}"] = item[0]
        ws[f"B{r}"] = item[1]
        ws[f"C{r}"] = item[2]
        ws[f"D{r}"] = item[3]
        ws[f"E{r}"] = item[4]
        ws[f"F{r}"] = item[5]
        ws[f"G{r}"] = item[6]
        # Formula: (Qty / Conversion) * Price
        ws[f"H{r}"] = f"=(C{r}/G{r})*F{r}"
        
        ws[f"A{r}"].alignment = Alignment(horizontal="left", vertical="center")
        ws[f"B{r}"].alignment = Alignment(horizontal="center", vertical="center")
        ws[f"C{r}"].alignment = Alignment(horizontal="center", vertical="center")
        ws[f"D{r}"].alignment = Alignment(horizontal="center", vertical="center")
        ws[f"E{r}"].alignment = Alignment(horizontal="center", vertical="center")
        ws[f"F{r}"].alignment = Alignment(horizontal="right", vertical="center")
        ws[f"G{r}"].alignment = Alignment(horizontal="center", vertical="center")
        ws[f"H{r}"].alignment = Alignment(horizontal="right", vertical="center")
        
        ws[f"F{r}"].number_format = '#,##0.00 "L.E"'
        ws[f"H{r}"].number_format = '#,##0.00 "L.E"'
        
        for col_char in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            ws[f"{col_char}{r}"].border = border_all
            ws[f"{col_char}{r}"].font = normal_font
        ws.row_dimensions[r].height = 22

    # Bottom Summary Rows (Whiteboard matching):
    season_row = 21
    subtotal_row = 22
    waste_row = 23
    total_row = 24
    
    # Seasoning
    ws.merge_cells(f"A{season_row}:G{season_row}")
    ws[f"A{season_row}"] = "Seasoning (التوابل والبهارات)"
    ws[f"H{season_row}"] = 10.00
    
    # Sub total
    ws.merge_cells(f"A{subtotal_row}:G{subtotal_row}")
    ws[f"A{subtotal_row}"] = "Sub-total (المجموع الفرعي = المكونات + البهارات)"
    ws[f"H{subtotal_row}"] = f"=SUM(H{start_row}:H{start_row+len(sample_data)-1})+H{season_row}"
    
    # 5% Waste
    ws.merge_cells(f"A{waste_row}:G{waste_row}")
    ws[f"A{waste_row}"] = "5% Waste (نسبة الهالك / الفاقد 5%)"
    ws[f"H{waste_row}"] = f"=H{subtotal_row}*0.05"
    
    # Total Cost
    ws.merge_cells(f"A{total_row}:G{total_row}")
    ws[f"A{total_row}"] = "Total Cost (التكلفة الإجمالية للوصفة)"
    ws[f"H{total_row}"] = f"=H{subtotal_row}+H{waste_row}"
    
    # Update cost per portion formula
    ws["B9"] = f"=H{total_row}/B6"

    summary_rows = [
        (season_row, bold_font, summary_fill),
        (subtotal_row, bold_font, warning_fill),
        (waste_row, bold_font, summary_fill),
        (total_row, Font(name="Arial", size=11, bold=True, color="1E3A8A"), soft_green_fill)
    ]
    
    for r, f_style, fill_style in summary_rows:
        ws[f"A{r}"].font = f_style
        ws[f"A{r}"].fill = fill_style
        ws[f"A{r}"].alignment = Alignment(horizontal="right", vertical="center")
        ws[f"A{r}"].border = border_all
        
        ws[f"H{r}"].font = f_style
        ws[f"H{r}"].fill = fill_style
        ws[f"H{r}"].alignment = Alignment(horizontal="right", vertical="center")
        ws[f"H{r}"].border = border_total if r == total_row else border_all
        ws[f"H{r}"].number_format = '#,##0.00 "L.E"'
        ws.row_dimensions[r].height = 24
        
        for c in ["B", "C", "D", "E", "F", "G"]:
            ws[f"{c}{r}"].border = border_all

    # Explanatory Notes & Footer
    notes = [
        ("A26", "ملاحظات إرشادية من فريق Blue Healing:"),
        ("A27", "• Cost / Portion: إجمالي تكلفة الوصفة مقسومة على عدد الحصص."),
        ("A28", "• Selling Price: يتم تحديده عبر معامل الضرب (3.1 - 3.6) لتغطية مصاريف التشغيل وصافي الربح."),
        ("A29", "• Price Date: تم تدوين تاريخ الأسعار لمتابعة التضخم وتغيرات أسعار الموردين دورياً."),
    ]
    for cell_ref, note_text in notes:
        ws[cell_ref] = note_text
        ws[cell_ref].font = Font(name="Arial", size=9, italic=True, color="4B5563")

    # Column Widths
    ws.column_dimensions["A"].width = 38
    ws.column_dimensions["B"].width = 15
    ws.column_dimensions["C"].width = 15
    ws.column_dimensions["D"].width = 14
    ws.column_dimensions["E"].width = 14
    ws.column_dimensions["F"].width = 17
    ws.column_dimensions["G"].width = 16
    ws.column_dimensions["H"].width = 22
    
    wb.save(filename)
    print(f"Blue Healing Excel file created: {filename}")

if __name__ == "__main__":
    build_recipe_sheet()
