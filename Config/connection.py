from flask import Flask
import pymysql
def connect_mysql():
    conn = pymysql.connect(
            host='localhost',
            user='vishwa',
            password='Password.123',
            database='shopping'
        )
    mycursor = conn.cursor()
    return conn