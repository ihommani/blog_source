#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

RELATIVE_URLS = False
SITEURL = 'https://ihommani.github.io'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#GOOGLE_ANALYTICS = ""
GOSQUARED_SITENAME = 'GSN-556406-R'
PLUGINS = ["summary", 'optimize_images', 'gravatar']

GITHUB_USER = 'ihommani'

# SOCIAL 
TWITTER_USERNAME = 'ihommani'
TWITTER_WIDGET_ID = "452570615828856832"
DISQUS_SITENAME = 'ihommani'
