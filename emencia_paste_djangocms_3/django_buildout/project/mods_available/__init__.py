"""
.. _buildout: http://www.buildout.org/
.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Foundation 3: http://foundation.zurb.com/old-docs/f3/
.. _Foundation: http://foundation.zurb.com/
.. _Compass: http://compass-style.org/
.. _SCSS: http://sass-lang.com/
.. _rvm: http://rvm.io/
.. _Django: https://www.djangoproject.com/
.. _django-admin-tools: https://bitbucket.org/izi/django-admin-tools/
.. _Django CMS: https://www.django-cms.org/
.. _django-assets: https://github.com/miracle2k/django-assets/
.. _django-debug-toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar/
.. _Django Blog Zinnia: https://github.com/Fantomas42/django-blog-zinnia
.. _Django CKEditor: https://github.com/divio/djangocms-text-ckeditor/
.. _Django Filebrowser: https://github.com/wardi/django-filebrowser-no-grappelli
.. _django-google-tools: https://pypi.python.org/pypi/django-google-tools
.. _Django Porticus: https://github.com/emencia/porticus
.. _Django PDB: https://github.com/tomchristie/django-pdb
.. _Django flatpages app: https://docs.djangoproject.com/en/1.5/ref/contrib/flatpages/
.. _Django sites app: https://docs.djangoproject.com/en/1.5/ref/contrib/sites/
.. _Django reCaptcha: https://github.com/praekelt/django-recaptcha
.. _Django registration: https://github.com/macropin/django-registration
.. _CKEditor: http://ckeditor.com/
.. _emencia-cms-snippet: https://github.com/emencia/emencia-cms-snippet
.. _Service reCaptcha: http://www.google.com/recaptcha
.. _Django Codemirror: https://github.com/sveetch/djangocodemirror
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _crispy-forms-foundation: https://github.com/sveetch/crispy-forms-foundation
.. _emencia-django-slideshows: https://github.com/emencia/emencia-django-slideshows
.. _emencia-django-staticpages: https://github.com/emencia/emencia-django-staticpages
.. _emencia-django-socialaggregator: https://github.com/emencia/emencia-django-socialaggregator
.. _django-urls-map: https://github.com/sveetch/django-urls-map
.. _Sitemap framework: https://docs.djangoproject.com/en/1.5/ref/contrib/sitemaps/
.. _djangocms-admin-style: https://github.com/divio/djangocms-admin-style
.. _django-admin-shortcuts: https://github.com/alesdotio/django-admin-shortcuts/
.. _django-sendfile: https://github.com/johnsensible/django-sendfile
.. _django-filer: https://github.com/stefanfoulis/django-filer
.. _easy-thumbnails: https://github.com/SmileyChris/easy-thumbnails/

*******************
DjangoCMS 3.x paste
*******************

DjangoCMS projects are created with the many components that are available for use. These components are called **mods** and these mods are already installed and ready to use, but they are not all enabled. You can enable or disable them, as needed.

It is always preferable to use the mods system to install new apps. You should never install a new app with `pip`_. If you plan to integrate it into the project, always use the `buildout`_ system. Just open and edit the ``buildout.cfg`` file to add the new egg to be installed. For more details, read the `buildout`_ documentation.

Links
=====

* Download his `PyPi package <https://pypi.python.org/pypi/emencia_paste_djangocms_3>`_;
* Clone it on his `Github repository <https://github.com/emencia/emencia_paste_djangocms_3>`_;

Paste
=====

This paste will appear with the name ``djangocms-3`` in the paster templates list (with the ``paster create --list-templates`` command).

To use this paste to create a new project you will do something like : ::

    paster create -t djangocms-3 myproject

Django
======

django-instance
---------------

This is the command installed to replace the ``manage.py`` script in Django. ``django-instance`` is aware of the installed eggs.

Paste template version
----------------------

In your projects, you can find from which Paste template they have been builded in the ``project/__init__.py`` file where you should find the used package name and its version. So you can easily see the version doing something like : ::

    cat project/__init__.py

Note that previously (before the Epaster version 1.8), this file was containing the Epaster version, not the Paste template one, since the package didn't exists yet.

How the Mods work
-----------------

The advantage of centralizing app configurations in their mods is the project's ``settings.py`` and ``urls.py`` are gathered together in its configuration (cache, smtp, paths, BDD access, etc.). Furthermore, it is easier to enable or disable the apps.

To create a new mods, create a directory in ``$PROJECT/mods_avalaible/`` that contains at least one empty ``__init__.py`` and a ``settings.py`` to build the app in the project and potentially its settings. The `settings.py`` and ``urls.py`` files in this directory will be executed automatically by the project (the system loads them after the project ones so that a mods can overwrite the project's initial settings and urls). N.B. With Django's ``runserver`` command, a change to these files does not reload the project instance; you need to relaunch it yourself manually.

To enable a new mods, you need to create its symbolic link (**a relative path**) in ``$PROJECT/mods_enabled``. To disable it, simply delete the symbolic link.

Installation and initial use
============================

Once your project has been created with this epaster template, you need to install it to use it. The process is simple. Do it in your project directory: ::

    make install

When it's finished, active the virtual environment: ::

    source bin/active

You can then use the project on the development server: ::

    django-instance runserver 0.0.0.0:8001

.. note::
        ``0.0.0.0`` is some sort of alias that mean "bind this server on my ip", so if your local ip is "192.168.0.42", the server will be reachable in your browser with the url ``http://192.168.0.42:8001/``.

.. note::
        Note the ``:8001`` that mean "bind the server on this port", this is a required part when you specify an IP. Commonly you can't bind on the port 80 so allways prefer to use a port starting from *8001*.

.. note::
        If you don't know your local IP, you can use ``127.0.0.1`` that is an internal alias to mean "my own network card", but this IP cannot be reached from other computers (because they have also this alias linked to their own network card).

The first required action is the creation of a CMS page for the home page and also you should fill-in the site's name and its domain under ``Administration > Sites > Sites > Add site``.

Available mods
==============

.. document-mods::

Changelogs
==========

Version 1.2.4 - 2014/12/19
--------------------------

* Add Foundation's *kitchen sink* in a staticpage within ``project/templates/prototypes/foundation5.html`` and mounted on ``/prototypes/foundation5.html``;
* Add template tag library named ``utils_addons`` in ``project/utils/templatetags/``;
* Add ``split`` filter in ``utils_addons`` template tag library;
* Add nginx conf for admin with timeout and max body size increase;

Version 1.2.3 - 2014/12/02
--------------------------

* Improve ``sitemap`` mod, more modular and usefull;
* Add ``filer`` and ``thumbnails`` mod, ususally not used in our projects but it could be usefull for some specific goals;
* Fix contact_form app that was missing its ``sitemap.py`` file;
* Update to ``crispy-forms-foundation==0.4``;
* DjangoCMS page templates has moved from ``project/templates/cms`` to ``project/templates/pages``, following a recommandation from DjangoCMS' documentation;
* Add ``menu/menu_sidenav.html`` and ``pages/2_cols.autonav.html`` templates to have a template with deep menu for current root page;
* Update to ``porticus==0.9.6``;
* Update to ``emencia-django-slideshows==0.9.4``;

Version 1.2.2 - 2014/11/24
--------------------------

* Add ``sendfile`` mod;
* Add *client_max_body_size* sample directive usage in nginx template (but commented);
* Add commented location */protected_medias* to demonstrate sendfile mod usage within nginx template;

Version 1.2.1 - 2014/11/24
--------------------------

* Update to Foundation 5.4.7;

Version 1.2 - 2014/11/19
------------------------

* Refactoring Template code to open a new way for a much modular behavior, should not break anything;

Version 1.1.3 - 2014/11/17
--------------------------

* Mount 500 and 404 page view in urls.py when debug mode is activated;

Version 1.1.2 - 2014/11/16
--------------------------

* Fix a bug with symlinks that was not packaged and so was missing from the installed egg, this close #1, thanks to @ilanouh;
* Add missing gitignore rule to ignore debug_toolbar mod (it must never be installed from the start because it causes issues with cms and the syncdb command);

Version 1.1.1 - 2014/11/07
--------------------------

* Update to ``zc.buildout==2.2.5``;
* Update to ``buildout.recipe.uwsgi==0.0.24``;
* Update to ``collective.recipe.cmd==0.9``;
* Update to ``collective.recipe.template==1.11``;
* Update to ``djangorecipe==1.10``;
* Update to ``porticus==0.9.5``;
* Add package ``cmsplugin-porticus==0.2`` in buildout config;
* Remove dependancy for ``zc.buildout`` and ``zc.recipe.egg``;

Version 1.1 - 2014/11/03
------------------------

* Update to ``zc.buildout==2.2.4`` to fix a bug introduced in 2.2.3;
* Update to last ``bootstrap.py`` script;
* Remove Foundation3 sources, CSS and bundles, they are not used anymore;
* Move ckeditor and minimalist CSS to common SCSS sources with Foundation5;
* Update Compass README;
* Correct admin_style Compass config;
* Add 'ar' country to the CSS flags;
* Recompile all CSS in project's webapp_statics;
* Changing ``assets.py`` to use nested bundles, so we can separate app bundles (foundation, royalslider, etc..) from the main bundles where we load the app bundles;
* Main frontend's CSS & JS bundles are now called ``main.css`` and ``main.js`` not anymore ``app.***`` (yes we use the old Foundation3 ones that have been removed);

Version 1.0.4 - 2014/11/03
---------------------------

Update mods doc

Version 1.0.3 - 2014/11/03
--------------------------

Fix some app versions in version.cfg, fix app.js to use socialaggregator only if its lib is loaded.

Version 1.0.2 - 2014/11/03
--------------------------

Remove all enabled mods because it's the template responsability to enabled them or not.

Version 1.0.1 - 2014/11/03
--------------------------

Following repository renaming for a workaround with 'gp.vcsdevelop'.

Version 1.0 - 2014/11/03
------------------------

First commit started from emencia-paste-djangocms-2 == 1.9.1 and merged with buildout_cms3 repository, bump to 1.0

"""