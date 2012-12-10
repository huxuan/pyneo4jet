"""
File: user.py
Author: huxuan - i(at)huxuan.org
        Meryl - panwanqiong(at)pku.edu.cn
Created: 2012-11-25
Last modified: 2012-12-07
Description:
    models used in pyneo4jet

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

from config import INVITATION_CODE

from database import GRAPHDB as db
from database import USER_IDX as user_idx
from database import TWEET_IDX as tweet_idx
from database import TWEET_REF as tweet_ref

class User(object):
    """Wrap of all actions related to User

    :param username: the username of the user
    :type username: string
    """
    def __init__(self, username, password=None):
        """Init User"""
        self.username = username
        self.password = password

    @staticmethod
    def add(username, password, password_confirm, invitation):
        """
        Add a user to neo4j database

        :rtype: true or false indicates the result of add action

        Note:
            Before add there needs a check!
        """
        if not username or not password or not password_confirm:
            return False, 'The username/password should not be empty!'
        if password != password_confirm:
            return False, 'The password you input twice is not the same!'
        if invitation != INVITATION_CODE:
            return False, 'The invitation code is invalid!'
        user_node = user_idx['username'][username].single
        if user_node:
            return False, 'The username %s has been used!' % username
        user = User(username, password)
        with db.transaction:
            user_node = db.node()
            user_node['username'] = user.username
            user_node['password'] = user.password
            user_idx['username'][username] = user_node
        return True, ''

    @staticmethod
    def get(username):
        """
        get a user by username

        :param username: the username of the user
        :type username: string
        :rtype: instance of user
        """
        user = User(username)
        user_node = user_idx['username'][username].single
        user.password = user_node['password']
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
        user_node = user_idx['username'][username].single
        if not user_node:
            return False, 'User does not exist!'
        if user_node['password'] != password:
            return False, 'Invalid password!'
        return True, ''

    def update(self, username):
        """
        Update a user's profile with username

        :param username: the username of the user
        :type username: string
        :rtype: true or false indicated the result of update action

        Notes:
            Before update there needs a check!
        """
        # NOTE(huxuan): There still exists bug here for deletion in index
        if not username:
            return False, 'The username should not be empty!'
        user_node = user_idx['username'][self.username].single
        if not user_node:
            return False, 'User does not exist!'
        with db.transaction:
            user_idx['username'][self.username].single.delete()
            self.username = username
            user_node['username'] = username
            user_idx['username'][username] = user_node
        return True, ''

    def update_password(self, old_pw, new_pw1, new_pw2):
        """
        Update a user's password

        :param old_pw: old password
        :type old_pw: string
        :param new_pw1: new password
        :type new_pw1: string
        :param new_pw2: new password for comfirm
        :type new_pw2: string
        :rtype: true of false indicate the result and more specific msg
        """
        user_node = user_idx['username'][self.username].single
        if not user_node:
            return False, 'User does not exist!'
        if user_node['password'] != old_pw:
            return False, 'Wrong old password!'
        if new_pw1 != new_pw2:
            return False, 'The new passwords do not match!'
        with db.transaction:
            user_node['password'] = new_pw1
        return True, ''

    def isfollow(self, username):
        """
        Check whether user has followed user called username

        :param username: the username of the person to follow
        :type username: string
        :rtype: true or false indicates the relationship
        """
        user_node = user_idx['username'][self.username].single
        for rel in user_node.FOLLOW.outgoing:
            f_node = rel.end
            if f_node['username'] == username:
                return True
        return False

    def follow(self, username):
        """
        A user follow one person named username

        :param username: the username of the person to follow
        :type username: string
        :rtype: true or false indicates the result of follow action
        """
        user_node = user_idx['username'][self.username].single
        for rel in user_node.FOLLOW.outgoing:
            f_node = rel.end
            if f_node['username'] == username:
                return False, 'You have already followed %s !' % username
        follow_user = user_idx['username'][username].single
        with db.transaction:
            user_node.FOLLOW(follow_user)
        return True

    def unfollow(self, username):
        """
        A user unfollow one person named username

        :param username: the username of the person to unfollow
        :type username: string
        :rtype: true or false indicates the result of unfollow action
        """
        user_node = user_idx['username'][self.username].single
        with db.transaction:
            for rel in user_node.FOLLOW.outgoing:
                f_node = rel.end
                if f_node['username'] == username:
                    rel.delete()
                    return True, 'Unfollowed user %s successfully !' % username
        return False, 'You haven\'t follow %s yet !' % username

    def get_followers(self, index=0, amount=10):
        """
        get a user's followers by username

        :param index: the begin index of followers to be shown, default to 1
        :type index: int
        :param index: the amount of followers to be shown, default to 10
        :type index: int
        :rtype: list of followers/user instances
        """
        user_from = user_idx['username'][self.username].single
        users_list = []
        for relationship in user_from.FOLLOW.incoming:
            user_to = relationship.start
            user = User('','')
            user.username = user_to['username']
            user.password = user_to['password']
            users_list.append(user)
        return users_list[index : min(index+amount, len(users_list))]

    def get_following(self, index=0, amount=10):
        """
        get a user's following by username

        :param index: the begin index of following to be shown, default to 1
        :type index: int
        :param index: the amount of following to be shown, default to 10
        :type index: int
        :rtype: list of following/user instances
        """
        user_from = user_idx['username'][self.username].single
        users_list = []
        for relationship in user_from.FOLLOW.outgoing:
            user_to = relationship.end
            user = User('','')
            user.username = user_to['username']
            user.password = user_to['password']
            users_list.append(user)
        return users_list[index : min(index+amount, len(users_list))]

    def get_tweets(self, index=0, amount=10):
        """
        get a user's tweets by username

        :param index: the begin index of tweets to be shown, default to 1
        :type index: int
        :param index: the amount of tweets to be shown, default to 10
        :type index: int
        :rtype: list of tweet instances
        """
        user_from = user_idx['username'][self.username].single
        tweets_list = []
        for relationship in user_from.SEND.incoming:
            tweet_node = relationship.start
            tweet = Tweet()
            tweet.text = tweet_node['text']
            tweet.username = tweet_node.SEND.outgoing.single.end['username']
            tweet.created_at = tweet_node['created_at']
            tweet.tid = tweet_node['tid']
            tweets_list.append(tweet)
        return tweets_list[index : min(index + amount, len(tweets_list))]

    def get_timeline(self, index=0, amount=10):
        """
        get timeline items

        :param index: the begin index of tweets to be shown, default to 1
        :type index: int
        :param index: the amount of tweets to be shown, default to 10
        :type index: int
        :rtype: list of tweet instances shown in the timeline
        """
        tweets_list = []
        user_node = user_idx['username'][self.username].single
        for follow_rel in user_node.FOLLOW.outgoing:
            follow_node = follow_rel.end
            follow = User(follow_node['username'])
            for send_rel in follow_node.SEND.incoming:
                tweet_node = send_rel.start
                tweet = Tweet.get(tweet_node['tid'])
                tweets_list.append(tweet)
        for rel in user_node.SEND.incoming:
            tweet_node = rel.start
            tweet = Tweet.get(tweet_node['tid'])
            tweets_list.append(tweet)
        tweets_list.sort(key=lambda tweet: tweet.created_at, reverse=True)
        return tweets_list[index : min(index + amount, len(tweets_list))]

class Tweet(object):
    """Wrap of all actions related to Tweet

    :param text: the text of tweet
    :type text: string
    :param created_at: the time created the tweet
    :type created_at: datetime
    """
    def __init__(self, text='', created_at='', tid=0):
        """Init Tweet"""
        self.username = None
        self.text = text
        self.created_at = created_at
        self.tid = tid

    @staticmethod
    def get(tid):
        """
        get a tweet by tid

        :param tid: the id of the tweet
        :type tid: int
        :rtype: instance of tweet
        """
        tweet = Tweet()
        tweet_node = tweet_idx['tid'][tid].single
        if tweet_node:
            tweet.username = tweet_node.SEND.outgoing.single.end['username']
            tweet.text = tweet_node['text']
            tweet.created_at = tweet_node['created_at']
            tweet.tid = tweet_node['tid']
            return tweet

    @staticmethod
    def add(username, text, created_at):
        """
        Add a tweet to neo4j database

        :rtype: true or false indicates the result of add action

        Note:
            Before add there needs a check!
        """
        if text:
            with db.transaction:
                tweet_node = db.node()
                tweet_node['text'] = text
                tweet_node['created_at'] = created_at
                user_node = user_idx['username'][username].single
                tweet_node.SEND(user_node)
                tid = tweet_ref['tot_tweet']
                tweet_node['tid'] = tid
                tweet_ref['tot_tweet'] = tweet_ref['tot_tweet'] + 1
                tweet_idx['tid'][tid] = tweet_node
            return True, ''
        else:
            return False, 'Tweet should not be empty!'

    def remove(self):
        """
        Remove a tweet from neo4j database

        :rtype: true or false indicates the result of remove action
        """
        tweet_node = tweet_idx['tid'][self.tid].single
        if not tweet_node:
            return False, 'The tweet does not exist!'
        with db.transaction:
            for rel in tweet_node.SEND:
                rel.delete()
            tweet_idx['tid'][self.tid].single.delete()
        return True, ''
