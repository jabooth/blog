#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

# Avoid having hard coded paths to these files
base_path = os.path.dirname(os.path.realpath(__file__))
THEME = '{}/themes/pelican-responsive/responsive'.format(base_path)

AUTHOR = u'James Booth'
SITENAME = u'jabooth.github.io'
SITEURL = 'http://jabooth.github.io'
MINI_BIO = u"PhD Candidate at Imperial College London"
BIO = u'<strong>James Booth</strong> has some sort of BIO text'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/jabooth', '&#xe037;'),
    ('Google Plus', 'https://plus.google.com/+JamesBoothUK', '&#xe039;'),
    ('Twitter', 'https://twitter.com/jamesabooth', '&#xe086;'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


PLUGIN_PATH = 'plugins'
PLUGINS = ['liquid_tags.notebook', 'liquid_tags.include_code']
LIQUID_TAGS_IPYTHON_STYLES = open('_nb_header.html').read().decode('utf-8')

PATH = '{}/content'.format(base_path)
# all these are copied into the output folder
STATIC_PATHS = ['images', 'code', 'notebooks', 'theme/img/avatar.jpg']

