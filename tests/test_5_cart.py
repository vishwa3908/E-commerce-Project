
from pydoc import resolve
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
    wrong_add_cart_data = {
        "name":"xxxxx",
        "password":data["password"],
        "item-type":category_data["category"].capitalize(),
        "item":sub_data["sub-category"].capitalize()
    }
    # -----adding cart------------
    # first check cart is empty
    def test_9_show_customer_cart(self):
        response = self.tester.get("/records/{}".format(self.data["name"]))
        assert response.status_code==200
        assert response.headers["Content-Type"]=="application/json"
        response_data = response.json
        assert response_data=="Nothing on Cart"

    def test_9_1_add_cart(self):
        response = self.tester.post("/records",json=self.add_cart_data)
        assert response.status_code==201

    # updating cart one more time to check quantity updation
    def test_9_2_add_cart(self):
        response = self.tester.post("/records",json=self.add_cart_data)
        assert response.status_code==201
    
    # adding item with wrong customer data
    def test_9_3_add_cart(self):
        response = self.tester.post("/records",json=self.wrong_add_cart_data)
        assert response.status_code==404
        assert response.json=="Wrong Customer Data"
        assert response.content_type=="application/json"

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