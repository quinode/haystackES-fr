#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup



VERSION = __import__('haystack_fr').__version__


setup(
    name ='haystackES-fr',
    version = '0.1.0',
    author = 'Claude Huchet',
    author_email = 'contact@quinode.fr',
    packages = [
        'haystack_fr',
        'haystack_fr.backends',
    ],
    install_requires = ['haystack'],
    url = 'https://github.com/quinode/haystachES-fr',
    download_url = 'https://github.com/quinode/haystachES-fr/tarball/master',

    license = 'README.me',
    description = 'A french haystack backend for ElasticSearch',
    long_description = open('README.md').read(),
)
