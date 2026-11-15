import sys
import os
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QLineEdit, QDoubleSpinBox, QSpinBox,
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,
    QComboBox, QMessageBox, QFileDialog, QGroupBox, QFrame, QDateEdit
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont, QColor
import openpyxl
from openpyxl.styles import Font as XlFont, Alignment as XlAlign, PatternFill, Border, Side

class BlueHealingRecipeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blue Healing • نظام حساب وتكلفة الوجبات وتسعير المنيو المعياري")
        self.resize(1180, 840)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        
        self.init_ui()
        self.load_sample_data()
        self.calculate_all()
        
    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setSpacing(14)
        main_layout.setContentsMargins(18, 16, 18, 16)
        
        # 1. Creative Header Banner (Blue Healing Theme)
        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #0F172A, stop:0.5 #1E3A8A, stop:1 #2563EB);
                border-radius: 12px;
                padding: 14px;
            }
        """)
        header_layout = QHBoxLayout(header_frame)
        
        title_box = QVBoxLayout()
        brand_badge = QLabel("✦ BLUE HEALING ✦  |  CULINARY INTELLIGENCE & MENU ENGINEERING")
        brand_badge.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        brand_badge.setStyleSheet("color: #38BDF8; letter-spacing: 1px;")
        
        main_title = QLabel("كارت تكلفة الوصفة المعيارية (Standard Recipe Cost Card)")
        main_title.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        main_title.setStyleSheet("color: #FFFFFF;")
        
        sub_desc = QLabel("إدارة مقادير الطهي، تواريخ أسعار الموردين، حساب الهالك (5%)، ومضاعف التسعير (3.1 - 3.6)")
        sub_desc.setFont(QFont("Segoe UI", 10))
        sub_desc.setStyleSheet("color: #BFDBFE;")
        
        title_box.addWidget(brand_badge)
        title_box.addWidget(main_title)
        title_box.addWidget(sub_desc)
        header_layout.addLayout(title_box)
        
        header_layout.addStretch()
        
        # Quick Top KPI Card
        self.top_kpi_frame = QFrame()
        self.top_kpi_frame.setStyleSheet("""
            QFrame {
                background: rgba(255, 255, 255, 0.12);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                padding: 8px 16px;
            }
        """)
        top_kpi_layout = QVBoxLayout(self.top_kpi_frame)
        top_lbl = QLabel("سعر البيع المقترح للحصة")
        top_lbl.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        top_lbl.setStyleSheet("color: #93C5FD;")
        top_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.top_val_lbl = QLabel("0.00 ج.م")
        self.top_val_lbl.setFont(QFont("Segoe UI", 17, QFont.Weight.Bold))
        self.top_val_lbl.setStyleSheet("color: #34D399;")
        self.top_val_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        top_kpi_layout.addWidget(top_lbl)
        top_kpi_layout.addWidget(self.top_val_lbl)
        header_layout.addWidget(self.top_kpi_frame)
        
        main_layout.addWidget(header_frame)
        
        # 2. Meal Information & Pricing Parameters
        info_group = QGroupBox("بيانات الوجبة وإعدادات التسعير (Meal Information & Pricing)")
        info_group.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        info_group.setStyleSheet("""
            QGroupBox {
                border: 1.5px solid #CBD5E1;
                border-radius: 10px;
                margin-top: 8px;
                padding-top: 12px;
                background-color: #F8FAFC;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 14px;
                padding: 0 6px;
                color: #1E3A8A;
            }
        """)
        info_layout = QGridLayout(info_group)
        info_layout.setHorizontalSpacing(14)
        info_layout.setVerticalSpacing(8)
        
        self.item_no_input = QLineEdit("#101")
        self.meal_name_input = QLineEdit("وجبة دجاج مشوي مع أرز بسمتي")
        
        self.price_date_edit = QDateEdit()
        self.price_date_edit.setCalendarPopup(True)
        self.price_date_edit.setDate(QDate.currentDate())
        self.price_date_edit.dateChanged.connect(self.sync_dates)
        
        self.portions_spin = QSpinBox()
        self.portions_spin.setRange(1, 1000)
        self.portions_spin.setValue(4)
        self.portions_spin.valueChanged.connect(self.calculate_all)
        
        self.portion_size_input = QLineEdit("350 gm")
        
        self.seasoning_spin = QDoubleSpinBox()
        self.seasoning_spin.setRange(0, 10000)
        self.seasoning_spin.setValue(10.0)
        self.seasoning_spin.setSuffix(" ج.م")
        self.seasoning_spin.valueChanged.connect(self.calculate_all)
        
        self.waste_spin = QDoubleSpinBox()
        self.waste_spin.setRange(0, 50)
        self.waste_spin.setValue(5.0)
        self.waste_spin.setSuffix(" %")
        self.waste_spin.valueChanged.connect(self.calculate_all)
        
        self.multiplier_spin = QDoubleSpinBox()
        self.multiplier_spin.setRange(1.0, 10.0)
        self.multiplier_spin.setSingleStep(0.05)
        self.multiplier_spin.setValue(3.33)
        self.multiplier_spin.valueChanged.connect(self.on_multiplier_changed)
        
        self.food_cost_pct_spin = QDoubleSpinBox()
        self.food_cost_pct_spin.setRange(5.0, 90.0)
        self.food_cost_pct_spin.setValue(30.0)
        self.food_cost_pct_spin.setSuffix(" %")
        self.food_cost_pct_spin.valueChanged.connect(self.on_food_cost_changed)
        
        team_lbl = QLabel("Blue Healing")
        team_lbl.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        team_lbl.setStyleSheet("color: #2563EB;")
        
        # Grid Placement
        info_layout.addWidget(QLabel("رقم الصنف (Item No):"), 0, 0)
        info_layout.addWidget(self.item_no_input, 0, 1)
        info_layout.addWidget(QLabel("اسم الوجبة (Meal Name):"), 0, 2)
        info_layout.addWidget(self.meal_name_input, 0, 3)
        info_layout.addWidget(QLabel("تاريخ التسعير (Price Date):"), 0, 4)
        info_layout.addWidget(self.price_date_edit, 0, 5)
        
        info_layout.addWidget(QLabel("عدد الحصص (Portions):"), 1, 0)
        info_layout.addWidget(self.portions_spin, 1, 1)
        info_layout.addWidget(QLabel("حجم الحصة (Portion Size):"), 1, 2)
        info_layout.addWidget(self.portion_size_input, 1, 3)
        info_layout.addWidget(QLabel("الفريق المعتمد (Team):"), 1, 4)
        info_layout.addWidget(team_lbl, 1, 5)
        
        info_layout.addWidget(QLabel("تكلفة التوابل (Seasoning):"), 2, 0)
        info_layout.addWidget(self.seasoning_spin, 2, 1)
        info_layout.addWidget(QLabel("نسبة الهالك (5% Waste):"), 2, 2)
        info_layout.addWidget(self.waste_spin, 2, 3)
        info_layout.addWidget(QLabel("معامل التسعير (3.1 - 3.6):"), 2, 4)
        info_layout.addWidget(self.multiplier_spin, 2, 5)
        
        main_layout.addWidget(info_group)
        
        # 3. Ingredients Table
        table_group = QGroupBox("جدول المكونات وتواريخ شراء الخامات (Ingredients & Recipe Table)")
        table_group.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        table_group.setStyleSheet("""
            QGroupBox {
                border: 1.5px solid #CBD5E1;
                border-radius: 10px;
                margin-top: 6px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 14px;
                padding: 0 6px;
                color: #1E3A8A;
            }
        """)
        table_layout = QVBoxLayout(table_group)
        
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "اسم المكون\nIngredients",
            "تاريخ السعر\nPrice Date",
            "كمية الوصفة\nRecipe Qty",
            "وحدة الوصفة\nRecipe Unit",
            "وحدة الشراء\nPurchase Unit",
            "سعر الشراء (ج.م)\nPrice / Unit",
            "التكلفة بالجنيه\nCost L.E"
        ])
        
        self.table.setStyleSheet("""
            QHeaderView::section {
                background-color: #1E293B;
                color: white;
                font-weight: bold;
                padding: 6px;
                border: 1px solid #334155;
            }
            QTableWidget {
                gridline-color: #E2E8F0;
                font-size: 13px;
                selection-background-color: #EFF6FF;
            }
        """)
        
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)
        
        table_layout.addWidget(self.table)
        
        # Action Buttons
        btn_bar = QHBoxLayout()
        add_btn = QPushButton("➕ إضافة خامة جديدة")
        add_btn.setStyleSheet("background-color: #2563EB; color: white; padding: 7px 14px; font-weight: bold; border-radius: 6px;")
        add_btn.clicked.connect(self.add_empty_row)
        
        del_btn = QPushButton("➖ حذف الخامة المحددة")
        del_btn.setStyleSheet("background-color: #EF4444; color: white; padding: 7px 14px; font-weight: bold; border-radius: 6px;")
        del_btn.clicked.connect(self.delete_selected_row)
        
        sample_btn = QPushButton("🔄 استعادة وجبة تجريبية")
        sample_btn.setStyleSheet("background-color: #64748B; color: white; padding: 7px 14px; font-weight: bold; border-radius: 6px;")
        sample_btn.clicked.connect(self.load_sample_data)
        
        btn_bar.addWidget(add_btn)
        btn_bar.addWidget(del_btn)
        btn_bar.addWidget(sample_btn)
        btn_bar.addStretch()
        table_layout.addLayout(btn_bar)
        
        main_layout.addWidget(table_group)
        
        # 4. Results & Profit Deck
        results_layout = QHBoxLayout()
        
        self.subtotal_box = self.create_kpi_card("المجموع الفرعي (Sub-total)", "0.00 ج.م", "#F8FAFC", "#1E293B")
        self.waste_cost_box = self.create_kpi_card("الهالك 5% (Waste)", "0.00 ج.م", "#FEF3C7", "#B45309")
        self.total_cost_box = self.create_kpi_card("إجمالي التكلفة (Total)", "0.00 ج.م", "#DBEAFE", "#1E40AF")
        self.portion_cost_box = self.create_kpi_card("4. تكلفة الحصة (Cost/Portion)", "0.00 ج.م", "#F3E8FF", "#6B21A8")
        self.selling_price_box = self.create_kpi_card("6. سعر البيع المقترح (Selling Price)", "0.00 ج.م", "#ECFDF5", "#065F46", highlight=True)
        self.gross_profit_box = self.create_kpi_card("هامش الربح للحصة", "0.00 ج.م", "#F0FDF4", "#059669")
        
        results_layout.addWidget(self.subtotal_box)
        results_layout.addWidget(self.waste_cost_box)
        results_layout.addWidget(self.total_cost_box)
        results_layout.addWidget(self.portion_cost_box)
        results_layout.addWidget(self.selling_price_box)
        results_layout.addWidget(self.gross_profit_box)
        main_layout.addLayout(results_layout)
        
        # 5. Export Action
        export_btn = QPushButton("📊 تصدير شيت إكسيل فاخر معتمد باسم Blue Healing (.xlsx)")
        export_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        export_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #059669, stop:1 #10B981);
                color: white;
                padding: 12px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background: #047857;
            }
        """)
        export_btn.clicked.connect(self.export_to_excel)
        main_layout.addWidget(export_btn)
        
    def create_kpi_card(self, title, val, bg_color, text_color, highlight=False):
        frame = QFrame()
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {bg_color};
                border: {'2px solid #059669' if highlight else '1px solid #CBD5E1'};
                border-radius: 8px;
                padding: 8px;
            }}
        """)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(6, 6, 6, 6)
        
        lbl_title = QLabel(title)
        lbl_title.setFont(QFont("Segoe UI", 8, QFont.Weight.Bold))
        lbl_title.setStyleSheet("color: #64748B;")
        lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        lbl_val = QLabel(val)
        lbl_val.setFont(QFont("Segoe UI", 13 if highlight else 12, QFont.Weight.Bold))
        lbl_val.setStyleSheet(f"color: {text_color};")
        lbl_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(lbl_title)
        layout.addWidget(lbl_val)
        frame.value_label = lbl_val
        return frame

    def sync_dates(self):
        master_date = self.price_date_edit.date()
        for r in range(self.table.rowCount()):
            date_widget = self.table.cellWidget(r, 1)
            if isinstance(date_widget, QDateEdit):
                # only sync if needed
                pass

    def on_multiplier_changed(self, val):
        self.food_cost_pct_spin.blockSignals(True)
        if val > 0:
            self.food_cost_pct_spin.setValue((1.0 / val) * 100)
        self.food_cost_pct_spin.blockSignals(False)
        self.calculate_all()

    def on_food_cost_changed(self, val):
        self.multiplier_spin.blockSignals(True)
        if val > 0:
            self.multiplier_spin.setValue(100.0 / val)
        self.multiplier_spin.blockSignals(False)
        self.calculate_all()

    def load_sample_data(self):
        self.table.setRowCount(0)
        sample = [
            ("صدور دجاج مخلي (Chicken Breast)", "2026-11-12", 800.0, "جرام (Gram)", "كيلوجرام (Kg)", 220.0),
            ("أرز بسمتي هندي (Basmati Rice)", "2026-11-10", 400.0, "جرام (Gram)", "كيلوجرام (Kg)", 85.0),
            ("زيت ذرة / سمن (Cooking Oil)", "2026-11-08", 60.0, "مليلتر (ml)", "لتر (L)", 70.0),
            ("خضار مشكل طازج (Vegetables)", "2026-11-13", 300.0, "جرام (Gram)", "كيلوجرام (Kg)", 25.0),
            ("علب وتغليف تقديم (Packaging)", "2026-11-01", 4.0, "قطعة / حصة", "قطعة / حصة", 5.0),
        ]
        for item in sample:
            self.add_row(*item)
            
    def add_empty_row(self):
        today_str = self.price_date_edit.date().toString("yyyy-MM-dd")
        self.add_row("خامة جديدة", today_str, 100.0, "جرام (Gram)", "كيلوجرام (Kg)", 50.0)

    def add_row(self, name, date_str, qty, r_unit, p_unit, price):
        row = self.table.rowCount()
        self.table.insertRow(row)
        
        name_item = QTableWidgetItem(name)
        
        # Price Date
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        qdate = QDate.fromString(date_str, "yyyy-MM-dd")
        date_edit.setDate(qdate if qdate.isValid() else QDate.currentDate())
        
        qty_spin = QDoubleSpinBox()
        qty_spin.setRange(0.01, 100000)
        qty_spin.setValue(qty)
        qty_spin.valueChanged.connect(self.calculate_all)
        
        r_unit_cb = QComboBox()
        r_unit_cb.addItems(["جرام (Gram)", "كيلوجرام (Kg)", "مليلتر (ml)", "لتر (L)", "قطعة / حصة"])
        r_unit_cb.setCurrentText(r_unit)
        r_unit_cb.currentTextChanged.connect(self.calculate_all)
        
        p_unit_cb = QComboBox()
        p_unit_cb.addItems(["كيلوجرام (Kg)", "لتر (L)", "قطعة / حصة", "جرام (Gram)", "مليلتر (ml)"])
        p_unit_cb.setCurrentText(p_unit)
        p_unit_cb.currentTextChanged.connect(self.calculate_all)
        
        price_spin = QDoubleSpinBox()
        price_spin.setRange(0.0, 100000)
        price_spin.setValue(price)
        price_spin.valueChanged.connect(self.calculate_all)
        
        cost_item = QTableWidgetItem("0.00 ج.م")
        cost_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        cost_item.setFlags(cost_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        cost_item.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        cost_item.setForeground(QColor("#166534"))
        
        self.table.setItem(row, 0, name_item)
        self.table.setCellWidget(row, 1, date_edit)
        self.table.setCellWidget(row, 2, qty_spin)
        self.table.setCellWidget(row, 3, r_unit_cb)
        self.table.setCellWidget(row, 4, p_unit_cb)
        self.table.setCellWidget(row, 5, price_spin)
        self.table.setItem(row, 6, cost_item)

    def delete_selected_row(self):
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)
            self.calculate_all()
        else:
            QMessageBox.information(self, "تنبيه", "يرجى تحديد الخامة المراد حذفها من الجدول أولاً.")

    def compute_ingredient_cost(self, qty, r_unit, p_unit, price):
        conversion = 1.0
        if "جرام" in r_unit and "كيلوجرام" in p_unit:
            conversion = 1000.0
        elif "مليلتر" in r_unit and "لتر" in p_unit:
            conversion = 1000.0
        elif "كيلوجرام" in r_unit and "جرام" in p_unit:
            conversion = 0.001
        elif "لتر" in r_unit and "مليلتر" in p_unit:
            conversion = 0.001
            
        cost = (qty / conversion) * price
        return cost, conversion

    def calculate_all(self):
        ingredients_total = 0.0
        
        for row in range(self.table.rowCount()):
            qty_widget = self.table.cellWidget(row, 2)
            r_unit_widget = self.table.cellWidget(row, 3)
            p_unit_widget = self.table.cellWidget(row, 4)
            price_widget = self.table.cellWidget(row, 5)
            cost_item = self.table.item(row, 6)
            
            if qty_widget and price_widget and cost_item:
                qty = qty_widget.value()
                r_unit = r_unit_widget.currentText()
                p_unit = p_unit_widget.currentText()
                price = price_widget.value()
                
                cost, _ = self.compute_ingredient_cost(qty, r_unit, p_unit, price)
                ingredients_total += cost
                cost_item.setText(f"{cost:,.2f} ج.م")
                
        seasoning = self.seasoning_spin.value()
        subtotal = ingredients_total + seasoning
        waste_pct = self.waste_spin.value() / 100.0
        waste_cost = subtotal * waste_pct
        total_cost = subtotal + waste_cost
        
        portions = max(1, self.portions_spin.value())
        cost_per_portion = total_cost / portions
        
        multiplier = self.multiplier_spin.value()
        selling_price = cost_per_portion * multiplier
        gross_profit = selling_price - cost_per_portion
        
        # Update KPI boxes
        self.subtotal_box.value_label.setText(f"{subtotal:,.2f} ج.م")
        self.waste_cost_box.value_label.setText(f"{waste_cost:,.2f} ج.م")
        self.total_cost_box.value_label.setText(f"{total_cost:,.2f} ج.م")
        self.portion_cost_box.value_label.setText(f"{cost_per_portion:,.2f} ج.م")
        self.selling_price_box.value_label.setText(f"{selling_price:,.2f} ج.م")
        self.gross_profit_box.value_label.setText(f"{gross_profit:,.2f} ج.م")
        self.top_val_lbl.setText(f"{selling_price:,.2f} ج.م")

    def export_to_excel(self):
        default_filename = f"Blue_Healing_Cost_{self.meal_name_input.text().replace(' ', '_')}.xlsx"
        filepath, _ = QFileDialog.getSaveFileName(
            self, "حفظ ملف إكسيل", default_filename, "Excel Files (*.xlsx)"
        )
        if not filepath:
            return
            
        try:
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Blue Healing Recipe Card"
            ws.views.sheetView[0].showGridLines = True
            
            brand_font = XlFont(name="Arial", size=11, bold=True, color="93C5FD")
            title_font = XlFont(name="Arial", size=15, bold=True, color="FFFFFF")
            header_font = XlFont(name="Arial", size=10, bold=True, color="FFFFFF")
            bold_font = XlFont(name="Arial", size=10, bold=True, color="111827")
            normal_font = XlFont(name="Arial", size=10, color="1F2937")
            kpi_val_font = XlFont(name="Arial", size=11, bold=True, color="1E3A8A")
            price_val_font = XlFont(name="Arial", size=13, bold=True, color="065F46")
            
            navy_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
            royal_fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
            header_fill = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
            soft_blue_fill = PatternFill(start_color="EFF6FF", end_color="EFF6FF", fill_type="solid")
            soft_green_fill = PatternFill(start_color="ECFDF5", end_color="ECFDF5", fill_type="solid")
            summary_fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
            warning_fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
            
            thin_line = Side(border_style="thin", color="CBD5E1")
            double_bottom = Side(border_style="double", color="0F172A")
            border_all = Border(left=thin_line, right=thin_line, top=thin_line, bottom=thin_line)
            border_total = Border(left=thin_line, right=thin_line, top=thin_line, bottom=double_bottom)
            
            # Row 1: Brand Banner
            ws.merge_cells("A1:H1")
            ws["A1"] = "✦ BLUE HEALING ✦ | CULINARY OPERATIONS & MENU ENGINEERING"
            ws["A1"].font = brand_font
            ws["A1"].fill = navy_fill
            ws["A1"].alignment = XlAlign(horizontal="center", vertical="center")
            ws.row_dimensions[1].height = 25
            
            # Row 2: Title
            ws.merge_cells("A2:H2")
            ws["A2"] = "كارت تكلفة الوصفة المعيارية - STANDARD RECIPE COST CARD"
            ws["A2"].font = title_font
            ws["A2"].fill = royal_fill
            ws["A2"].alignment = XlAlign(horizontal="center", vertical="center")
            ws.row_dimensions[2].height = 35
            
            row_count = self.table.rowCount()
            start_row = 17
            season_row = start_row + row_count
            subtotal_row = season_row + 1
            waste_row = subtotal_row + 1
            total_row = waste_row + 1
            
            portions = self.portions_spin.value()
            price_date_str = self.price_date_edit.date().toString("yyyy-MM-dd")
            
            info_labels = [
                ("A4", "B4", "1. Item No. (رقم الصنف):", self.item_no_input.text()),
                ("A5", "B5", "Meal Name (اسم الوجبة):", self.meal_name_input.text()),
                ("A6", "B6", "2. No. of Portions (عدد الوجبات):", portions),
                ("A7", "B7", "3. Size of Portion (حجم الحصة):", self.portion_size_input.text()),
                ("A8", "B8", "تاريخ تسعير الخامات (Price Date):", price_date_str),
                ("A9", "B9", "4. Cost / Portion (تكلفة الوجبة):", f"=H{total_row}/B6"),
                ("A10", "B10", "5. Food Cost % (نسبة تكلفة الطعام):", self.food_cost_pct_spin.value() / 100.0),
                ("A11", "B11", "Pricing Multiplier (مُعامل الضرب):", self.multiplier_spin.value()),
                ("A12", "B12", "6. Selling Price / Portion (سعر البيع):", f"=B9*B11"),
                ("A13", "B13", "Team / فريق العمل:", "Blue Healing"),
            ]
            
            for lbl_c, val_c, label, val in info_labels:
                ws[lbl_c] = label
                ws[lbl_c].font = bold_font
                ws[lbl_c].fill = soft_blue_fill
                ws[lbl_c].alignment = XlAlign(horizontal="left", vertical="center")
                ws[lbl_c].border = border_all
                
                ws[val_c] = val
                ws[val_c].font = kpi_val_font if lbl_c in ["A9", "A12"] else normal_font
                ws[val_c].border = border_all
                ws[val_c].alignment = XlAlign(horizontal="center", vertical="center")
                
                if lbl_c == "A10":
                    ws[val_c].number_format = "0.0%"
                elif lbl_c in ["A9", "A12"]:
                    ws[val_c].number_format = '#,##0.00 "L.E"'
                    if lbl_c == "A12":
                        ws[val_c].font = price_val_font
                        ws[val_c].fill = soft_green_fill
            
            # Header Rows 15 & 16
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
            
            for c_ref in ["A15", "B15", "C15", "D15", "E15", "F15", "G15", "H15", "C16", "D16", "E16", "F16"]:
                ws[c_ref].font = header_font
                ws[c_ref].fill = header_fill
                ws[c_ref].alignment = XlAlign(horizontal="center", vertical="center", wrap_text=True)
                ws[c_ref].border = border_all
                
            for r in range(row_count):
                curr = start_row + r
                name = self.table.item(r, 0).text() if self.table.item(r, 0) else ""
                row_date_widget = self.table.cellWidget(r, 1)
                row_date = row_date_widget.date().toString("yyyy-MM-dd") if row_date_widget else price_date_str
                qty = self.table.cellWidget(r, 2).value()
                r_unit = self.table.cellWidget(r, 3).currentText()
                p_unit = self.table.cellWidget(r, 4).currentText()
                price = self.table.cellWidget(r, 5).value()
                _, conv = self.compute_ingredient_cost(qty, r_unit, p_unit, price)
                
                ws[f"A{curr}"] = name
                ws[f"B{curr}"] = row_date
                ws[f"C{curr}"] = qty
                ws[f"D{curr}"] = r_unit
                ws[f"E{curr}"] = p_unit
                ws[f"F{curr}"] = price
                ws[f"G{curr}"] = conv
                ws[f"H{curr}"] = f"=(C{curr}/G{curr})*F{curr}"
                
                ws[f"A{curr}"].alignment = XlAlign(horizontal="left", vertical="center")
                ws[f"B{curr}"].alignment = XlAlign(horizontal="center", vertical="center")
                ws[f"C{curr}"].alignment = XlAlign(horizontal="center", vertical="center")
                ws[f"D{curr}"].alignment = XlAlign(horizontal="center", vertical="center")
                ws[f"E{curr}"].alignment = XlAlign(horizontal="center", vertical="center")
                ws[f"F{curr}"].alignment = XlAlign(horizontal="right", vertical="center")
                ws[f"G{curr}"].alignment = XlAlign(horizontal="center", vertical="center")
                ws[f"H{curr}"].alignment = XlAlign(horizontal="right", vertical="center")
                
                ws[f"F{curr}"].number_format = '#,##0.00 "L.E"'
                ws[f"H{curr}"].number_format = '#,##0.00 "L.E"'
                
                for col in ["A", "B", "C", "D", "E", "F", "G", "H"]:
                    ws[f"{col}{curr}"].border = border_all
                    ws[f"{col}{curr}"].font = normal_font
                    
            # Bottom Summaries
            # Seasoning
            ws.merge_cells(f"A{season_row}:G{season_row}")
            ws[f"A{season_row}"] = "Seasoning (التوابل والبهارات)"
            ws[f"H{season_row}"] = self.seasoning_spin.value()
            
            # Sub-total
            ws.merge_cells(f"A{subtotal_row}:G{subtotal_row}")
            ws[f"A{subtotal_row}"] = "Sub-total (المجموع الفرعي = الخامات + التوابل)"
            ws[f"H{subtotal_row}"] = f"=SUM(H{start_row}:H{season_row-1})+H{season_row}"
            
            # Waste
            waste_pct_val = self.waste_spin.value() / 100.0
            ws.merge_cells(f"A{waste_row}:G{waste_row}")
            ws[f"A{waste_row}"] = f"{self.waste_spin.value()}% Waste (نسبة الهالك / الفاقد)"
            ws[f"H{waste_row}"] = f"=H{subtotal_row}*{waste_pct_val}"
            
            # Total Cost
            ws.merge_cells(f"A{total_row}:G{total_row}")
            ws[f"A{total_row}"] = "Total Cost (التكلفة الإجمالية للوصفة)"
            ws[f"H{total_row}"] = f"=H{subtotal_row}+H{waste_row}"
            
            sum_rows = [
                (season_row, bold_font, summary_fill, border_all),
                (subtotal_row, bold_font, warning_fill, border_all),
                (waste_row, bold_font, summary_fill, border_all),
                (total_row, XlFont(name="Arial", size=11, bold=True, color="1E3A8A"), soft_green_fill, border_total)
            ]
            for r, f_style, fill_style, b_style in sum_rows:
                ws[f"A{r}"].font = f_style
                ws[f"A{r}"].fill = fill_style
                ws[f"A{r}"].alignment = XlAlign(horizontal="right", vertical="center")
                ws[f"A{r}"].border = border_all
                
                ws[f"H{r}"].font = f_style
                ws[f"H{r}"].fill = fill_style
                ws[f"H{r}"].alignment = XlAlign(horizontal="right", vertical="center")
                ws[f"H{r}"].border = b_style
                ws[f"H{r}"].number_format = '#,##0.00 "L.E"'
                
                for col in ["B", "C", "D", "E", "F", "G"]:
                    ws[f"{col}{r}"].border = border_all
                    
            ws.column_dimensions["A"].width = 38
            ws.column_dimensions["B"].width = 15
            ws.column_dimensions["C"].width = 14
            ws.column_dimensions["D"].width = 14
            ws.column_dimensions["E"].width = 15
            ws.column_dimensions["F"].width = 17
            ws.column_dimensions["G"].width = 16
            ws.column_dimensions["H"].width = 22
            
            wb.save(filepath)
            QMessageBox.information(self, "نجاح", f"تم تصدير ملف الإكسيل بنجاح باسم فريق Blue Healing!\n\nالمسار:\n{filepath}")
        except Exception as e:
            QMessageBox.critical(self, "خطأ", f"حدث خطأ أثناء تصدير الملف:\n{str(e)}")

def main():
    app = QApplication(sys.argv)
    window = BlueHealingRecipeApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
