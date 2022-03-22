
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

    

#==========checking new category creation-===================
    

    def test_5_create_new_category(self):
        response = self.tester.post("/categories/add",json=self.category_data)
        assert response.status_code==201
        assert response.content_type=="application/json"
        response_data = response.json
        assert response_data==self.category_data["category"]+" "+"Category added"
    
    def test_5_1_wrong_category_details(self):
        response = self.tester.post("/categories/add",json=self.wrong_category_data)  
        assert response.status_code==404  
        response_data = response.json
        assert response_data=="invalid details"    

#=========showing category check================

    def test_6_show_category(self):
        response = self.tester.get("/categories")
        assert response.status_code==200
        assert response.content_type=="application/json"
