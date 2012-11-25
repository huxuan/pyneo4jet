# pyneo4jet

A really simpilified version for tweet based on neo4j written in python.

## Why named pyneo4jet?

Just a combination of prefix of python, neo4j and suffix of tweet.

## What is neo4j?

Neo4j is a high-performance, NOSQL graph database with all the features of
a mature and robust database [1]. For more information, refer to the
[official site](http://neo4j.org/).

## requirements

- gevent

You can easily install all requirements via pip by command

```
sudo pip install -r requirements.txt
```

## What does pyneo4jet supported?

- /register/

  > register new account (currently need ivitation code).

- /me/profile/

  > set & view basic profile with username and avatar.

- /me/tweet/

  >  post your tweet.

- /[username]/

  > view your friend's profile and where you can make friends with others

- /[username]/friends/

  > View friend's friends

## Material

- [Official python embedded installation guide](http://docs.neo4j.org/chunked/stable/python-embedded-installation.html)
- [Official Hello World python embedded examples](http://docs.neo4j.org/chunked/stable/tutorials-python-embedded.html)
- [Official more detailed doc for python embedded](http://docs.neo4j.org/chunked/stable/python-embedded.html)
- <del>[Official python-embedded application example](https://github.com/neo4j-examples/python-shop-categories)</del> (Deprecated for haven't been updated for 3 years!)

[1]: http://neo4j.org/
