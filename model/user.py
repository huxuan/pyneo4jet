"""
File: user.py
Author: huxuan
E-mail: i(at)huxuan.org
Created: 2012-11-25
Last modified: 2012-11-25
Description:
    Description for user.py

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

class User(object):
    """Wrap of all actions related to User

    Attributes:
        args: Description of args
    """
    def __init__(self, *args, **kwargs):
        """Init User"""
        super(User, self).__init__(*args, **kwargs)

    @staticmethod
    def add(self, username, avatar_url=''):
        """
        Add a user with username and avatar_url

        :param username: the username of the user
        :type username: string
        :param avatar_url: the url of user's avatar
        :type avatar: string
        """
        pass

    @staticmethod
    def get(self, username):
        """
        get a user by username

        :param username: the username of the user
        :type username: string
        """
        pass

    def get_friends(self, username, index=0, amount=10):
        """
        get a user's friends by username

        :param username: the username of the user
        :type username: string
        :param index: the begin index of friends to be shown, default to 1
        :type index: int
        :param index: the amount of friends to be shown, default to 10
        :type index: int
        """
        pass

    def get_tweets(self, username, index=0, amount=10):
        """
        get a user's tweets by username

        :param username: the username of the user
        :type username: string
        :param index: the begin index of tweets to be shown, default to 1
        :type index: int
        :param index: the amount of tweets to be shown, default to 10
        :type index: int
        """
        pass
