# -*- coding: UTF-8 -*-

# Import from the Standard Library
from os import getcwd, symlink
from os.path import dirname, join
from random import choice
from subprocess import Popen, PIPE
from sys import modules, exit

# Import from PasteScript
from paste.script.templates import Template, var
from __init__ import __version__ as template_version

class Caller(object):

    def __init__(self, cwd=None):
        self.cwd = cwd


    def __call__(self, *args):
        popen = Popen(args, stdout=PIPE, stderr=PIPE, cwd=self.cwd)
        out, err = popen.communicate()
        if popen.returncode != 0:
            print args
            print 'Exit %d' % popen.returncode
            exit(popen.returncode)
        return out



class Django(Template):

    summary = "DjangoCMS 3.x project"
    _template_dir = 'django_buildout'
    vars = [
        var('admin_tools', 'Enable admin_tools (yes/no)', default='yes'),
        var('accounts', 'Enable accounts registration (yes/no)', default='yes'),
        var('contact_form', 'Enable contact_form (yes/no)', default='yes'),
        var('porticus', 'Enable porticus (yes/no)', default='yes'),
        var('site_metas', 'Enable site_metas (yes/no)', default='yes'),
        var('slideshows', 'Enable Slideshows (yes/no)', default='yes'),
        var('zinnia', 'Enable Zinnia (yes/no)', default='yes'),
        ]


    def pre(self, command, output_dir, kw):
        # secret_key
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        kw['secret_key'] = ''.join([ choice(chars) for i in range(50) ])

        # template version
        kw['epaster_template_name'] = 'emencia-paste-djangocms-3'
        kw['epaster_template_version'] = template_version


    def post(self, command, output_dir, vars):
        if command.simulate:
            return

        # 1. Mods
        mods = [
            var.name for var in self.vars if vars[var.name].lower() == 'yes' ]
        mods = set(mods)

        # Required
        mods.add('emencia_utils')       # Useful utilities
        mods.add('sitemap')   # Common sitemap for djangocms and other apps
        mods.add('assets')       # Used in templates
        mods.add('google_tools') # Used in templates
        mods.add('cms')
        mods.add('filebrowser') # Used in djangocms and zinnia
        mods.add('ckeditor')     # Used in djangocms and zinnia
        mods.add('codemirror')   # Used in snippet cms plugin
        
        # Conditionnal dependancies
        if 'contact_form' in mods:
            mods.add('crispy_forms')
            mods.add('recaptcha')

        # Enable
        project = join(getcwd(), vars['project'], 'project')
        for name in mods:
            symlink(
                join('..', 'mods_available', name),
                join(project, 'mods_enabled', name))

        # 2. Git initialization
        call = Caller(vars['project'])
        call('git', 'init', '.')                    # init
        call('git', 'add', '.')                     # add
        call('git', 'commit', '-m', 'First commit') # commit
