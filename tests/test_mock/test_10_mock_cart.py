from unittest.mock import patch
from api.customer import *
class Testing_cart:

    category_data = {"admin":"vishwa3908",
    "password":"pass1234",
    "category":"Tester"}
    sub_data = {
        "category":category_data["category"].capitalize(),
        "sub-category":"mytest".capitalize(),
        "price":200
    }
    data = {"id":12,
            "name":"kevin".capitalize(),
            "password":"pass",
            "age":22,
            "gender":"m".capitalize()}
    add_cart_data = {
    "name":data["name"].capitalize(),
    "password":data["password"],
    "item-type":category_data["category"].capitalize(),
    "item":sub_data["sub-category"].capitalize()
        }

    @patch("services.customer.customer_code.Customer.add_customer_cart")
    def test_1_add_cart(self,mock_response):
        mock_response.return_value = "Item added in cart"
        data = add_customer_cart()
        assert data==mock_response.return_value

    @patch("services.customer.customer_code.Customer.customer_cart")
    def test_1_show_cart(self,mock_response):
        mock_response.return_value =self.sub_data
        data = show_customer_cart(self.data["name"])
        assert data==mock_response.return_value

    @patch("services.customer.customer_code.Customer.customer_details")
    def test_1_show_records(self,mock_response):
        mock_response.return_value =self.data
        data = show_customer_record()
        assert data==mock_response.return_value
