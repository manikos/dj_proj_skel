This directory gets filled with the files located inside each dir of the setting `STATICFILES_DIRS` and inside each app's `static` directory.

These files, get copied here (this dir is the value of the setting `STATIC_ROOT` inside `settings/base.py`) using the command `./manage.py collectstatic`.
