#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: pyneo4jet.py
Author: huxuan - i(at)huxuan.org
Created: 2012-11-25
Last modified: 2012-11-25
Description:
    Main interface for pyneo4jet

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""
import sys

import gevent.monkey
gevent.monkey.patch_all()
from bottle import run, get, post, request, template

try:
    from config import *
except ImportError:
    print '[Error] config.py is NEEDED! Refer to config-sample.py'
    sys.exit(1)

@get('/')
def login_or_timeline_get():
    """
    Check whether user has login
    show the timeline if is
    show login otherwise
    """
    pass

@post('/')
def login_post():
    """
    Check whether post the corresponding username and password
    """
    pass

@get('/register/')
def register_get():
    """
    Show the form for register

    Note:
        Currently INVITATION_CODE is NEEDED!
    """
    pass

@post('/register/')
def register_post():
    """
    Add a new account

    Note:
        Need to check whether username, avatar and INVITATION_CODE is valid
        avatar could be optional but should have default value
    """
    pass

@get('/profile/')
def profile_get():
    """
    Show form of profile with subbmit button which can change it.
    """
    pass

@post('/profile/')
def profile_post():
    """
    Update profile and redirect to get page
    """
    pass

@get('/tweet/')
def tweet_get():
    """
    Show an empty form for tweet
    """
    pass

@post('/tweet/')
def tweet_post():
    """
    Add a new tweet
    """
    pass

@get('/user/<username>')
def user_get():
    """
    Show user's profile and tweets as well as follow link or followed status.
    """
    pass

@get('/user/<username>/friends/')
def user_firends_get():
    """
    Show list for user's friends
    """
    pass

def main():
    """Parse the args and run the server"""
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        port = sys.argv[1]
    else:
        port = 8888
    run(server='gevent', host='0.0.0.0', port=port, quiet=True, fast=True)

if __name__ == '__main__':
    main()
