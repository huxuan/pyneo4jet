#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: pyneo4jet.py
Author: huxuan - i(at)huxuan.org
Created: 2012-11-25
Last modified: 2012-11-28
Description:
    Main interface for pyneo4jet

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""
import sys

import gevent.monkey
gevent.monkey.patch_all()
from bottle import run, get, post, request, template, redirect

try:
    from config import VERSION, INVITATION_CODE, COOKIES_SECRET
except ImportError:
    print '[Error] config.py is NEEDED! Refer to config-sample.py'
    sys.exit(1)

from model import User, Tweet

@get('/')
def index_get():
    """
    Show signin or signup form according to 'method' param
    If already signed in, redirect to timeline page

    :rtype: login or signup page or redirect to timeline page
    """
    if request.GET.get('method') == 'signup':
        return template('signup')
    else:
        username = request.get_cookie('username', secret=COOKIES_SECRET)
        if username:
            redirect('/%s/timeline/' % username)
        else:
            return template('signin')

@post('/')
def index_post():
    """
    Check validation for SignIn or SignUp

    :rtype: login page with form
    """
    return 'POST /'

@get('/<username>/')
def profile(username):
    """
    Show user's profile with at most recent 10 tweets

    :param username: username of the user
    :type username: string
    :rtype: profile page of the user

    Note:
        Need to check whether authenticated or not
        if so add an profile edit button
        if not follow button or followed status

        Use a 'method' to judge whether to edit the profile
        if is, update button should be shown instead.
    """
    return 'GET /%s/' % username

@post('/<username>/')
def profile_update(username):
    """
    Update user's profile

    :param username: username of the user
    :type username: string
    :rtype: profile page of the user
    """
    return 'POST /%s/' % username

@get('/<username>/timeline/')
@get('/<username>/timeline/<index:int>')
def timeline(username, index=0):
    """
    Show user's timeline

    :param username: username of the user
    :type username: string
    :param index: the begin index of timeline list, default to 0
    :type index: int
    :rtype: timeline page shown
    """
    return 'GET /%s/timeline/%d' % (username, index, )

@get('/<username>/tweets/')
@get('/<username>/tweets/<index:int>')
def tweets(username, index=0):
    """
    Show user's tweets

    :param username: username of the user
    :type username: string
    :param index: the begin index of tweets list, default to 0
    :type index: int
    :rtype: tweets page shown
    """
    return 'GET /%s/tweets/%d' % (username, index, )

@get('/<username>/followers/')
@get('/<username>/followers/<index:int>')
def followers(username, index=0):
    """
    Show user's followers

    :param username: username of the user
    :type username: string
    :param index: the begin index of followers list, default to 0
    :type index: int
    :rtype: followers list page
    """
    return 'GET /%s/followers/%d' % (username, index, )

@get('/<username>/following/')
@get('/<username>/following/<index:int>')
def following(username, index=0):
    """
    Show user's following

    :param username: username of the user
    :type username: string
    :param index: the begin index of following list, default to 0
    :type index: int
    :rtype: following list page
    """
    return 'GET /%s/following/%d' % (username, index, )

def main():
    """Parse the args and run the server"""
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        port = sys.argv[1]
    else:
        port = 8888
    run(server='gevent', host='0.0.0.0', port=port,
        debug=(VERSION != 'production'))

if __name__ == '__main__':
    main()
