#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: parser.py
Author: huxuan - i(at)huxuan.org
Created: 2012-11-26
Last modified: 2012-12-10
Description:
    The parser of database

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""

import re
import datetime

from model import User, Tweet, db
from config import INVITATION_CODE

INFO_PATTERN = re.compile('"([^"]+)"')

KEYS = (
    'username', 'name', 'joined', 'species', 'coloring', 'gender', 'birthday',
    'age', 'hometown', 'favorite_toy', 'favorite_activity', 'favorite_food',
)

def main():
    """docstring for main"""

    data = file('data/petster-hamster/ent.petster-hamster')
    for item in data.readlines():
        item = item.decode('utf8')
        # print repr(item)
        # print type(item)
        # print item
        if not item.startswith('%'):
            res = INFO_PATTERN.findall(item)
            info = dict(zip(KEYS, res))
            print info['username']
            res, user = User.add(
                username=info['username'],
                password='pyneo4jet%s' % info['username'],
                password_confirm='pyneo4jet%s' % info['username'],
                invitation=INVITATION_CODE,
            )
            user.update(
                name=info['name'],
                gender=info['gender'],
                hometown=info['hometown'],
            )
            for key in KEYS:
                res, msg = Tweet.add(info['username'],
                    'My %s is %s' % (key, info[key]),
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                )
                if not res:
                    print msg
                    print key
                    print info[key]
                    raw_input()
    data.close()

    data = file('data/petster-hamster/out.petster-hamster')
    for item in data.readlines():
        # print repr(item)
        # raw_input()
        if not item.startswith('%'):
            username1, username2 = item.strip().split(' ')
            print username1, username2
            # raw_input()
            user1 = User.get(username1)
            user2 = User.get(username2)
            if user1 and user2:
                if (int(username1) + int(username2)) % 2 == 0:
                    res, msg = user2.follow(username1)
                else:
                    res, msg = user1.follow(username2)
                if not res:
                    print msg
                    raw_input()
    data.close()

    db.shutdown()

if __name__ == '__main__':
    main()
