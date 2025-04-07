[app]
# اسم التطبيق
title = GuessTheFlag
# اسم الحزمة (Package Name)
package.name = guesstheflag
# اسم الحزمة الفريد
package.domain = org.example
# إصدار التطبيق
version = 1.0
# ملف Python الرئيسي
source.include_exts = py,png,jpg,kv,atlas

[buildozer]
# واجه البناء
log_level = 2
# نوع البناء (تجريبي أو نهائي)
release = 1  # تغيير هذا إلى 1 علشان تكون نسخة نهائية
# تحديد ملفات keystore للتوقيع
signing.keystore = /path/to/your/keystore
signing.keyalias = your-key-alias
signing.keypassword = your-key-password
signing.storepassword = your-store-password
