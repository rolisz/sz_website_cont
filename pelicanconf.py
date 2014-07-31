#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import getenv

AUTHOR = u'Szab\xf3 Tibor'
SITENAME = u'SzCont Consulting'
SITEURL = getenv('SITE_URL', 'http://rolisz.github.io/szcont')
print SITEURL
THEME = './pelican-bootstrap3'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'ro'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_ATOM = None
FEED_RSS = None

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

DIRECT_TEMPLATES = ('index', 'contact')

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS = ['i18n_subsites']
I18N_SUBSITES = {
    'ro': {
        'SITENAME': 'SzCont Consulting',
    },
    'en': {
        'SITENAME': 'SzCont Consulting',
    },
    'hu': {
        'SITENAME': 'SzCont Consulting',
    }
}
# Social widget
SOCIAL = None
HIDE_SIDEBAR = True
USE_OPEN_GRAPH = False
BOOTSTRAP_THEME = 'readable'

STATIC_PATHS = ['./images/', 'css']
CUSTOM_CSS = 'css/custom.css'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
