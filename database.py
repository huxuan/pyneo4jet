#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: database.py
Author: huxuan - i(at)huxuan.org
Created: 2012-11-28
Last modified: 2012-11-28
Description:
    Actions related to database only

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

from neo4j import GraphDatabase

from config import DBNAME

def indexs_create():
    """
    Create indexs for database
    """
    db = GraphDatabase(DBNAME)
    with db.transaction:
        user_idx = db.node.indexes.create('users')
        tweet_idx = db.node.indexes.create('tweets')
    db.shutdown()
