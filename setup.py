from setuptools import setup, find_packages

setup(
    name='emencia_paste_djangocms_3',
    version=__import__('emencia_paste_djangocms_3').__version__,
    description=__import__('emencia_paste_djangocms_3').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='dthenon@emencia.com',
    url='https://github.com/emencia/emencia_paste_djangocms_3',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Paste',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'Paste',
        'PasteDeploy',
        'PasteScript',
    ],
    entry_points={
        'paste.paster_create_template': [
            'djangocms-3 = emencia_paste_djangocms_3.templates:Django',
        ]
    },
    include_package_data=True,
    zip_safe=False
)