from  app import myapp


class Test():

# -------- All data to be used in testing----------------

    tester = myapp.test_client()
    data = {"id":12,
        "name":"kevin".capitalize(),
        "password":"pass",
        "age":22,
        "gender":"m".capitalize()}
    
    show_data = {"id":12,
        "name":"kevin".capitalize(),
        "age":22,
        "gender":"m".capitalize()}

    category_data = {"admin":"vishwa3908",
        "password":"pass1234",
        "category":"Tester"}

    sub_data = {
            "category":category_data["category"].capitalize(),
            "sub-category":"mytest".capitalize(),
            "price":200
        }

    add_cart_data = {
        "name":data["name"].capitalize(),
        "password":data["password"],
        "item-type":category_data["category"].capitalize(),
        "item":sub_data["sub-category"].capitalize()
    }

    #------testing home page--------------
    def test_1_home(self):
        response = self.tester.get("/")
        response_data = response.json
        assert response_data=="WELCOME TO SHOPPING BUDDY"
        assert response.content_type =="application/json"
        assert response.status_code==200

        
        # assert response.content_type=="application/json"

    # wrong http request for home
    def test_1_1_home(self):
        response = self.tester.post("/")
        assert response.status_code==405
        
    


    
#----------testing new customers--------------

    def test_2_new_customer(self):
        
        response = self.tester.post("/login/new",json=self.data)
        assert response.status_code==201
        response_data = response.json
        assert response_data==self.show_data
        assert response.content_type=="application/json"

        #------- negative testing--------------------
        # ---If id is over limit-------
    def test_2_1_wrong_new_customer(self):
        wrong_data = {
                "id":333333,
                "name": self.data["name"],
                "age":self.data["age"],
                "gender":self.data["gender"],
                "password":self.data["password"]
        }
        response = self.tester.post("/login/new",json =wrong_data )
        assert response.status_code==200
        response_data = response.json
        assert response_data=="enter id between 1 and 99999"
        assert response.content_type=="application/json"

# --------if data is not inserted----------
    def test_2_2_wrong_new_customer(self):
        response = self.tester.post("/login/new")
        assert response.status_code==500

# -------------if same id is inserted----------
    def test_2_3_new_customer(self):
        
        response = self.tester.post("/login/new",json=self.data)
        assert response.status_code==200
        response_data = response.json
        assert response_data=="Enter different id"
        assert response.content_type=="application/json"
#-------------------testing all customers records-----------------

    def test_3_get_all_customer(self):
        response = self.tester.get("/records")
        assert response.status_code==200
        assert response.content_type=="application/json"

    def test_3_1_get_all_customer(self):
        response = self.tester.post("/records")
        assert response.status_code==500
        
#-----------checking old customer login----------------

    def test_4_old_customer(self):
        login_data = {
            "id": self.data["id"],
            "name":self.data["name"],
            "password":self.data["password"]
        }
        response = self.tester.get("/login",json = login_data)
        assert response.status_code ==200
        response_data = response.json
        assert response_data["Id"]==self.data["id"]
        assert response_data["Name"]==self.data["name"].capitalize()
        assert response_data["Age"]==self.data["age"]
        assert response_data["Gender"]==self.data["gender"].capitalize()
        assert response.content_type=="application/json"

#------negative checking of old login--------------
    # negative test
    def test_4_1_wrong_old_customer_login(self):
        data = {
            "id":self.data["id"],
            "name":self.data["name"],
            "password":"ppp"
        }
        response = self.tester.get("/login",json = data)
        assert response.status_code==404
        response_data = response.json
        assert response_data== "No record found"
        assert response.content_type=="application/json"

    def test_4_2_wrong_old_customer_login(self):
        data = {
            "id":self.data["id"],
            "name":"ddd",
            "password":self.data["password"]
        }
        response = self.tester.get("/login",json = data)
        assert response.status_code==404
        response_data = response.json
        assert response_data== "No record found"
        assert response.content_type=="application/json"

    def test_4_3_wrong_old_customer_login(self):
        data = {
            "id":self.data["id"],
            "name":self.data["name"],
            "password":1222
        }
        response = self.tester.get("/login",json = data)
        assert response.status_code==404
        response_data = response.json
        assert response_data== "No record found"
        assert response.content_type=="application/json"
    
    def test_4_4_wrong_old_customer_login(self):
        response = self.tester.get("/login")
        assert response.status_code==500
    

#==========checking new category creation-===================
        
    def test_5_create_new_category(self):
        response = self.tester.post("/categories/add",json=self.category_data)
        assert response.status_code==201
        assert response.content_type=="application/json"
        response_data = response.json
        assert response_data==self.category_data["category"]+" "+"Category added"

#=========showing category check================

    def test_6_show_category(self):
        response = self.tester.get("/categories")
        assert response.status_code==200
        assert response.content_type=="application/json"

    #------------ adding sub category---------------    

    def test_7_add_subcategory(self):
        
        response = self.tester.post("/categories/add/subcategory",json=self.sub_data)
        assert response.status_code==201
        assert response.content_type=="application/json"
        response_data= response.json
        assert response_data== self.sub_data["sub-category"]+" "+"subcategory created"

#     showing sub category================

    def test_8_show_subcategory(self): 
        response = self.tester.get("/categories/{}".format(self.sub_data["category"]))
        assert response.status_code==200
        response_data = response.json
        assert response.headers["Content-Type"]=="application/json"
        assert response_data[0]["Item"]==self.sub_data["sub-category"].capitalize()
        assert response_data[0]["Price"]=="Rs"+" "+str(self.sub_data["price"])

# -----adding cart------------

    def test_9_add_cart(self):
        response = self.tester.post("/records",json=self.add_cart_data)
        assert response.status_code==201

    # updating cart one more time to check quantity updation
    def test_9_1_add_cart(self):
        response = self.tester.post("/records",json=self.add_cart_data)
        assert response.status_code==201

# --------------showing customer cart----------------

    def test_10_show_customer_cart(self):
        response = self.tester.get("/records/{}".format(self.data["name"]))
        assert response.status_code==200
        assert response.headers["Content-Type"]=="application/json"
        response_data = response.json
        assert response_data[0]["Item"]==self.sub_data["sub-category"].capitalize()
        assert response_data[0]["Item-Type"]==self.sub_data["category"].capitalize()
        assert response_data[0]["Price"]==self.sub_data["price"]
        quant = response_data[0]["Quantity"]
        assert response_data[0]["Total Price"]==self.sub_data["price"]*quant

# -----deleting cart--------------- and all data-------------------
    def test_11_delete_cart(self):
        delete_data = self.add_cart_data

        response = self.tester.delete("/records",json=delete_data)
        assert response.status_code==204
    # deleting one more quantity
    def test_11_1_delete_cart(self):
        delete_data = self.add_cart_data

        response = self.tester.delete("/records",json=delete_data)
        assert response.status_code==204

    def test_12_delete_subcategory(self):
        del_sub_data = {
            "category":self.category_data["category"],
            "sub-category":self.sub_data["sub-category"]
        }
        response = self.tester.delete("/categories/delete/subcategory",json = del_sub_data)
        assert response.status_code==204

    def test_13_delete_category(self):
        del_cat_data = self.category_data
        response = self.tester.delete("/categories/delete",json=del_cat_data)
        assert response.status_code==204


    def test_14_delete_customer_account(self):
        data = {
            "id":self.data["id"],
            "name":self.data["name"],
            "password":self.data["password"]
        }
        response = self.tester.delete("/login/delete",json=data)
        assert response.status_code==204