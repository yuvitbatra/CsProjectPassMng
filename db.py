import os
os.system("pip install -r requirements.txt")

import pymysql

conn = pymysql.connect(host="localhost",user="root",password="amity")
c = conn.cursor()
c.execute("create database adityagautampassmng25346")
conn.commit()
conn.select_db("adityagautampassmng25346")
c.execute("create table passlog(sno int not null, softname varchar(100),password varchar(512),emailId varchar(200), deviation bigint)")
conn.commit()

