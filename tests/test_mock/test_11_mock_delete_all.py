
from unittest.mock import patch
from api.login import *
from api.categories import *
from api.subcategories import *
from api.customer import *

class Test_delete_all:
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

    @patch("services.subcategory.subcategorycode.Subcategory.delete_this_subcategory")
    def test_1_delete_subcategory(self,mock_response):
        mock_response.return_value = self.sub_data["sub-category"] + "sub-category deleted"
        data = deletesubcategory()
        assert data == mock_response.return_value

    @patch('services.categories.categories_code.Categories.deletecategory')
    def test_2_delete_category(self,mock_response):
        mock_response.return_value = self.category_data["category"] + "category deleted"
        data = delete_category()

    @patch("services.customer.customer_code.Customer.remove_cart")
    def test_3_delete_cart(self,mock_response):
        mock_response.return_value = "item removed"
        data = remove_cart_item()
        assert data == mock_response.return_value

    @patch("services.login.customer_entry.Login.delete_my_account")
    def test_3_delete_account(self,mock_response):
        mock_response.return_value = "record deleted"
        data = delete_account()
        assert data==mock_response.return_value
