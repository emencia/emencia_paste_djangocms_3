# -*- coding: UTF-8 -*-
"""
Paste for DjangoCMS 3.x, install all needed stuff plus some optionnal apps
"""
from os import getcwd, symlink
from os.path import dirname, join
from random import choice
from subprocess import Popen, PIPE
from sys import modules, exit

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
    """
    Paste
    """
    # Relative path to the directory containing all stuff to install
    _template_dir = 'django_buildout'
    # Summary as it will be displayed with "--list-templates" paster argument
    summary = "DjangoCMS 3.x project"
    # A list of symlinks to create in the post process
    symlink_list = [
        # ([Target to link], [Symlink file to create]),
    ]
    # Questions to ask to enable some mods/options
    vars = [
        var('admin_style', 'Enable "djangocms_admin_style" (yes/no)', default='yes'),
        var('accounts', 'Enable "accounts registration" (yes/no)', default='yes'),
        var('contact_form', 'Enable "contact_form" (yes/no)', default='yes'),
        var('porticus', 'Enable "Porticus" (yes/no)', default='yes'),
        var('site_metas', 'Enable "site_metas" (yes/no)', default='yes'),
        var('slideshows', 'Enable "Slideshows" (yes/no)', default='yes'),
        var('socialaggregator', 'Enable "Social Aggregator" (yes/no)', default='yes'),
        var('zinnia', 'Enable Zinnia (yes/no)', default='yes'),
    ]

    def pre(self, command, output_dir, kw):
        """
        Prepare some context before install (will be accessible from paste templates)
        """
        # Build a random secret_key
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        kw['secret_key'] = ''.join([ choice(chars) for i in range(50) ])

        # Paste version
        kw['epaster_template_name'] = 'emencia-paste-djangocms-3'
        kw['epaster_template_version'] = template_version


    def post(self, command, output_dir, vars):
        """
        Do some tasks after install
        """
        if command.simulate:
            return
        
        # Find the 'project/' dir in the created paste project
        project = join(getcwd(), vars['project'], 'project')
        
        # 1. Mods
        mods = [var.name for var in self.vars if vars[var.name].lower() == 'yes']
        mods = set(mods)

        # Required
        mods.add('emencia_utils')       # Useful utilities
        mods.add('sitemap')   # Common sitemap for djangocms and other apps
        mods.add('assets')       # Used in templates
        mods.add('google_tools') # Used in templates
        mods.add('cms')
        mods.add('filebrowser') # Used in djangocms and zinnia
        mods.add('ckeditor')     # Used in djangocms and zinnia
        #mods.add('codemirror')   # Used in snippet cms plugin
        
        # Conditionnal dependancies
        if 'contact_form' in mods:
            mods.add('crispy_forms')
            mods.add('recaptcha')
        if 'cms' in mods:
            # Mirroring Ckeditor JS overrides for the CKEditor cmsplugin that 
            # use a different namespace than 'django-ckeditor'
            self.symlink_list.append(('ckeditor', join(project, 'mods_available/ckeditor/static/djangocms_text_ckeditor')))

        # Enable all selected mods (it resumes to make a list of symlinks to 
        # do in mods_enabled)
        for name in mods:
            self.symlink_list.append((
                join('..', 'mods_available', name),
                join(project, 'mods_enabled', name)
            ))
        
        # Generic list items to make some useful symlinks like mods
        for target, linkfile in self.symlink_list:
            symlink(target, linkfile)

        # 2. Git initialization
        call = Caller(vars['project'])
        call('git', 'init', '.')
        call('git', 'add', '.')
        call('git', 'commit', '-m', 'First commit')
