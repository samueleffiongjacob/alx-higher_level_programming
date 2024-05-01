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
# install venv and start
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate

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

# Install MySQLdb module version 2.0.x
# databae on linux must always be startup
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient

$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)

# Install SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
# start up mysql service
$  service mysql start  
sudo mysql -u root # I had to use "sudo" since it was a new installation

mysql> USE mysql;
mysql> SELECT User, Host, plugin FROM mysql.user;

+------------------+-----------------------+
| User             | plugin                |
+------------------+-----------------------+
| root             | auth_socket           |
| mysql.sys        | mysql_native_password |
| debian-sys-maint | mysql_native_password |
+------------------+-----------------------+



# On some systems, like Ubuntu, MySQL is using the Unix auth_socket plugin by default.

# Basically it means that: db_users using it, will be "authenticated" by the system user credentials. You can see if your root user is set up like this by doing the following:

$ sudo mysql -u root # I had to use "sudo" since it was a new installation

mysql> USE mysql;
mysql> SELECT User, Host, plugin FROM mysql.user;

+------------------+-----------------------+
| User             | plugin                |
+------------------+-----------------------+
| root             | auth_socket           |
| mysql.sys        | mysql_native_password |
| debian-sys-maint | mysql_native_password |
+------------------+-----------------------+

# As you can see in the query, the root user is using the auth_socket plugin.

# There are two ways to solve this:

    #You can set the root user to use the mysql_native_password plugin
    #You can create a new db_user with you system_user (recommended)
$ sudo service mysql restart


#Option 1:
$ sudo mysql -u root # I had to use "sudo" since it was a new installation

mysql> USE mysql;
mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
mysql> FLUSH PRIVILEGES;
mysql> exit;

# Option 2: (replace YOUR_SYSTEM_USER with the username you have)
$ sudo mysql -u root # I had to use "sudo" since it was a new installation

mysql> USE mysql;
mysql> CREATE USER 'YOUR_SYSTEM_USER'@'localhost' IDENTIFIED BY 'YOUR_PASSWD';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'YOUR_SYSTEM_USER'@'localhost';
mysql> UPDATE user SET plugin='auth_socket' WHERE User='YOUR_SYSTEM_USER';
mysql> FLUSH PRIVILEGES;
mysql> exit;

$ sudo service mysql restart
```
