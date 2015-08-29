#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Massmann'
SITENAME = u'it-spirit'
SITEURL = ''
SITESUBTITLE = u'IT-Consulting & Software Development'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': ('en_US', '%A, %d %b %Y'),
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
GOOGLE_ANALYTICS = u'UA-3549237-1'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/it_spirit'),
    ('Coderwall', 'https://coderwall.com/tmassman'),
    ('Github', 'https://github.com/tmassman'),
    ('Bitbucket', 'https://bitbucket.org/it_spirit'),
    ('LinkedIn', 'http://www.linkedin.com/pub/thomas-massmann/20/393/259'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
