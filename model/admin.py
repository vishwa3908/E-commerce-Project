from flask import Flask
import pymysql
from  Config.connection import connect_mysql

class Admin:
    
    def create_admin():
        conn = connect_mysql()
        mycursor = conn.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS admin(name varchar(20) PRIMARY KEY,password varchar(20))")
        mycursor.execute("INSERT INTO admin(name,password)SELECT * FROM(SELECT 'vishwa3908','pass1234') as temp WHERE NOT EXISTS(SELECT name,password FROM admin WHERE name ='vishwa3908' AND password = 'pass1234')LIMIT 1")
        conn.commit()
