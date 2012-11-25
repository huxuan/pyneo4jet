"""
File: tweet.py
Author: huxuan - i(at)huxuan.org
Created: 2012-11-25
Last modified: 2012-11-25
Description:
    Description for tweet.py

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

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
