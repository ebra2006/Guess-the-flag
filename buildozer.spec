[app]
# (اسم التطبيق)
title = MyApp
# (اسم الحزمة)
package.name = myapp
# (الإصدار)
version = 0.1
# (المتطلبات)
requirements = kivy, requests

# الأذونات المطلوبة للتطبيق (مثلًا الإنترنت)
android.permissions = INTERNET

# (حجم النافذة الافتراضي)
window.size = 480x320

# (أي ملفات إضافية، مثل الصور)
source.include_exts = py,png,jpg,kv,atlas
icon.filename = %(source.dir)s/icon.png

