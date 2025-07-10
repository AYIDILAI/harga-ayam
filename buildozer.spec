[app]
# (str) Title of your application
title = HargaAyamApp

# (str) Package name
package.name = hargaayamapp

# (str) Package domain (unique, like a Java package)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (comma separated)
source.include_exts = py,txt,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = kivy

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Icon of the application
#icon.filename = %(source.dir)s/icon.png

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Supported Android API
android.api = 33

# (str) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android entry point, default is ok
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is 'import android' (light theme)
#android.theme = '@android:style/Theme.NoTitleBar'

# (list) Patterns to whitelist for the whole project
#android.whitelist = *

# (str) Custom Java class to use as an entry point
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Custom package data files to include
#android.add_src = src

# (str) Custom Java source files to include
#android.add_jars = foo.jar,bar.jar

# (list) Gradle dependencies to add (comma separated)
#android.gradle_dependencies = com.android.support:appcompat-v7:28.0.0

# (str) Path to a custom keystore file
#android.release_keystore = %(source.dir)s/android.keystore

# (str) Password for the keystore
#android.release_keyalias = mykey
#android.release_keyalias_password = password
#android.release_keystore_password = password

[buildozer]
# (int) Log level (0 = error only, 1 = warning, 2 = info, 3 = debug, 4 = trace)
log_level = 2

# (bool) Warn if root is used
warn_on_root = 1
