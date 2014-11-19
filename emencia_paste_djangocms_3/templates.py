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
    # Summary as it will be displayed with "--list-templates" paster argument
    summary = "DjangoCMS 3.x project"
    # Relative path to the directory containing all stuff to install
    _template_dir = 'django_buildout'
    # A list of symlinks to create in the post process
    symlink_list = [
        # ([Target to link], [Symlink file to create]),
    ]
    # The base mods list to enable
    mods_list = [
        'admin_style',
        'assets', # Used in templates
        'ckeditor', # Used in djangocms and another apps
        'cms',
        'emencia_utils', # Useful utilities
        'filebrowser', # Used in djangocms and another apps
        'google_tools', # Used for almost customer projects
        'site_metas', # Common sitemap for djangocms and another apps
        'sitemap', # Common sitemap for djangocms and another apps
    ]
    # Questions to enable some optionnal mods
    vars = [
        var('accounts', 'Enable "Accounts registration" (yes/no)', default='yes'),
        #var('cms', 'Enable "DjangoCMS" (yes/no)', default='yes'),
        var('contact_form', 'Enable "contact_form" (yes/no)', default='yes'),
        var('porticus', 'Enable "Porticus" (yes/no)', default='yes'),
        var('slideshows', 'Enable "Slideshows" (yes/no)', default='yes'),
        var('socialaggregator', 'Enable "Social Aggregator" (yes/no)', default='yes'),
        var('zinnia', 'Enable Zinnia (yes/no)', default='yes'),
    ]

    def pre(self, command, output_dir, kw):
        """
        Prepare some context before install
        
        Added kwargs in ``kw`` will be accessible into paste template files
        """
        # Build a random secret_key
        chars = u'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        kw['secret_key'] = ''.join([ choice(chars) for i in range(50) ])

        # Paste version
        kw['epaster_template_name'] = u'emencia-paste-djangocms-3'
        kw['epaster_template_version'] = template_version

    def get_mods(self, project_path, vars):
        """
        Build the mod list to enable
        """
        # Start with answers from interactive command
        mods = [var.name for var in self.vars if vars[var.name].lower() == 'yes']
        mods = set(mods)

        # Base mods
        for name in self.mods_list:
            mods.add(name)
        
        # Conditionnal mods dependancies
        if 'accounts' in mods or 'contact_form' in mods:
            mods.add('crispy_forms')
            mods.add('recaptcha')
        
        return mods

    def get_symlinks(self, project_path, vars, mods):
        """
        Build the symlink list to create (to enable mods and other stuff)
        """
        # Some additional symlinks
        if 'cms' in mods:
            # Mirroring Ckeditor JS overrides for the CKEditor cmsplugin that 
            # use a different namespace than 'django-ckeditor'
            self.symlink_list.append(('ckeditor', join(project_path, 'mods_available/ckeditor/static/djangocms_text_ckeditor')))

        # Enable all selected mods (it resumes to make a list of symlinks to 
        # do in mods_enabled)
        for name in mods:
            self.symlink_list.append((
                join('..', 'mods_available', name),
                join(project_path, 'mods_enabled', name)
            ))
        
        return self.symlink_list

    def post(self, command, output_dir, vars):
        """
        Do some tasks after install
        """
        if command.simulate:
            return
        
        # Find the 'project/' dir in the created paste project
        project_path = join(getcwd(), vars['project'], 'project')
        
        # 1. Mods
        mods = self.get_mods(project_path, vars)
        
        # 2. Create symlinks
        for target, linkfile in self.get_symlinks(project_path, vars, mods):
            print "* Symlink TO:", target, 'INTO:', linkfile
            symlink(target, linkfile)

        # 3. Git first initialization
        call = Caller(vars['project'])
        call('git', 'init', '.')
        call('git', 'add', '.')
        call('git', 'commit', '-m', 'First commit')
