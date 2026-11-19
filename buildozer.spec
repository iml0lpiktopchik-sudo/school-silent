[app]
title = SchoolSilent
package.name = schoolsilent
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
# Фиксируем Python 3.10 и проверенный коммит pyjnius для совместимости
requirements = python3==3.10,kivy,plyer,pyjnius @ git+https://github.com/kivy/pyjnius.git@eaf76a5#egg=pyjnius

orientation = portrait
fullscreen = 0

android.permissions = ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, ACCESS_BACKGROUND_LOCATION, ACCESS_NOTIFICATION_POLICY
android.api = 33
android.minapi = 24
android.ndk = 25b
# Используем ветку develop для поддержки AAB
p4a.branch = develop
# Указываем, что нам нужен APK, а не AAB
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
