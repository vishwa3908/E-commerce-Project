from flask import Flask
import pymysql
from  Config.connection import connect_mysql


class Category:

    def create_category():
        conn = connect_mysql()
        mycursor = conn.cursor()
        mycursor.execute("CREATE TABLE if not exists category(CATEGORY_NAME VARCHAR(30) PRIMARY KEY)")