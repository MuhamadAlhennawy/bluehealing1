import json

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Navigation Links for Activities & Gallery in the Hilton header
old_nav_links = """            <ul class="hotel-nav-links">
                <li><a href="#customerSection" class="active">المأكولات والمشروبات (Dining)</a></li>
                <li><a href="#amenitiesSection">المرافق الفندقية (Amenities)</a></li>
                <li><a href="javascript:void(0)" onclick="filterCustomerMenu('🎈 وجبات الأطفال')">منيو الأطفال (Kids Menu)</a></li>
                <li><a href="javascript:void(0)" onclick="openResortContactInfo()">معلومات الحجز (Info)</a></li>
            </ul>"""

new_nav_links = """            <ul class="hotel-nav-links">
                <li><a href="#customerSection" class="active">المأكولات الصحية (Healthy Dining)</a></li>
                <li><a href="#activitiesSection">الأنشطة والرياضة (Sports & Wellness)</a></li>
                <li><a href="#gallerySection">ألبوم المنتجع (Gallery)</a></li>
                <li><a href="javascript:void(0)" onclick="filterCustomerMenu('🎈 وجبات الأطفال')">منيو الأطفال (Kids)</a></li>
                <li><a href="#amenitiesSection">مرافق الضيافة (Amenities)</a></li>
            </ul>"""

if 'href="#activitiesSection"' not in html:
    html = html.replace(old_nav_links, new_nav_links)

# 2. Add Manager Buttons in the Manager Control Bar
old_m_buttons = """                <button class="btn btn-purple btn-sm" onclick="openCategoriesManagerModal()">📂 تعديل أقسام المنيو</button>
                <button class="btn btn-purple btn-sm" onclick="openAdminManagementModal()">👥 حسابات المدراء</button>"""

new_m_buttons = """                <button class="btn btn-primary btn-sm" style="background: linear-gradient(135deg, #059669, #10B981); border:none;" onclick="openActivitiesManagerModal()">🏃 إدارة الأنشطة الرياضية</button>
                <button class="btn btn-primary btn-sm" style="background: linear-gradient(135deg, #0284C7, #0EA5E9); border:none;" onclick="openGalleryManagerModal()">🖼️ إدارة ألبوم الصور</button>
                <button class="btn btn-gold btn-sm" onclick="openHeroImageModal()">🌅 تغيير صورة الواجهة</button>
                <button class="btn btn-purple btn-sm" onclick="openCategoriesManagerModal()">📂 تعديل أقسام المنيو</button>
                <button class="btn btn-purple btn-sm" onclick="openAdminManagementModal()">👥 حسابات المدراء</button>"""

if 'openActivitiesManagerModal()' not in html:
    html = html.replace(old_m_buttons, new_m_buttons)

# 3. Add Customer Sections: Sports Activities & Resort Gallery before customer footer
customer_footer_tag = '<div style="text-align: center; padding: 24px 10px; color: var(--text-muted); font-size: 13px; border-top: 1px solid var(--border);">'

wellness_and_gallery_sections = """
        <!-- ======================================================== -->
        <!-- SECTION: SPORTS & WELLNESS ACTIVITIES (الأنشطة والتمارين)  -->
        <!-- ======================================================== -->
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

            <!-- Activities Category Tabs -->
            <div class="hilton-category-tabs" id="activityCategoryPills">
                <!-- Dynamically rendered -->
            </div>

            <!-- Activities Grid -->
            <div class="customer-menu-grid" id="activitiesGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-bottom: 40px;">
                <!-- Activity cards rendered dynamically -->
            </div>
        </div>

        <!-- ======================================================== -->
        <!-- SECTION: RESORT PHOTO GALLERY (ألبوم صور المنتجع)         -->
        <!-- ======================================================== -->
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

            <!-- Gallery Category Tabs -->
            <div class="hilton-category-tabs" id="galleryCategoryPills">
                <!-- Dynamically rendered -->
            </div>

            <!-- Gallery Grid -->
            <div id="resortGalleryGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; max-width: 1360px; margin: 0 auto;">
                <!-- Gallery photos rendered dynamically -->
            </div>
        </div>
"""

if 'id="activitiesSection"' not in html:
    html = html.replace(customer_footer_tag, wellness_and_gallery_sections + "\n        " + customer_footer_tag)

