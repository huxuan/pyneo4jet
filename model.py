"""
File: user.py
Author: huxuan - i(at)huxuan.org
        Meryl - panwanqiong(at)pku.edu.cn
Created: 2012-11-25
Last modified: 2012-12-04
Description:
    models used in pyneo4jet

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

from neo4j import GraphDatabase

from config import DBNAME, INVITATION_CODE

from database import GRAPHDB as db
from database import USER_IDX as user_idx
from database import TWEET_IDX as tweet_idx

from database import TWEET_REF as tweet_ref
"""
tweet_ref is the reference node which contains number of total tweets and is connected to every tweet.
tweet_ref should be initialized as:
    tweet_ref = db.node()
    tweet_ref['tot_tweet'] = 0 (this could be optional)
Every new tweet will be connected as:
    tweet.INSTANCE_OF(tweet_ref)
    tweet.tid = tweet_ref['tot_tweet']+1 (this could be optional)
    tweet_ref['tot_tweet'] = tweet.tid (this could be optional)
"""
class User(object):
    """Wrap of all actions related to User

    :param username: the username of the user
    :type username: string
    """
    def __init__(self, username, password=None, avatar='/images/default.png'):
        """Init User"""
        self.username = username
        self.avatar = avatar
        self.password = password

    @staticmethod
    def add(username, password, password_confirm, invitation):
        """
        Add a user to neo4j database

        :rtype: true or false indicates the result of add action

        Note:
            Before add there needs a check!
        """
        if not username:
            return False, 'The username should not be empty!'
        if not password:
            return False, 'The password should not be empty!'
        if not password_confirm:
            return False, 'The password for confirmation should not be empty!'
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
            user_node['avatar'] = user.avatar
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
        user.avatar = user_node['avatar']
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

    def update(self, username, avatar):
        """
        Update a user's profile with username

        :param username: the username of the user
        :type username: string
        :param avatar: the path of the user's avatar
        :type avatar: string
        :rtype: true or false indicated the result of update action

        Notes:
            Before update there needs a check!
        """
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
        return True, ''

    def isfollow(self, username):
        """
        Check whether user has followed user called username

        :param username: the username of the person to follow
        :type username: string
        :rtype: true or false indicates the relationship
        """
        # NOTE(huxuan): HERE is another more method need to be implemented
        user_node = user_idx['username'][self.username].single
        for rel in user_node.FOLLOW.outgoing:
            f_node = rel.end
            if f_node['username']=username: 
                return True
        return False

    def follow(self, username):
        """
        A user follow one person named username

        :param username: the username of the person to follow
        :type username: string
        :rtype: true or false indicates the result of follow action
        """
        self.user_node = user_idx['username'][self.username].single
        for rel in self.user_node.FOLLOW.outgoing:
            f_node = rel.end
            if f_node['username'] == username:
                return False,'The user '+username+' has been followed by '+self.username+'!'
        follow_user = user_idx['username'][username].single
        with db.transaction:
            self.user_node.FOLLOW(follow_user)
        return True

    def unfollow(self, username):
        """
        A user unfollow one person named username

        :param username: the username of the person to unfollow
        :type username: string
        :rtype: true or false indicates the result of unfollow action
        """
        self.user_node = user_idx['username'][self.username].single
        with db.transaction:
            for rel in self.user_node.FOLLOW.outgoing:
                f_node = rel.end
                if f_node['username'] == username:
                    rel.delete()
                    return True,'The user '+username+' has been unfollowed sucessfully!'
        return False,'The user '+self.username+' does not follow '+username+'!'

    def get_followers(self, index=0, amount=10):
        """
        get a user's followers by username

        :param index: the begin index of followers to be shown, default to 1
        :type index: int
        :param index: the amount of followers to be shown, default to 10
        :type index: int
        :rtype: list of followers/user instances
        """
        self.user_node = user_idx['username'][self.username].single
        user_from = user_idx['username'][self.username].single
        List = []
        for relationship in user_from.FOLLOW.incoming:
            user_to = relationship.start
            user = User()
            user.user_node = user_to
            user.username = user_to['username']
            user.password = user_to['password']
            List.append(user)
        return List[index:min(index+amount,len(List))]

    def get_following(self, index=0, amount=10):
        """
        get a user's following by username

        :param index: the begin index of following to be shown, default to 1
        :type index: int
        :param index: the amount of following to be shown, default to 10
        :type index: int
        :rtype: list of following/user instances
        """
        self.user_node = user_idx['username'][self.username].single
        user_from = user_idx['username'][self.username].single
        List = []
        for relationship in user_from.FOLLOW.outgoing:
            user_to = relationship.end
            user = User()
            user.user_node = user_to
            user.username = user_to['username']
            user.password = user_to['password']
            List.append(user)
        return List[index:min(index+amount,len(List))]

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
        List = []
        for relationship in user_from.SEND.incoming:
            tweet_node = relationship.start
            tweet = Tweet()
            tweet.text = tweet_node['text']
            tweet.username = tweet_node['username']
            tweet.created_at = tweet_node['created_at']
            # NOTE(huxuan): Currently comment it for further discussion
            # tweet.tid = tweet_node['tid']
            List.append(tweet)
        return List[index : min(index + amount, len(List))]

    def get_timeline(self, index=0, amount=10):
        """
        get timeline items

        :param index: the begin index of tweets to be shown, default to 1
        :type index: int
        :param index: the amount of tweets to be shown, default to 10
        :type index: int
        :rtype: list of tweet instances shown in the timeline
        """
        List = []
        last_tweet = tweet_ref['tot_tweet']
        for i in range(last_tweet-index:last_tweet-(index+amout)):
            tweet = Tweet()
            tweet.get(i)
            List.append(tweet)  
        return Lsit

class Tweet(object):
    """Wrap of all actions related to Tweet

    :param text: the text of tweet
    :type text: string
    :param created_at: the time created the tweet
    :type created_at: datetime
    """
    # NOTE(huxuan): Maybe no tid is needed?
    def __init__(self, username='', text='', created_at='',tid=''):
        """Init Tweet"""
        self.username = username
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
        tweet.username = tweet.tweet_node['username']
        tweet.text = tweet.tweet_node['text']
        tweet.created_at = tweet.tweet_node['created_at']
        tweet.tid = tweet.tweet_node['tid']
        return tweet

    @staticmethod
    def add(username, text, created_at):
        """
        Add a tweet to neo4j database

        :rtype: true or false indicates the result of add action

        Note:
            Before add there needs a check!
        """
        # NOTE(huxuan): If tid is needed we should manually generate it
        if text:
            with db.transaction:
                tweet_node = db.node();
                tweet_node['username'] = username
                tweet_node['text'] = text
                tweet_node['created_at'] = created_at
                user_node = user_idx['username'][username].single
                tweet_node.SEND(user_node)
                
                tweet_node.INSTANCE_OF(tweet_ref)
                tweet_node.tid = tweet_ref['tot_tweet'] + 1
                tweet_ref['tot_tweet'] = tweet_ref['tot_tweet'] + 1
                tweet_idx['tid'][tweet_node.tid] = tweet_node
            return True, ''
        else:
            return False, 'Tweet should not be empty!'

    def remove(self):
        """
        Remove a tweet from neo4j database

        :rtype: true or false indicates the result of remove action
        """
        pass
