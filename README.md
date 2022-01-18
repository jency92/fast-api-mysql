# fast-api-mysql

### Run mysql as docker
```
docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=admin -d mysql
```

### Create database
```
root@instance-1:~# docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                                  NAMES
aa88ee58e5a9   mysql     "docker-entrypoint.s…"   37 seconds ago   Up 3 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   some-mysql
root@instance-1:~# docker exec -it aa88ee58e5a9 sh
# mysql -u root -p'admin' -h localhost
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.27 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.


mysql> create database flask_test;
Query OK, 1 row affected (0.00 sec)

```

### Create table and insert data
```
mysql> use flask_test;
Database changed

mysql> use flask_test;
Database changed
mysql> CREATE TABLE User(
    ->  userId INT NOT NULL AUTO_INCREMENT,
    ->  userName VARCHAR(100) NOT NULL,
    ->  password VARCHAR(40) NOT NULL,
    ->  PRIMARY KEY(userId)
    ->  );
Query OK, 0 rows affected (0.02 sec)

mysql> insert into User values('1','Admin','admin');
Query OK, 1 row affected (0.00 sec)
```

Referenece: https://codehandbook.org/python-web-application-flask-mysql/
