"""
.. djangocms-admin-style: https://github.com/divio/djangocms-admin-style
.. django-admin-shortcuts: https://github.com/alesdotio/django-admin-shortcuts/

Enable `djangocms-admin-style`_ to enhance the administration interface. Also enable `django-admin-shortcuts`_.

*admin-style* better fit with DjangoCMS than *admin_tools*. This mod cannot live with *admin_tools*, you have to choose only one of them.
"""
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'djangocms_admin_style', before="django.contrib.admin")

