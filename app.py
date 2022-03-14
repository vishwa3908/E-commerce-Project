from flask import Flask,jsonify
import pymysql,requests
from  api.customer import mycustomer
from  api.login import log_in
from  api.subcategories import mysubcategory
from  api.categories import mycategories
from  Config.connection import connect_mysql
from  model.admin import Admin
from  model.category import Category
from  model.customer import Customer

myapp = Flask(__name__)
myapp.register_blueprint(mycustomer)
myapp.register_blueprint(mycategories)

myapp.register_blueprint(log_in)
myapp.register_blueprint(mysubcategory)
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='vishwa',
        password='Password.123'
    )
    return conn
@myapp.route("/",methods=["GET"])
def home():
    conn = connection()
    mycursor = conn.cursor()
    mycursor.execute("""CREATE USER IF NOT EXISTS 'vishwa'@'localhost' IDENTIFIED BY 'Password.123'""")
    mycursor.execute("CREATE DATABASE IF NOT EXISTS shopping")

    Admin.create_admin()
    Category.create_category()
    Customer.create_custome_table()

    return jsonify("WELCOME TO SHOPPING BUDDY")


if __name__=="__main__":
    myapp.run(debug=True)