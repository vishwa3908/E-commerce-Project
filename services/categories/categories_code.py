from flask import request,jsonify
from  Config.connection import connect_mysql


class Categories:
 
    def show_categories():
        conn = connect_mysql()
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM category")
        result = mycursor.fetchall()
        category = []
        if result:
            for i in range(len(result)):
                data = {"Category":result[i]}
                category.append(data)
            return {"Categories":category},200
        else:
            return jsonify("Empty"),200
    
    def add_category():
        conn = connect_mysql()
        mycursor = conn.cursor()
        admin = request.json['admin']
        password = request.json['password']
        if admin == 'vishwa3908' and password == 'pass1234':
            category_name = request.json["category"].capitalize()
            category_add_value = (category_name,category_name)
            category_add_query = '''INSERT INTO category(CATEGORY_NAME)SELECT * FROM(SELECT %s) as temp WHERE NOT EXISTS(SELECT CATEGORY_NAME FROM category WHERE CATEGORY_NAME = %s)LIMIT 1'''
            mycursor.execute(category_add_query,category_add_value)
            mycursor.execute('''CREATE TABLE IF NOT EXISTS {}(ID INT AUTO_INCREMENT PRIMARY KEY,ITEMS VARCHAR(20),PRICE INT )'''.format(category_name))
            conn.commit()
            return jsonify("{} Category added".format(category_name)),201
        else:
            return jsonify("invalid details"),404
    
    def deletecategory():
        conn = connect_mysql()
        mycursor = conn.cursor()
        admin = request.json['admin']
        password = request.json['password']
        category_name = request.json['category'].capitalize()
        if admin == 'vishwa3908' and password == 'pass1234':
            value = (category_name,)
            check_record_query = "SELECT * FROM category WHERE CATEGORY_NAME = %s"
            mycursor.execute(check_record_query,value)
            result = mycursor.fetchall()
            if result:
                query = "DELETE FROM category WHERE CATEGORY_NAME = %s"
                mycursor.execute(query,value)
                conn.commit()
                drop_query = "DROP TABLE IF EXISTS {}".format(category_name)
                mycursor.execute(drop_query)
                conn.commit()
                return jsonify('ok'),204
            else:
                return jsonify('404'),404
        else:
            return jsonify('404'),404
                
            
            