# 4. Add Modals for:
# A) Activities Management
# B) Gallery Management
# C) Hero Image Modifier
# D) Gallery Lightbox Modal
modals_html = """
<!-- Modal: Activities Management (إدارة الأنشطة والتمارين الرياضية) -->
<div class="modal-overlay" id="activitiesManagerModal">
    <div class="modal-content" style="max-width: 850px;">
        <div class="modal-header" style="background: linear-gradient(135deg, #064E3B, #059669);">
            <span>🏃 إدارة الأنشطة الرياضية والتمارين (Sports & Wellness Activities)</span>
            <span style="cursor: pointer; font-size: 18px;" onclick="closeActivitiesManagerModal()">✕</span>
        </div>
        <div class="modal-body" style="max-height: 80vh; overflow-y: auto;">
            <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 14px;">
                يمكنك من هنا إضافة، تعديل أو حذف الأنشطة الرياضية، مواعيدها، مدربيها، وأسعارها لعرضها مباشرة لزوار المنتجع.
            </p>

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

            <div class="manager-sub-box" id="activityFormBox">
                <h4 style="font-size: 13px; font-weight: 800; color: #1E293B; margin-bottom: 10px;" id="activityFormTitle">
                    ➕ إضافة نشاط أو تمرين رياضي جديد
                </h4>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px;">
                    <div class="form-control" style="grid-column: span 2;">
                        <label>عنوان النشاط الرياضي (Activity Title):</label>
                        <input type="text" id="actInputTitle" placeholder="مثال: يوغا صباحية على الشاطئ (Sunrise Yoga)">
                    </div>
                    <div class="form-control">
                        <label>قسم النشاط (Category):</label>
                        <select id="actInputCategory">
                            <option value="يوغا وتأمل">🧘 يوغا وتأمل</option>
                            <option value="لياقة وتمارين">🏋️ لياقة وتمارين (Gym & Fitness)</option>
                            <option value="رياضات مائية">🏊 رياضات مائية وسباحة</option>
                            <option value="سبا واستشفاء">💆 سبا واستشفاء (Recovery)</option>
                            <option value="مضرب وتنس">🎾 ملاعب بادل وتنس</option>
                        </select>
                    </div>
                    <div class="form-control">
                        <label>المواعيد والجدول (Schedule):</label>
                        <input type="text" id="actInputSchedule" placeholder="مثال: يومياً: 06:30 ص - 07:30 ص">
                    </div>
                    <div class="form-control">
                        <label>المدرب المسؤول (Instructor):</label>
                        <input type="text" id="actInputInstructor" placeholder="مثال: كابتن سارة أحمد (معتمدة)">
                    </div>
                    <div class="form-control">
                        <label>الشدة والمستوى (Intensity):</label>
                        <input type="text" id="actInputIntensity" placeholder="مثال: خفيف ومريح / متوسط">
                    </div>
                    <div class="form-control">
                        <label>السعر (Price):</label>
                        <input type="text" id="actInputPrice" placeholder="مثال: 150 ج.م أو مجاناً للنزلاء">
                    </div>
                    <div class="form-control" style="grid-column: span 2;">
                        <label>وصف النشاط ومزاياه (Description):</label>
                        <textarea id="actInputDesc" rows="2" placeholder="اكتب وصفاً جذاباً للنشاط ومميزاته للزوار..."></textarea>
                    </div>
                    <div class="form-control" style="grid-column: span 2;">
                        <label>صورة النشاط (Photo Upload / URL):</label>
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

<!-- Modal: Gallery Management (إدارة ألبوم صور المنتجع) -->
<div class="modal-overlay" id="galleryManagerModal">
    <div class="modal-content" style="max-width: 800px;">
        <div class="modal-header" style="background: linear-gradient(135deg, #004B87, #0284C7);">
            <span>🖼️ إدارة ألبوم صور المنتجع والمرافق (Resort Gallery Manager)</span>
            <span style="cursor: pointer; font-size: 18px;" onclick="closeGalleryManagerModal()">✕</span>
        </div>
        <div class="modal-body" style="max-height: 80vh; overflow-y: auto;">
            <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 14px;">
                أضف صور مرافق المنتجع (المسابح، الجيم، الشاطئ، الشاليهات، المطعم الصحي) ليراها الزوار في ألبوم الصور.
            </p>

            <!-- Add Photo Box -->
            <div class="manager-sub-box" style="margin-bottom: 16px;">
                <h4 style="font-size: 13px; font-weight: 800; color: #1E293B; margin-bottom: 10px;">
                    ➕ إضافة صورة جديدة للألبوم:
                </h4>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px;">
                    <div class="form-control">
                        <label>عنوان الصورة / المرفق (Title):</label>
                        <input type="text" id="galInputTitle" placeholder="مثال: مسبح إنفينيتي المطل على البحر">
                    </div>
                    <div class="form-control">
                        <label>تصنيف المرفق (Category):</label>
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
                            <input type="text" id="galInputImage" placeholder="رابط صورة المرفق أو اختر من جهازك..." style="flex-grow: 1;">
                            <button type="button" class="btn btn-outline btn-sm" onclick="triggerGalleryPhotoUpload()">📁 رفع صورة</button>
                        </div>
                        <input type="file" id="galFileInput" accept="image/*" style="display:none;" onchange="handleGalleryPhotoUpload(event)">
                    </div>
                </div>
                <div style="display: flex; justify-content: flex-end; margin-top: 10px;">
                    <button class="btn btn-primary btn-sm" onclick="addPhotoToGallery()">إضافة إلى الألبوم 📸</button>
                </div>
            </div>

            <!-- Existing Photos Grid in Manager -->
            <h4 style="font-size: 13px; font-weight: 800; color: #1E293B; margin-bottom: 10px;">
                📸 الصور الحالية في الألبوم:
            </h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px;" id="managerGalleryGrid">
                <!-- Rendered dynamically -->
            </div>
        </div>
        <div class="modal-footer">
            <button class="btn btn-secondary btn-sm" onclick="closeGalleryManagerModal()">إغلاق</button>
        </div>
    </div>
</div>

<!-- Modal: Hero Cover Image Modifier (تعديل صورة الواجهة الرئيسية) -->
<div class="modal-overlay" id="heroImageModal">
    <div class="modal-content" style="max-width: 650px;">
        <div class="modal-header" style="background: linear-gradient(135deg, #B8860B, #D97706);">
            <span>🌅 تعديل وتغيير صورة الواجهة الرئيسية (Hero Cover Image)</span>
            <span style="cursor: pointer; font-size: 18px;" onclick="closeHeroImageModal()">✕</span>
        </div>
        <div class="modal-body">
            <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 14px;">
                اختر صورة بانورامية عالية الجودة تعبر عن منتجعك الصحي (شاطئ، مسبح إنفينيتي، يوغا، أو قاعة الطعام الساحلية).
            </p>

            <!-- Current Preview -->
            <div style="width: 100%; height: 200px; border-radius: var(--radius-md); overflow: hidden; margin-bottom: 14px; position: relative; border: 1px solid var(--border);">
                <img id="heroImagePreview" src="" alt="Hero Preview" style="width:100%; height:100%; object-fit: cover;">
                <div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.65); color:white; font-size:11px; padding:3px 8px; border-radius:4px;">
                    معاينة الواجهة الحالية
                </div>
            </div>

            <!-- Upload or URL -->
            <div class="form-control" style="margin-bottom: 12px;">
                <label>رابط الصورة المباشر (Image URL):</label>
                <div style="display: flex; gap: 8px;">
                    <input type="text" id="heroImageUrlInput" placeholder="ضع رابط صورة عالي الجودة هنا..." oninput="updateHeroPreview(this.value)">
                    <button class="btn btn-outline btn-sm" onclick="triggerHeroPhotoUpload()">📁 رفع من جهازك</button>
                </div>
                <input type="file" id="heroFileInput" accept="image/*" style="display:none;" onchange="handleHeroPhotoUpload(event)">
            </div>

            <!-- Preset Luxury Images -->
            <div style="margin-bottom: 14px;">
                <label style="font-size: 12px; font-weight: 800; color: #334155; display: block; margin-bottom: 6px;">
                    ✨ صور بانورامية فندقية مقترحة (اضغط للاختيار فوراً):
                </label>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;">
                    <div onclick="selectHeroPreset('https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1920&q=85')" style="height: 60px; border-radius: 6px; overflow: hidden; cursor: pointer; border: 2px solid transparent;" onmouseover="this.style.borderColor='var(--brand-primary)'" onmouseout="this.style.borderColor='transparent'">
                        <img src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=300&q=80" style="width:100%; height:100%; object-fit: cover;" title="مطعم يوناني وإطلالة البحر">
                    </div>
                    <div onclick="selectHeroPreset('https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=1920&q=85')" style="height: 60px; border-radius: 6px; overflow: hidden; cursor: pointer; border: 2px solid transparent;" onmouseover="this.style.borderColor='var(--brand-primary)'" onmouseout="this.style.borderColor='transparent'">
                        <img src="https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=300&q=80" style="width:100%; height:100%; object-fit: cover;" title="مسبح إنفينيتي شاطئي">
                    </div>
                    <div onclick="selectHeroPreset('https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=1920&q=85')" style="height: 60px; border-radius: 6px; overflow: hidden; cursor: pointer; border: 2px solid transparent;" onmouseover="this.style.borderColor='var(--brand-primary)'" onmouseout="this.style.borderColor='transparent'">
                        <img src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=300&q=80" style="width:100%; height:100%; object-fit: cover;" title="يوغا واستشفاء على الشاطئ">
                    </div>
                    <div onclick="selectHeroPreset('https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?auto=format&fit=crop&w=1920&q=85')" style="height: 60px; border-radius: 6px; overflow: hidden; cursor: pointer; border: 2px solid transparent;" onmouseover="this.style.borderColor='var(--brand-primary)'" onmouseout="this.style.borderColor='transparent'">
                        <img src="https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?auto=format&fit=crop&w=300&q=80" style="width:100%; height:100%; object-fit: cover;" title="منتجع صحي ولاونج فاخر">
                    </div>
                </div>
            </div>
        </div>
        <div class="modal-footer">
            <button class="btn btn-secondary btn-sm" onclick="closeHeroImageModal()">إلغاء</button>
            <button class="btn btn-gold btn-sm" onclick="saveHeroImage()">حفظ صورة الواجهة وتحديث الموقع 💾</button>
        </div>
    </div>
</div>

<!-- Modal: Lightbox for Gallery (عرض الصورة مكبرة) -->
<div class="modal-overlay" id="galleryLightboxModal" onclick="closeGalleryLightbox(event)">
    <div style="position: relative; max-width: 90vw; max-height: 90vh; display: flex; flex-direction: column; align-items: center;">
        <span style="position: absolute; top: -35px; right: 0; color: white; font-size: 28px; cursor: pointer;" onclick="document.getElementById('galleryLightboxModal').classList.remove('active')">✕</span>
        <img id="lightboxImg" src="" style="max-width: 100%; max-height: 80vh; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <div id="lightboxCaption" style="color: white; font-size: 14px; font-weight: 700; margin-top: 10px; text-align: center; text-shadow: 0 1px 4px rgba(0,0,0,0.8);"></div>
    </div>
</div>
"""

