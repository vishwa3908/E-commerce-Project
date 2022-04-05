from constants import constant
from  app import myapp
import pytest
from Config.connection import connect_mysql
class Test():

# -------- All data to be used in testing----------------

    tester = myapp.test_client()
    # -----adding cart------------

        # first check cart is empty
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_9_show_customer_cart(self):
        response = self.tester.get("/records/{}".format(constant.data["id"]))
        assert response.status_code==200
        assert response.headers["Content-Type"]=="application/json"
        response_data = response.json
        assert response_data=="Nothing on Cart"

    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_9_1_add_cart(self):
        response = self.tester.post("/records",json=constant.add_cart_data)
        assert response.status_code==201

    # updating cart one more time to check quantity updation
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_9_2_add_cart(self):
        response = self.tester.post("/records",json=constant.add_cart_data)
        assert response.status_code==201
    
    # adding item with wrong customer data
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_9_3_add_cart(self):
        response = self.tester.post("/records",json=constant.wrong_add_cart_data)
        assert response.status_code==404
        assert response.json=="Wrong Customer Data"
        assert response.content_type=="application/json"

# --------------showing customer cart----------------
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_10_show_customer_cart(self):
        response = self.tester.get("/records/{}".format(constant.data["id"]))
        assert response.status_code==200
        assert response.headers["Content-Type"]=="application/json"
        response_data = response.json
        assert response_data[0]["Item"]==constant.sub_data["sub-category"].capitalize()
        assert response_data[0]["Item-Type"]==constant.sub_data["category"].capitalize()
        assert response_data[0]["Price"]==constant.sub_data["price"]
        quant = response_data[0]["Quantity"]
        assert response_data[0]["Total Price"]==constant.sub_data["price"]*quant