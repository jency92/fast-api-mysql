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
```

```
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

```

#### Create database with name flask_test
```
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



## Steps to run the app

#### Install package dependencies with pip3
```
pip3 install -r requirements.txt
```

#### Run the app
```
export db_user=root
export db_password=admin
export db_name=flask_test
export db_host=localhost
sudo docker run -e db_user=root -e db_password=admin -e db_name=flask_test -e db_host=192.168.1.7 fast-api-mysql

python3 main.py
```

#### Test application
```
curl http://127.0.0.1:8080/Authenticate?UserName=Admin&Password=admin
```


### K8s deployment changes to inject env
```
      env:
        - name: db_user
          value: root
        - name: db_password
          value: admin
        - name: db_name
          value: flask_test
        - name: db_host
          value: localhost
```


NOTE: don't use db_host as localhost instead use GCP instance external IP or VM IP 
