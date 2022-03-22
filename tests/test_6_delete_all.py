
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
#  -----deleting cart--------------- and all data-------------------
    def test_11_delete_cart(self):
        delete_data = self.add_cart_data

        response = self.tester.delete("/records",json=delete_data)
        assert response.status_code==204
    # deleting one more quantity
    def test_11_1_delete_cart(self):
        delete_data = self.add_cart_data

        response = self.tester.delete("/records",json=delete_data)
        assert response.status_code==204
    
    #deleting cart with wrong cart data
    def test_11_2_delete_cart_wrong_item(self):
        wrong_cart_item ={
        "name":self.data["name"].capitalize(),
        "password":self.data["password"],
        "item-type":self.category_data["category"].capitalize(),
        "item":"xxxx"
    }
        response = self.tester.delete("/records",json=wrong_cart_item)
        assert response.status_code==404
        assert response.content_type=="application/json"
        assert response.json=="Wrong item details"


    # deleting cart with user wrong credentials

    def test_11_3_delete_cart_wrong_password(self):
        wrong_cart_password ={
        "name":self.data["name"].capitalize(),
        "password":"xxx",
        "item-type":self.category_data["category"].capitalize(),
        "item":self.sub_data["sub-category"].capitalize()
    }
        response = self.tester.delete("/records",json=wrong_cart_password)
        assert response.status_code==404
        assert response.content_type=="application/json"
        assert response.json=="Wrong item record"

    def test_12_delete_subcategory(self):
        del_sub_data = {
            "category":self.category_data["category"],
            "sub-category":self.sub_data["sub-category"]
        }
        response = self.tester.delete("/categories/delete/subcategory",json = del_sub_data)
        assert response.status_code==204

    # deleting already deleted subcategory for its else part
    def test_12_1_delete_subcategory(self):
        del_sub_data = {
            "category":self.category_data["category"],
            "sub-category":self.sub_data["sub-category"]
        }
        response = self.tester.delete("/categories/delete/subcategory",json = del_sub_data)
        assert response.status_code==404
        response_data = response.json
        assert response_data == "Not Found"
    def test_13_delete_category(self):
        del_cat_data = self.category_data
        response = self.tester.delete("/categories/delete",json=del_cat_data)
        assert response.status_code==204

    # delete category with wrong details
        # wrong credentials
    def test_13_1_delete_category(self):
        del_cat_data = self.wrong_category_data
        response = self.tester.delete("/categories/delete",json=del_cat_data)
        assert response.status_code==404
        response_data = response.json
        assert response_data=='404'        

    def test_13_2_delete_category(self):
        response = self.tester.delete("/categories/delete",json=self.wrong_category_data_name)
        assert response.status_code==404
        response_data = response.json
        assert response_data=='404'

    def test_14_delete_customer_account(self):
        data = {
            "id":self.data["id"],
            "name":self.data["name"],
            "password":self.data["password"]
        }
        response = self.tester.delete("/login/delete",json=data)
        assert response.status_code==204
    #  deleting customer deletion else check
    def test_14_1_delete_customer_account(self):
        data = {
            "id":self.data["id"],
            "name":self.data["name"],
            "password":self.data["password"]
        }
        response = self.tester.delete("/login/delete",json=data)
        assert response.status_code==404
        assert response.content_type=="application/json"
        assert response.json == "record not found"
