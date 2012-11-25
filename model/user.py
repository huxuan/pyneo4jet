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

    :param username: the username of the user
    :type username: string
    :param avatar_url: the url of user's avatar
    :type avatar: string
    """
    def __init__(self, username, avatar_url=''):
        """Init User"""
        super(User, self).__init__(*args, **kwargs)
        self.username = username
        self.avatar_url = avatar_url

    @staticmethod
    def get(self, username):
        """
        get a user by username

        :param username: the username of the user
        :type username: string
        :rtype: instance of user
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
