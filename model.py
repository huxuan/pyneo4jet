"""
File: user.py
Author: huxuan - i(at)huxuan.org
        Meryl - panwanqiong(at)pku.edu.cn
Created: 2012-11-25
Last modified: 2012-11-29
Description:
    models used in pyneo4jet

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

from neo4j import GraphDatabase

from config import DBNAME, INVITATION_CODE

class User(object):
    """Wrap of all actions related to User

    :param username: the username of the user
    :type username: string
    """
    def __init__(self, username='',avatar_url='',password='123'):
        """Init User"""
        self.username = username
		self.avatar_url = avatar_url
		self.password = password
		self.user_node =''

    @staticmethod
    def get(username):
        """
        get a user by username

        :param username: the username of the user
        :type username: string
        :rtype: instance of user
        """
		user_idx = db.node.indexes.get('users')
		user = User()
		user.username = username
		user.user_node = user_idx['username'][username]
		user.avatar_url = user.user_node.avatar_url
		user.password = user.user_node.password
		return user

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

    @staticmethod
    def add(username, password, password_confirm, invitation):
        """
        Add a user to neo4j database

        :rtype: true or false indicates the result of add action

        Note:
            Before add there needs a check!
        """
        pass

    def update(self, username):
        """
        Update a user's profile with username

        :param username: the username of the user
        :type username: string
        :rtype: true or false indicated the result of update action

        Notes:
            Before update there needs a check!
        """
        pass

    def follow(self, username):
        """
        A user follow one person named username

        :param username: the username of the person to follow
        :type username: string
        :rtype: true or false indicates the result of follow action
        """
        pass

    def unfollow(self, username):
        """
        A user unfollow one person named username

        :param username: the username of the person to unfollow
        :type username: string
        :rtype: true or false indicates the result of unfollow action
        """
        pass

    def get_followers(self, index=0, amount=10):
        """
        get a user's followers by username

        :param index: the begin index of followers to be shown, default to 1
        :type index: int
        :param index: the amount of followers to be shown, default to 10
        :type index: int
        :rtype: list of followers/user instances
        """
        pass

    def get_following(self, index=0, amount=10):
        """
        get a user's following by username

        :param index: the begin index of following to be shown, default to 1
        :type index: int
        :param index: the amount of following to be shown, default to 10
        :type index: int
        :rtype: list of following/user instances
        """
        pass

    def get_tweets(self, index=0, amount=10):
        """
        get a user's tweets by username

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
    def __init__(self, username, text, created_at):
        """Init Tweet"""
        self.username = username
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

    def remove(self):
        """
        Remove a tweet from neo4j database

        :rtype: true or false indicates the result of remove action
        """
        pass
