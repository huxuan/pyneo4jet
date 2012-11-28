#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: parser.py
Author: huxuan - i(at)huxuan.org
Created: 2012-11-26
Last modified: 2012-11-28
Description:
    The parser of database

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

import re

from model import User

INFO_PATTERN = re.compile('"([^"]+)"')

KEYS = (
    'id', 'username', 'joined', 'species', 'coloring', 'gender', 'birthday',
    'age', 'hometown', 'favorite_toy', 'favorite_activity', 'favorite_food',
)

def main():
    """docstring for main"""
    username_list = {}

    data = file('data/petster-hamster/ent.petster-hamster')
    for item in data.readlines():
        if not item.startswith('%'):
            res = INFO_PATTERN.findall(item)
            info = dict(zip(KEYS, res))
            username_list[info['id']] = info['username']
            user = User(info)
            user.add()
    data.close()

    data = file('data/petster-hamster/out.petster-hamster')
    for item in data.readlines():
        # print repr(item)
        # raw_input()
        if not item.startswith('%'):
            uid1, uid2 = item.strip().split(' ')
            # print repr(uid1), repr(uid2)
            # raw_input()
            username1 = username_list[uid1]
            username2 = username_list[uid2]
            user1 = User.get(username1)
            user2 = User.get(username2)
            user1.follow(username2)
            user2.follow(username1)
    data.close()

if __name__ == '__main__':
    main()
