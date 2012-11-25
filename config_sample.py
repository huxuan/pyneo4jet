"""
File: config-sample.py
Author: huxuan - i(at)huxuan.org
Created: 2012-11-25
Last modified: 2012-11-25
Description:
    Sample for config.py
    Mostly for some global variables

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

# VERSION should be development or production to judge
# whether to deploy for test or not
VERSION = 'development | production'

# INVITATION_CODE is needed currently for register
INVITATION_CODE = 'whatever_you_want'

# COOKIES_SECRET is used to sign cookies in bottle
COOKIES_SECRET = 'whatever_you_want'
