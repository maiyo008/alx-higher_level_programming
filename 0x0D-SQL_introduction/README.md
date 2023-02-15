# 0x0D. SQL - Introduction
---
## Concepts
* [Databases](https://intranet.alxswe.com/concepts/37)
* [Databases](https://intranet.alxswe.com/concepts/556)

## Resources
**Read or watch**
* [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
* [Basic SQL statements: DDL and DML (_no need to read the chapter “Privileges_”)](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
* [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
* [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
* [installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

## Learning resources
**General**
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

## More info
**Comments for your SQL file:**
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
**Install MySQL 8.0 on Ubuntu 20.04 LTS**
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
**Connect to your MySQL server:**
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
### **Use “container-on-demand” to run MySQL**
**In the container, credentials are root/root**
* Ask for container Ubuntu 20.04
* Connect via SSH
* OR connect via the Web terminal
* In the container, you should start MySQL * before playing with it:
```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
**In the container, credentials are - root/root**

## Tasks
### Task 0. List Databases
* Write a script that lists all databases of your MySQL server

### Task 1 . Create a database
* Write a script that creates the database `hbtn_0c_0` in your MySQL server.
    * If the database `hbtn_0c_0` already exists, your script should not fail
    * You are not allowed to use the `SELECT` or `SHOW` statements

### Task 2. Delete a database
* Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
    * If the database `hbtn_0c_0` doesn’t exist, your script should not fail
    * You are not allowed to use the `SELECT` or `SHOW` statements

### Task 3. List tables
* Write a script that lists all the tables of a database in your MySQL server.
    The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)

### Task 4. First table
* Write a script that creates a table called `first_table` in the current database in your MySQL server.
    * `first_table `description:
        * `id` INT
        * `name` VARCHAR(256)
    * The database name will be passed as an argument of the `mysql` command
    * If the table `first_table` already exists, your script should not fail
    * You are not allowed to use the `SELECT` or `SHOW` statements

### Task 5. Full description
* Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
    * The database name will be passed as an argument of the `mysql` command
    * You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements

### Task 6. List all in table
* Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
    * All fields should be printed
    * The database name will be passed as an argument of the `mysql` command

### Task 7. First add
* Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
    * New row:
        * `id` = 89
        * `name` = Best School
    * The database name will be passed as an argument of the `mysql` command

### Task 8. Count89
* Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
    * The database name will be passed as an argument of the mysql command

### Task 9. Full creation
* Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.

    * `second_table` description:
        * `id` INT
        * `name` VARCHAR(256)
        * `score` INT
    * The database name will be passed as an argument to the `mysql` command
    * If the table `second_table` already exists, your script should not fail
    * You are not allowed to use the `SELECT` and `SHOW` statements
    * Your script should create these records:
        * `id` = 1, `name` = “John”, `score` = 10
        * `id` = 2, `name` = “Alex”, `score` = 3
        * `id` = 3, `name` = “Bob”, `score` = 14
        * `id` = 4, `name` = “George”, `score` = 8

### Task 10. List by best
* Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
    * Results should display both the score and the name (in this order)
    * Records should be ordered by score (top first)
    * The database name will be passed as an argument of the `mysql `command

### Task 11. Select the best
* Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
    * Results should display both the `score` and the `name` (in this order)
    * Records should be ordered by score (top first)
    * The database name will be passed as an argument of the `mysql` command

### Task 12. Cheating is bad
* Write a script that updates the score of Bob to `10` in the table `second_table`
    * You are not allowed to use Bob’s id value, only the `name` field
    * The database name will be passed as an argument of the `mysql` command

### Task 13. Score too low
* Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
    * The database name will be passed as an argument of the `mysql` command

### Task 14. Average
* Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

    * The result column name should be `average`
    * The database name will be passed as an argument of the `mysql` command

### Task 15. Number by score
* Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

    * The result should display:
        * the `score`
        * the number of records for this `score` with the label `number`
    * The list should be sorted by the number of records (descending)
    * The database name will be passed as an argument to the `mysql` command

### Task 16. Say my name
* Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

    * Don’t list rows without a `name` value
    * Results should display the score and the name (in this order)
    * Records should be listed by descending score
    * The database name will be passed as an argument to the `mysql` command
__In this example, new data have been added to the table second_table.__

### Task 17. Go to UTF8
* Write a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.

* You need to convert all of the following to `UTF8`:

    * Database `hbtn_0c_0`
    * Table `first_table`
    * Field `name` in `first_table`

### Task 18. Temperatures 0.
* Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql)

* Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

### Task 19. Temperatures 1.
* Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

### Task 20. Temperature 2.
* Write a script that displays the max temperature of each state (ordered by State name).