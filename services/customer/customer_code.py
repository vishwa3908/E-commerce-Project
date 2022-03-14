from flask import Flask,request,jsonify
import pymysql
from  Config.connection import connect_mysql



class Customer:

    def customer_cart(name):
    
        conn = connect_mysql()
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM {}".format(name.capitalize()))
        result = mycursor.fetchall()
        if result:
            sub_category = []
            for i in range(len(result)):
                data = {"Item-Type":result[i][0],
                'Item':result[i][1],
                "Quantity":result[i][2],
                'Price':result[i][3],
                "Total Price":result[i][4]}
                sub_category.append(data)
            return jsonify(sub_category),200
        else:
            return jsonify("Nothing on Cart"),200

    
    def customer_details():
        conn = connect_mysql()
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM customers")
        result = mycursor.fetchall()
        if result:
            customer_result = []
            for  i in range(len(result)):
                data = {
                    "Id":result[i][0],
                    'Name':result[i][1],
                'Age':result[i][2],
                'Gender':result[i][3]}
                customer_result.append(data)
            return jsonify(customer_result),200
        else:
            return jsonify("No customers"),404

    
    def add_customer_cart():
        
        conn = connect_mysql()
        mycursor = conn.cursor()
        name = request.json["name"].capitalize()
        password = request.json["password"]
        item = request.json["item"].capitalize()
        item_type = request.json["item-type"].capitalize()

        customer_record_value = (name,password,)
        # CHECKING IF CUSTOMER EXISTS

        customer_record_query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''

        mycursor.execute(customer_record_query,customer_record_value)
        customer_record_result = mycursor.fetchall()
        if customer_record_result:
            # CHECKING IF ITEM EXISTS IN CART 
            item_present_in_cart_value = (item,)
            item_present_in_cart_query = '''SELECT * FROM {} WHERE ITEM = %s'''.format(name)
            mycursor.execute(item_present_in_cart_query,item_present_in_cart_value)
            item_already_in_cart_result = mycursor.fetchall()
            
            if item_already_in_cart_result:
                # UPDATING QUANTITY COLUMN and total price column
                
                # UPDATING QUANTITY COLUMN 
                
                updating_column_value = (item,)
                updating_column_query = '''UPDATE {} SET QUANTITY = QUANTITY+1  WHERE ITEM = %s'''.format(name)
                
                mycursor.execute(updating_column_query,updating_column_value)
                conn.commit()
                
                
                #UPDATING TOTAL COLUMN   
                updating_total_column_query = '''UPDATE {} SET TOTAL = PRICE*QUANTITY  WHERE ITEM = %s'''.format(name)
                
                mycursor.execute(updating_total_column_query,updating_column_value)
                
                conn.commit()
                return jsonify("item added"),201
            # IF NOT IN CART THEN ADDING ITEM 
            else:
                item_check_value = (item,)
                item_check_query = '''SELECT PRICE FROM {} WHERE ITEMS = %s'''.format(item_type)
                mycursor.execute(item_check_query,item_check_value)
                item_check_result = mycursor.fetchall()
                mycursor.execute("INSERT INTO {}(ITEM_TYPE,ITEM,PRICE,TOTAL)VALUES(%s,%s,%s,%s)".format(name),(item_type,item,item_check_result[0][0],item_check_result[0][0]))
                conn.commit()
                return jsonify("Item added in cart"),201
            
        else:
            return jsonify("Wrong Customer Data"),404
    
    def remove_cart():
        
        conn = connect_mysql()
        mycursor = conn.cursor()
        name = request.json["name"].capitalize()
        password= request.json["password"]
        item_type = request.json["item-type"].capitalize()
        item = request.json["item"].capitalize()
        # CHECKING IF CUSTOMER EXISTS 
        check_customer_value = (name,password,)
        check_customer_query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''
        mycursor.execute(check_customer_query,check_customer_value)
        check_customer_result= mycursor.fetchall()
        # IF EXISTS 
        if check_customer_result:
            # CHECK IF ITEM EXISTS
            item_check_value = (item,)
            item_check_query = '''SELECT * FROM {} WHERE ITEMS = %s'''.format(item_type)
            mycursor.execute(item_check_query,item_check_value)
            item_check_result = mycursor.fetchall()
            if item_check_result:
                # CHECK IF ITS QUANTITY IS  1
                quantity_check_value = (item,)
                quantity_check_query = '''SELECT QUANTITY FROM {} WHERE ITEM = %s'''.format(name)
                mycursor.execute(quantity_check_query,quantity_check_value)
                quantity_check_result = mycursor.fetchall()
                # if 1
                if quantity_check_result[0][0]==1:
                    
                    delete_cart_value = (item,)
                    delete_cart_query = '''DELETE FROM {} WHERE ITEM = %s'''.format(name)
                    mycursor.execute(delete_cart_query,delete_cart_value)
                    conn.commit()
                    return jsonify("{} Deleted".format(item)),204
                # if not 1
                else:
                    # subtracting 1 from quantity
                    update_quantity_value = (item,)
                    update_quantity_query = '''UPDATE {} SET QUANTITY = QUANTITY-1 WHERE ITEM = %s'''.format(name)
                    mycursor.execute(update_quantity_query,update_quantity_value)
                    conn.commit()
                    # updating total value
                    updating_total_query = '''UPDATE {} SET TOTAL = PRICE*QUANTITY WHERE ITEM = %s'''.format(name)
                    mycursor.execute(updating_total_query,update_quantity_value)
                    conn.commit()
                    return jsonify("item removed"),204
                
                
                
                
                
            else:
                return jsonify("Wrong item details"),404

        else:
            return jsonify("Wrong item record"),404
            