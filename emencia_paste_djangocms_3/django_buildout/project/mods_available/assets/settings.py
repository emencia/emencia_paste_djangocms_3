# -*- coding: utf-8 -*-

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'django_assets')

ASSETS_DEBUG = DEBUG
ASSETS_ROOT = join(PROJECT_PATH, 'webapp_statics/')
STATICFILES_DIRS += (ASSETS_ROOT,)
ASSETS_MODULES = (
    'project.assets',
)
