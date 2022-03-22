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
    # wrong credentials
    wrong_category_data = {"admin":"vishwa",
        "password":"pass1234",
        "category":"Tester"}
    # wrong category name
    wrong_category_data_name = {"admin":"vishwa3908",
        "password":"pass1234",
        "category":"xxxxx"}

    sub_data = {
            "category":category_data["category"].capitalize(),
            "sub-category":"mytest".capitalize(),
            "price":200
        }
    
    wrong_sub_data = {
            "category":"xxxxxx",
            "sub-category":"mytest".capitalize(),
            "price":200
        }

    add_cart_data = {
        "name":data["name"].capitalize(),
        "password":data["password"],
        "item-type":category_data["category"].capitalize(),
        "item":sub_data["sub-category"].capitalize()
    }
    #------------ adding sub category---------------    
        # first check sub-category else part
    
    def test_6_1_show_subcategory_else(self):
        response = self.tester.get("/categories/{}".format(self.sub_data["category"]))
        assert response.status_code==200
        response_data = response.json
        assert response_data == "Empty"

    def test_7_add_subcategory(self):
        
        response = self.tester.post("/categories/add/subcategory",json=self.sub_data)
        assert response.status_code==201
        assert response.content_type=="application/json"
        response_data= response.json
        assert response_data== self.sub_data["sub-category"]+" "+"subcategory created"

    # adding sub category having category name wrong

    def test_7_1_add_subcategory(self):
        
        response = self.tester.post("/categories/add/subcategory",json=self.wrong_sub_data)
        assert response.status_code==404
        assert response.content_type=="application/json"
        response_data= response.json
        assert response_data== "No category Found"
        
    #     ==========showing sub category================

    def test_8_show_subcategory(self): 
        response = self.tester.get("/categories/{}".format(self.sub_data["category"]))
        assert response.status_code==200
        response_data = response.json
        assert response.headers["Content-Type"]=="application/json"
        assert response_data[0]["Item"]==self.sub_data["sub-category"].capitalize()
        assert response_data[0]["Price"]=="Rs"+" "+str(self.sub_data["price"])