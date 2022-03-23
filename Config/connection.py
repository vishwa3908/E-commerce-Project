from flask import Flask
import pymysql
def connect_mysql():
    conn = pymysql.connect(
            host='big-project-rds.cpgtqvgczfeo.us-east-1.rds.amazonaws.com',
            user='vishwa',
            password='Password.123',
            database='shopping'
        )
    mycursor = conn.cursor()
    return conn