#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import smileys

setup(
    name='django-smileys-plus',
    version=smileys.version(),
    description="Easily add, use and manage smileys on your Django-powered site.",
    long_description=open('README.rst', 'r').read(),
    keywords='django, image, smiley, useless, fun',
    author='Josh VanderLinden, Artscoop',
    author_email='artscoop93@gmail.com',
    url='http://bitbucket.org/artscoop/django-smileys/',
    license='BSD',
    package_dir={'smileys': 'smileys'},
    include_package_data=True,
    packages=find_packages(),
    requires=('easy_thumbnails',),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Artistic Software',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics'
    ],
    zip_safe=False
)
