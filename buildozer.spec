[app]
title = SchoolSilent
package.name = schoolsilent
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3==3.9,kivy,plyer,jnius>=1.4.0

orientation = portrait
fullscreen = 0

android.permissions = ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, ACCESS_NOTIFICATION_POLICY
android.api = 33
android.minapi = 24
android.ndk = 25b
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
