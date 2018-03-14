Run this template with Django installed
using this command:

    django-admin startproject --template https://github.com/manikos/dj_proj_skel/archive/master.zip --extension py,json --name gitignore project_name

After project created in your desired (local) directory, you can delete the README.md file from your directory.

The produced project structure looks like this:


<pre>proj
├── fabfile.py
├── gitignore
├── logs
│   ├── db.log
│   ├── dev.log
│   ├── my_apps.log
│   └── production.log
├── manage.py
├── media_root # saved uploaded files
│   └── README.md
├── myutils    # an app with common features applied (if needed) to all other apps
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── __init__.py
│   ├── locale
│   │   └── el
│   │       └── LC_MESSAGES
│   │           └── README.md
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templatetags
│   │   ├── __init__.py
│   │   ├── myutils_filters.py
│   │   └── myutils_tags.py
│   ├── tests.py
│   └── views.py
├── proj
│   ├── __init__.py
│   ├── locale
│   │   └── el
│   │       └── LC_MESSAGES
│   │           └── README.md
│   ├── settings
│   │   ├── base.py
│   │   ├── __init__.py
│   │   ├── local.py-tpl
│   │   ├── production.py
│   │   └── secret.json
│   ├── sitemap.py
│   ├── urls.py
│   └── wsgi.py
├── READ_ME
├── README.md
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── robots.txt
├── static
│   ├── css
│   │   └── style.css  # empty
│   ├── img
│   │   └── empty.png  # empty
│   └── js
│       └── main.js    # empty
├── static_root
│   └── README.md
└── templates
    ├── base
    │   └── base.html
    └── sitemap.xml
</pre>