if 'id="activitiesManagerModal"' not in html:
    html = html.replace('<div class="modal-overlay" id="themeModifierModal">', modals_html + '\n<div class="modal-overlay" id="themeModifierModal">')

# 5. Add JavaScript State and Logic for Activities, Gallery, and Hero Image
wellness_js = """
    // ========================================================
    // WELLNESS ACTIVITIES & RESORT GALLERY SYSTEM
    // ========================================================
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

    let selectedActivityCategory = "الكل";
    let selectedGalleryCategory = "الكل";
    let editingActivityId = null;

    // --- ACTIVITIES LOGIC ---
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
        const activities = (appState.activities && appState.activities.length) ? appState.activities : defaultActivities;
        const filtered = selectedActivityCategory === "الكل" ? activities : activities.filter(a => a.category === selectedActivityCategory);

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

    // --- ACTIVITIES MODAL FOR MANAGER ---
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
        const list = (appState.activities && appState.activities.length) ? appState.activities : defaultActivities;
        tbody.innerHTML = list.map(a => `
            <tr>
                <td><b>${a.title}</b></td>
                <td><span class="badge" style="background:#ECFDF5; color:#065F46;">${a.category}</span></td>
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

    function triggerActivityPhotoUpload() {
        document.getElementById("actFileInput").click();
    }

    function handleActivityPhotoUpload(e) {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = function(evt) {
            const img = new Image();
            img.onload = function() {
                const canvas = document.createElement("canvas");
                const MAX_WIDTH = 800;
                let width = img.width;
                let height = img.height;
                if (width > MAX_WIDTH) {
                    height *= MAX_WIDTH / width;
                    width = MAX_WIDTH;
                }
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext("2d");
                ctx.drawImage(img, 0, 0, width, height);
                const compressed = canvas.toDataURL("image/jpeg", 0.82);
                document.getElementById("actInputImage").value = compressed;
            };
            img.src = evt.target.result;
        };
        reader.readAsDataURL(file);
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

        if (!appState.activities) appState.activities = [...defaultActivities];

        if (editingActivityId) {
            const act = appState.activities.find(a => a.id === editingActivityId);
            if (act) {
                act.title = title;
                act.category = category;
                act.schedule = schedule;
                act.instructor = instructor;
                act.intensity = intensity;
                act.price = price;
                act.description = desc;
                act.image = img;
            }
            editingActivityId = null;
        } else {
            appState.activities.push({
                id: "act_" + Date.now(),
                title, category, schedule, instructor, intensity, price,
                description: desc, image: img
            });
        }

        saveState();
        renderActivitiesManagerTable();
        resetActivityForm();
        renderActivitiesUI();
        alert("✨ تم حفظ النشاط الرياضي بنجاح!");
    }

    function startEditActivity(id) {
        const list = appState.activities || defaultActivities;
        const act = list.find(a => a.id === id);
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
        if (!appState.activities) appState.activities = [...defaultActivities];
        appState.activities = appState.activities.filter(a => a.id !== id);
        saveState();
        renderActivitiesManagerTable();
        renderActivitiesUI();
    }

    // --- GALLERY LOGIC ---
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
        const gallery = (appState.gallery && appState.gallery.length) ? appState.gallery : defaultGallery;
        const filtered = selectedGalleryCategory === "الكل" ? gallery : gallery.filter(g => g.category === selectedGalleryCategory);

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

    function openGalleryLightbox(imgUrl, caption) {
        document.getElementById("lightboxImg").src = imgUrl;
        document.getElementById("lightboxCaption").innerText = caption || "";
        document.getElementById("galleryLightboxModal").classList.add("active");
    }

    function closeGalleryLightbox(e) {
        if (e.target.id === "galleryLightboxModal") {
            document.getElementById("galleryLightboxModal").classList.remove("active");
        }
    }

    // --- GALLERY MODAL FOR MANAGER ---
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
        const list = (appState.gallery && appState.gallery.length) ? appState.gallery : defaultGallery;
        grid.innerHTML = list.map(item => `
            <div style="border: 1px solid var(--border); border-radius: 8px; overflow: hidden; background: white; padding: 6px;">
                <img src="${item.image}" style="width: 100%; height: 110px; object-fit: cover; border-radius: 6px;">
                <div style="font-weight: 800; font-size: 11px; margin: 4px 0 2px;">${item.title}</div>
                <div style="font-size: 10px; color: var(--text-muted); margin-bottom: 6px;">${item.category}</div>
                <button class="btn btn-danger btn-sm" style="width: 100%; padding: 3px; font-size: 11px;" onclick="deleteGalleryItem('${item.id}')">حذف الصورة 🗑️</button>
            </div>
        `).join("");
    }

    function triggerGalleryPhotoUpload() {
        document.getElementById("galFileInput").click();
    }

    function handleGalleryPhotoUpload(e) {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = function(evt) {
            const img = new Image();
            img.onload = function() {
                const canvas = document.createElement("canvas");
                const MAX_WIDTH = 900;
                let width = img.width;
                let height = img.height;
                if (width > MAX_WIDTH) {
                    height *= MAX_WIDTH / width;
                    width = MAX_WIDTH;
                }
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext("2d");
                ctx.drawImage(img, 0, 0, width, height);
                const compressed = canvas.toDataURL("image/jpeg", 0.82);
                document.getElementById("galInputImage").value = compressed;
            };
            img.src = evt.target.result;
        };
        reader.readAsDataURL(file);
    }

    function addPhotoToGallery() {
        const title = document.getElementById("galInputTitle").value.trim();
        const cat = document.getElementById("galInputCategory").value;
        const img = document.getElementById("galInputImage").value.trim();
        if (!title || !img) {
            alert("من فضلك أدخل عنوان الصورة ورابطها أو ارفعها من جهازك.");
            return;
        }

        if (!appState.gallery) appState.gallery = [...defaultGallery];
        appState.gallery.push({
            id: "gal_" + Date.now(),
            title,
            category: cat,
            image: img
        });

        saveState();
        renderGalleryManagerGrid();
        renderGalleryUI();
        document.getElementById("galInputTitle").value = "";
        document.getElementById("galInputImage").value = "";
        alert("✨ تم إضافة الصورة للألبوم بنجاح!");
    }

    function deleteGalleryItem(id) {
        if (!confirm("هل أنت متأكد من حذف هذه الصورة من الألبوم؟")) return;
        if (!appState.gallery) appState.gallery = [...defaultGallery];
        appState.gallery = appState.gallery.filter(g => g.id !== id);
        saveState();
        renderGalleryManagerGrid();
        renderGalleryUI();
    }

    // --- HERO IMAGE MODIFIER ---
    function openHeroImageModal() {
        const currentHero = (appState.resortSettings && appState.resortSettings.heroImage) || "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1920&q=85";
        document.getElementById("heroImageUrlInput").value = currentHero;
        document.getElementById("heroImagePreview").src = currentHero;
        document.getElementById("heroImageModal").classList.add("active");
    }

    function closeHeroImageModal() {
        document.getElementById("heroImageModal").classList.remove("active");
    }

    function updateHeroPreview(url) {
        if (url) document.getElementById("heroImagePreview").src = url;
    }

    function selectHeroPreset(url) {
        document.getElementById("heroImageUrlInput").value = url;
        document.getElementById("heroImagePreview").src = url;
    }

    function triggerHeroPhotoUpload() {
        document.getElementById("heroFileInput").click();
    }

    function handleHeroPhotoUpload(e) {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = function(evt) {
            const img = new Image();
            img.onload = function() {
                const canvas = document.createElement("canvas");
                const MAX_WIDTH = 1920;
                let width = img.width;
                let height = img.height;
                if (width > MAX_WIDTH) {
                    height *= MAX_WIDTH / width;
                    width = MAX_WIDTH;
                }
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext("2d");
                ctx.drawImage(img, 0, 0, width, height);
                const compressed = canvas.toDataURL("image/jpeg", 0.82);
                document.getElementById("heroImageUrlInput").value = compressed;
                document.getElementById("heroImagePreview").src = compressed;
            };
            img.src = evt.target.result;
        };
        reader.readAsDataURL(file);
    }

    function saveHeroImage() {
        const url = document.getElementById("heroImageUrlInput").value.trim();
        if (!url) {
            alert("من فضلك أدخل رابط صورة الواجهة أو ارفع صورة من جهازك.");
            return;
        }

        if (!appState.resortSettings) appState.resortSettings = { ...defaultResortSettings };
        appState.resortSettings.heroImage = url;
        saveState();

        const heroBg = document.querySelector(".resort-hero-bg");
        if (heroBg) heroBg.src = url;

        closeHeroImageModal();
        alert("✨ تم تحديث وحفظ صورة الواجهة الرئيسية بنجاح!");
    }
"""

if 'defaultActivities' not in html:
    html = html.replace("const segmentColors =", wellness_js + "\n    const segmentColors =")

# Ensure applyResortSettingsUI applies heroImage if present
hero_apply_code = """
        if (resort.heroImage) {
            const heroBg = document.querySelector(".resort-hero-bg");
            if (heroBg) heroBg.src = resort.heroImage;
        }
"""
if 'resort.heroImage' not in html:
    html = html.replace('if (utilPhone) utilPhone.innerText = "📞 الحجز والاستعلام: " + (resort.phone || "01000000000");', 'if (utilPhone) utilPhone.innerText = "📞 الحجز والاستعلام: " + (resort.phone || "01000000000");\n' + hero_apply_code)

# Ensure renderActivitiesUI and renderGalleryUI are initialized on load
init_calls = """
        renderActivitiesUI();
        renderGalleryUI();
"""
if 'renderActivitiesUI();' not in html:
    html = html.replace("renderCustomerMenu();", "renderCustomerMenu();\n" + init_calls)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Wellness Activities, Photo Gallery & Hero Image Modifier successfully added!")
