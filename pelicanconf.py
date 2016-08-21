#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ihommani'
SITENAME = u'Thinking about...'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Use pelican-themes -l to list available themes
THEME = "Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('prendre un café', 'https://nicolas.perriault.net/'),
          ('videlalvaro.github.com', 'http://videlalvaro.github.io'), 
          )

########PLUGINS#########
PLUGIN_PATH = "~/Github/pelican-plugins"
PLUGINS = ["summary", 'optimize_images']


# Social widget
# Adding social links wich will appear in the footer
SOCIAL = (('twitter', 'http://twitter.com/ihommani'),
                    ('github', 'http://github.com/ihommani'),
                    ('flickr', 'http://www.flickr.com/photos/chaiyachaiya/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Specifying special content directories for linking internal contents
STATIC_PATHS = ['images']

#This is to suround code with a css class 'pgcss', and to automatically display lineNumber
PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
PYGMENT_STYLE = 'vim'

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

#To show gitHub ribbon
GITHUB_URL = 'https://github.com/ihommani'

DISQUS_SITENAME = 'ihommani'
