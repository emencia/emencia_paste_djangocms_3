
.PHONY: help install clean delpyc assets scss syncf5

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install -- to proceed to a new install of this project. Use clean command before if you want to reset a current install"
	@echo "  clean  -- to clean your local repository from all stuff created by buildout and instance usage"
	@echo "  delpyc  -- to remove all *.pyc files, this is recursive from the current directory"
	@echo
	@echo "  assets -- to minify all assets and collect static files"
	@echo "  scss -- to compile all SCSS stuffs with compass"
	@echo "  syncf5 -- to synchronize needed Javascript files from foundation5 sources dir to the project static files"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc 
	rm -Rf bin include eggs lib parts django-apps-src develop-eggs local .installed.cfg compass/.sass-cache project/webapp_statics/.webassets-cache

syncf5:
	rm -Rf project/webapp_statics/js/foundation5
	cp -r foundation5/bower_components/foundation/js project/webapp_statics/js/foundation5
	# Cleaning vendor libs
	rm -Rf project/webapp_statics/js/foundation5/vendor
	mkdir -p project/webapp_statics/js/foundation5/vendor
	# Getting the real sources for updated vendor libs
	cp foundation5/bower_components/fastclick/lib/fastclick.js project/webapp_statics/js/foundation5/vendor/
	cp foundation5/bower_components/jquery/dist/jquery.js project/webapp_statics/js/foundation5/vendor/
	cp foundation5/bower_components/jquery-placeholder/jquery.placeholder.js project/webapp_statics/js/foundation5/vendor/
	cp foundation5/bower_components/jquery.cookie/jquery.cookie.js project/webapp_statics/js/foundation5/vendor/
	cp foundation5/bower_components/lodash/dist/lodash.js project/webapp_statics/js/foundation5/vendor/
	cp foundation5/bower_components/modernizr/modernizr.js project/webapp_statics/js/foundation5/vendor/

assets:
	django-instance collectstatic --pythonpath=project/ --noinput
	django-instance assets build --pythonpath=project/
	django-instance collectstatic --pythonpath=project/ --noinput

scss:
	compass compile -c compass/config.rb compass/

install:
	virtualenv --no-site-packages --setuptools .
	bin/pip install --upgrade setuptools
	# Must upgrade PIP to 1.4 because of "nap"
	bin/pip install --upgrade pip
	mkdir -p eggs
	bin/python bootstrap.py
	bin/buildout -v
	bin/django-instance syncdb --all
	bin/django-instance migrate --fake
