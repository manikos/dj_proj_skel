Run this template with Django installed
using this command:

    django-admin startproject --template https://github.com/manikos/dj_proj_skel/archive/master.zip --extension py,json --name gitignore project_name

After project created in your desired (local) directory, you can delete the README.md file from your directory.

The produced project structure looks like this:

    proj/
        logs/
    	    db.log
    	    dev.log
    	    my_apps.log
    	    production.log
        media_root/  # saved uploaded files
        myutils/  # an app with common features applied (if needed) to all other apps
    	    locale/
    	    migrations/
    	    temlatetags/
    	    admin.py
    	    apps.py
    	    context_processors.py
    	    __init__.py
    	    models.py
    	    tests.py
    	    views.py
        proj/
    	    locale/
    	    settings/
    		    base.py
    		    __init__.py
    		    local.py
    		    prod.py
    		    secret.json
    	    __init__.py
    	    sitemap.py
    	    urls.py
    	    wsgi.py
        requirements/
    	    base.txt
    	    dev.txt
    	    prod.txt
        static/
        static_root/
        templates/
    	    base/
    		    base.html
    	    sitemap.xml
        .gitignore  # DO NOT FORGET to rename gitignore to .gitignore!
        manage.py
        robots.txt

