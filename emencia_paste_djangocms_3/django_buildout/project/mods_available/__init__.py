"""
Below is a list (non-exhaustive) of all the components available to create a new project.

Currently a new project installs the following (at least):

* `google_tools`_;
* `assets`_ to manage the assets;
* `cms`_ for `Django CMS`_;
* `codemirror`_ for the editor used in `Django CMS`_'s *snippet* plugin;
* `filebrowser`_ to manage the media uploaded in the CMS pages;
* `ckeditor`_ for the editor used with `Django CMS`_ and `Django Blog Zinnia`_;

If you do not want to use these components, you will need to manually disable them in your settings and the project's main ``urls.py``.

Also, there is a lot of mods that needs some private key, email adresses, services accounts, etc.. to be filled to works. Like 'contact_form' that needs to know a recipient email where it can send notifications. So after a first install remember to watch your mod settings to see if they need some datas to fill.
"""