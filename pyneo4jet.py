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
    from config import VERSION, INVITATION_CODE, COOKIES_SECRET
except ImportError:
    print '[Error] config.py is NEEDED! Refer to config-sample.py'
    sys.exit(1)

from model import User, Tweet

@get('/')
def login_or_timeline_get():
    """
    Check whether user has login
    show the timeline if is
    show login otherwise

    :rtype: timeline page if already signed in, login page otherswise
    """
    return 'GET /'

@post('/')
def login_post():
    """
    Check whether post the corresponding username and password

    :rtype: login page with form
    """
    return 'POST /'

@get('/register/')
def register_get():
    """
    Show the form for register

    :rtype: register page with form

    Note:
        Currently INVITATION_CODE is NEEDED!
    """
    return 'GET /register/'

@post('/register/')
def register_post():
    """
    Add a new account

    :rtype: login page if success, register page with error info otherwise

    Note:
        Need to check whether username, avatar and INVITATION_CODE is valid
        avatar could be optional but should have default value
    """
    return 'POST /register/'

@get('/profile/')
def profile_get():
    """
    Show form of profile with subbmit button which can change it.

    :rtype: user's profile page
    """
    return 'GET /profile/'

@post('/profile/')
def profile_post():
    """
    Update profile and redirect to get page

    :rtype: user's profile page
    """
    return 'POST /profile/'

@get('/tweet/')
@get('/tweet/<index:int>')
def tweet_get(index=0):
    """
    Show an empty form for tweet

    :param index: the begin index of tweets to be shown, default to 0
    :type index: int
    :rtype: tweets page shown with corresponding tweets
    """
    return 'GET /tweet/%d' % index

@post('/tweet/')
def tweet_post():
    """
    Add a new tweet

    :rtype: timeline page with result of post
    """
    return 'POST /tweet/'

@get('/user/<username>')
def user_get(username):
    """
    Show user's profile and tweets as well as follow link or followed status.

    :param username: username of the user
    :type username: string
    :rtype: profile page of the user
    """
    return 'GET /user/%s' % username

@get('/user/<username>/friends/')
@get('/user/<username>/friends/<index:int>')
def user_firends_get(username, index=0):
    """
    Show list for user's friends

    :param username: username of the user
    :type username: string
    :param index: the begin index of friends list, default to 0
    :type index: int
    :rtype: friends list page of corresponding user and friends
    """
    return 'GET /user/%s/friends/%d' % (username, index, )

def main():
    """Parse the args and run the server"""

    bottle.debug(VERSION == 'development')

    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        port = sys.argv[1]
    else:
        port = 8888
    run(server='gevent', host='0.0.0.0', port=port, quiet=True, fast=True)

if __name__ == '__main__':
    main()
