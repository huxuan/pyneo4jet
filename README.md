# pyneo4jet

A really simpilified version for tweet based on neo4j written in python.

## Why named pyneo4jet?

Just a combination of prefix of python, neo4j and suffix of tweet.

## What is neo4j?

Neo4j is a high-performance, NOSQL graph database with all the features of
a mature and robust database [1]. For more information, refer to the
[official site](http://neo4j.org/).

## What is required?

### dev packages

- python-dev
- libevent-dev

In Ubuntu/Debian, they can be easily intalled by command

```shell
sudo apt-get install python-dev libevent-dev
```

### python third part modules
- bottle
- gevent

You can easily install all requirements via pip by command

```shell
sudo pip install -r requirements.txt --upgrade
```

## How to run it?

After installing requirements, you can easily run it by command

```shell
python /path/to/pyneo4jet.py [port_number]
```

- **/path/to/pyneo4jet.py** is the path to the file pyneo4jet.py
- **[port_number]** is the port number to run the application which is optional
  and defaults to 8888

## How to begin develop? (For Collaborators Only)

### Workflow

```shell
0 git clone git@github.com:huxuan/pyneo4jet.git
1 cd pyneo4jet
2 sudo apt-get install python-dev libevent-dev
3 sudo pip install -r requirements.txt --upgrade
# Only need to do step 0 to step 4 once
4 git pull
# make some changes
5 git diff # Check the code changes, ensure whole app runnable
6 git add filename # if a new file named filename created, repeat if more
7 git commit -a -m 'Description about this change'
# repeat from step 4 to step 7
8 git push # When a whole new function has been implemented
```

### Some tips:

- Commit Early, Commit Often. [2]
- Every work should begin will `git pull`.
- Commit/Push with cautious, MUST ensure whole app runnable.

## Material

- [Official python embedded installation guide](http://docs.neo4j.org/chunked/stable/python-embedded-installation.html)
- [Official Hello World python embedded examples](http://docs.neo4j.org/chunked/stable/tutorials-python-embedded.html)
- [Official more detailed doc for python embedded](http://docs.neo4j.org/chunked/stable/python-embedded.html)
- <del>[Official python-embedded application example](https://github.com/neo4j-examples/python-shop-categories)</del>
  (Deprecated for haven't been updated for 3 years!)
- [Bottle Tutorial](http://bottlepy.org/docs/stable/)
- [SimpleTemplate Engine](http://bottlepy.org/docs/stable/stpl.html)

[1]: http://neo4j.org/
[2]: http://sethrobertson.github.com/GitBestPractices/#commit
