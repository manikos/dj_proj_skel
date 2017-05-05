Inside here there will be 2 files only.


1. The django.po file
2. The django.mo file

* The `django.po` file is created/updated when the `./manage.py makemessages` is executed. This is the file that you write your translations in. This file is used to produce the `django.mo` file.
* The `django.mo` file is created/updated when the `./manage.py compilemessages` is executed. This file **must not** be altered. This is used my Django to derive translations.
