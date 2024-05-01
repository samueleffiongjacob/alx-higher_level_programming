# Python - Object-relational mapping

At the end of this project, I am expected to be able to explain to anyone, without the help of Google:

    Why Python programming is awesome
    How to connect to a MySQL database from a Python script
    How to SELECT rows in a MySQL table from a Python script
    How to INSERT rows in a MySQL table from a Python script
    What ORM means
    How to map a Python Class to a MySQL table

## REsource

- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)

- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)

- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)

- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)

- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)

- [Introduction to SQLAlchemy vedio](https://www.youtube.com/watch?v=woKYyhLCcnU)

- [Flask SQLAlchemy vedio](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)

- [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)

- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)

- [SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)

- [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

```bash
# to start venv on windows
$ mkdir client-old
$ cd client-old
$ python -m venv venv --prompt="client-old"
$ venv\Scripts\activate
(client-old) PS> python -m pip install django==2.2.26
(client-old) PS> python -m pip list
    Package    Version
    ---------- -------
    Django     2.2.26
    pip        22.0.4
    pytz       2022.1
    setuptools 58.1.0
    sqlparse   0.4.2
# to deactivate
(client-old) deactivate


# on git bash
$ $ mkdir client-old
$ cd client-old
$ python3 -m venv venv --prompt="client-old"
$ cd venv 
$ source venv/bin/activate
# or 
# /Scripts/activate
(client-old) $ python -m pip install django==2.2.26
(client-old) $ python -m pip list
Package    Version
---------- -------
Django     2.2.26
pip        22.0.4
pytz       2022.1
setuptools 58.1.0
sqlparse   0.4.2
# to deactvate
(client-old) deactivate

# databae on linux must always be startup
$  service mysql start  

```
