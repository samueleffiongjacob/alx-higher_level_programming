# SQL - Introduction

## Tasks

    0. List databases
        0-list_databases.sql: MySQL script that lists all databases.

    1. Create a database
        1-create_database.sql: MySQL script that creates the database hbtn_0c_0.

    2. Delete a database
        2-remove_databases.sql: MySQL script that deletes the database hbtn_0c_0.

    3. List tables
        3-list_tables.sql: MySQL script that lists all tables.

    4. First table
        4-first_table.sql: MySQL script that creates a table first_table.
        Description:
            id: INT
            name: VARCHAR(256)

    5. Full description
        5-full_table.sql: MySQL script that prints the full description of the table first_table.

    6. List all in table
        6-list_values.sql: MySQL script that lists all rows of the table first_table.

    7. First add
        7-insert_value.sql: MySQL script that inserts a new row in the table first_table.
        Description:
            id = 89
            name = Best School

    8. Count 89
        8-count_89.sql: MySQL script that displays the number records with id = 89 in the table first_table.

    9. Full creation
        9-full_creation.sql: MySQL script that creates and fills a table second_table.
        Description:
            id: INT
            name: VARCHAR(256)
            score: INT
        Records:
            id = 1, name = "John", score = 10
            id = 2, name = "Alex", score = 3
            id = 3, name = "Bob", score = 14
            id = 4, name = "George", score = 8

    10. List by best
        10-top_score.sql: MySQL script that lists the score and name of all records of the table second_table in order of descending score.

    11. Select the best
        11-best_score.sql: MySQL script that lists the score and name of all records with a score >= 10 in the table second_table in order of descending score.

    12. Cheating is bad
        12-no_cheating.sql: MySQL script that updates the score of Bob to 10 the table second_table.

    13. Score too low
        13-change_class.sql: MySQL script that removes all records with a score <= 5 in the table second_table.

    14. Average
        14-average.sql: MySQL script that computes the average score of all records in the table second_table.

    15. Number by score
        15-groups.sql: MySQL script that lists the score and number of records with the same score in the table second_table in order of descending count.

    16. Say my name
        16-no_link.sql: MySQL script that lists the score and name of all records in the table second_table in order of descending score.
        Does not display rows without a name value.

    17. Go to UTF8
        100-move_to_utf8.sql: MySQL script that converts the hbtn_0c_0 database to UTF8.

    18. Temperatures #0
        101-avg_temperatures.sql: MySQL script that displays the average temperature (Fahrenheit) by city in descending order.

    19. Temperatures #1
        102-top_city.sql: MySQL script that displays the three cities with the highest average temperature from July to August in descending order.

    20. Temperature #2
        103-max_state.sql: MySQL script that displays the max temperature of each state in order of state name.

### Authors

samuel effiong <samueleffiongjacobgmail.com>

[sql installation](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

[Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)

[Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)

[SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)

[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)

[What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)

[MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)

[MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

[installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

[video](https://www.youtube.com/watch?v=FR4QIeZaPeM)

```bash 
# Mysql comment
$ service mysql start
# list db
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
# create db
$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
# remove db
$  cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
# show table
$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
# create first tables in a database collection
$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# show the tables in specified db
$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# to show full discription of db
$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# list all tables
$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# first add 
$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

#  count 89
$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
# full creation
$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
# list my best record
$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# select the best
$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# cheating is bad
$  cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# score too low
$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# avaerage score
$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# number by score
$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# say my name
$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

# go to UTF8
$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```
