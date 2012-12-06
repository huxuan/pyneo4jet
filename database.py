#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: database.py
Author: huxuan - i(at)huxuan.org
Created: 2012-11-28
Last modified: 2012-11-30
Description:
    Actions related to database only

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

from neo4j import GraphDatabase

from config import DBNAME

GRAPHDB = GraphDatabase(DBNAME)

if GRAPHDB.node.indexes.exists('user'):
    USER_IDX = GRAPHDB.node.indexes.get('user')
else:
    USER_IDX = GRAPHDB.node.indexes.create('user')

if GRAPHDB.node.indexes.exists('tweet'):
    TWEET_IDX = GRAPHDB.node.indexes.get('tweet')
else:
    TWEET_IDX = GRAPHDB.node.indexes.create('tweet')

TWEET_REF_ID = 1000000
if len(TWEET_IDX['tid'][TWEET_REF_ID]) == 0:
    with GRAPHDB.transaction:
        TWEET_REF = GRAPHDB.node()
        TWEET_REF['tot_tweet'] = 0
        TWEET_IDX['tid'][TWEET_REF_ID] = TWEET_REF
TWEET_REF = TWEET_IDX['tid'][TWEET_REF_ID].single
