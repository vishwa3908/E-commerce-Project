from flask import Flask
from constants import constant
import pymysql
def connect_mysql():
    try:
        conn = pymysql.connect(
                host=constant.host,
                user=constant.user,
                password=constant.password,
                database=constant.database
            )
        mycursor = conn.cursor()
        return conn
    except:
        return 0
    