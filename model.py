"""
File: user.py
Author: huxuan - i(at)huxuan.org
Created: 2012-11-25
Last modified: 2012-11-25
Description:
    models used in pyneo4jet

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

class User(object):
    """Wrap of all actions related to User

    :param username: the username of the user
    :type username: string
    :param avatar_url: the url of user's avatar
    :type avatar: string
    """
    def __init__(self, username, avatar_url=''):
        """Init User"""
        self.username = username
        self.avatar_url = avatar_url

    @staticmethod
    def get(username):
        """
        get a user by username

        :param username: the username of the user
        :type username: string
        :rtype: instance of user
        """
        pass

    @staticmethod
    def auth(username, password):
        """
        Check the authentication of a user

        :param username: the username of a user
        :type username: string
        :param password: the password need to be checked
        :type password: string
        :rtype: true if authentication is ok, false otherwise
        """
        pass

    def add(self):
        """
        Add a user to neo4j database

        :rtype: true or false indicates the result of add action

        Note:
            Before add there needs a check!
        """
        pass

    def update(self, username, avatar_url=''):
        """
        Update a user's profile with username and avatar_url

        :param username: the username of the user
        :type username: string
        :param avatar_url: the url of user's avatar
        :type avatar: string
        :rtype: true or false indicated the result of update action

        Notes:
            Before update there needs a check!
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
        :rtype: list of friends/user instances
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
        :rtype: list of tweet instances
        """
        pass

class Tweet(object):
    """Wrap of all actions related to Tweet

    :param text: the text of tweet
    :type text: string
    :param created_at: the time created the tweet
    :type created_at: datetime
    """
    def __init__(self, text, created_at):
        """Init Tweet"""
        self.text = text
        self.created_at = created_at

    @staticmethod
    def get(tid):
        """
        get a tweet by tid

        :param tid: the id of the tweet
        :type tid: int
        :rtype: instance of tweet
        """
        pass

    def add(self):
        """
        Add a tweet to neo4j database

        :rtype: true or false indicates the result of add action

        Note:
            Before add there needs a check!
        """
        pass
