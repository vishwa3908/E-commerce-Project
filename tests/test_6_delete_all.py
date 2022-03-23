
from  app import myapp
from constants import constant

class Test():

# -------- All data to be used in testing----------------

    tester = myapp.test_client()
#  -----deleting cart--------------- and all data-------------------
    def test_11_delete_cart(self):
        delete_data = constant.add_cart_data

        response = self.tester.delete("/records",json=delete_data)
        assert response.status_code==204
    # deleting one more quantity
    def test_11_1_delete_cart(self):
        delete_data = constant.add_cart_data

        response = self.tester.delete("/records",json=delete_data)
        assert response.status_code==204
    
    #deleting cart with wrong cart data
    def test_11_2_delete_cart_wrong_item(self):
        wrong_cart_item ={
        "name":constant.data["name"].capitalize(),
        "password":constant.data["password"],
        "item-type":constant.category_data["category"].capitalize(),
        "item":"xxxx"
    }
        response = self.tester.delete("/records",json=wrong_cart_item)
        assert response.status_code==404
        assert response.content_type=="application/json"
        assert response.json=="Wrong item details"


    # deleting cart with user wrong credentials

    def test_11_3_delete_cart_wrong_password(self):
        wrong_cart_password ={
        "name":constant.data["name"].capitalize(),
        "password":"xxx",
        "item-type":constant.category_data["category"].capitalize(),
        "item":constant.sub_data["sub-category"].capitalize()
    }
        response = self.tester.delete("/records",json=wrong_cart_password)
        assert response.status_code==404
        assert response.content_type=="application/json"
        assert response.json=="Wrong item record"

    def test_12_delete_subcategory(self):
        del_sub_data = {
            "category":constant.category_data["category"],
            "sub-category":constant.sub_data["sub-category"]
        }
        response = self.tester.delete("/categories/delete/subcategory",json = del_sub_data)
        assert response.status_code==204

    # deleting already deleted subcategory for its else part
    def test_12_1_delete_subcategory(self):
        del_sub_data = {
            "category":constant.category_data["category"],
            "sub-category":constant.sub_data["sub-category"]
        }
        response = self.tester.delete("/categories/delete/subcategory",json = del_sub_data)
        assert response.status_code==404
        response_data = response.json
        assert response_data == "Not Found"
    def test_13_delete_category(self):
        del_cat_data = constant.category_data
        response = self.tester.delete("/categories/delete",json=del_cat_data)
        assert response.status_code==204

    # delete category with wrong details
        # wrong credentials
    def test_13_1_delete_category(self):
        del_cat_data = constant.wrong_category_data
        response = self.tester.delete("/categories/delete",json=del_cat_data)
        assert response.status_code==404
        response_data = response.json
        assert response_data=='404'        

    def test_13_2_delete_category(self):
        response = self.tester.delete("/categories/delete",json=constant.wrong_category_data_name)
        assert response.status_code==404
        response_data = response.json
        assert response_data=='404'

    def test_14_delete_customer_account(self):
        data = {
            "id":constant.data["id"],
            "name":constant.data["name"],
            "password":constant.data["password"]
        }
        response = self.tester.delete("/login/delete",json=data)
        assert response.status_code==204
    #  deleting customer deletion else check
    def test_14_1_delete_customer_account(self):
        data = {
            "id":constant.data["id"],
            "name":constant.data["name"],
            "password":constant.data["password"]
        }
        response = self.tester.delete("/login/delete",json=data)
        assert response.status_code==404
        assert response.content_type=="application/json"
        assert response.json == "record not found"
