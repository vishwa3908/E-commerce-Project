from constants import constant
from unittest.mock import patch
from api.login import *
from api.categories import *
from api.subcategories import *
from api.customer import *

class Test_delete_all:

    @patch("services.subcategory.subcategorycode.Subcategory.delete_this_subcategory")
    def test_1_delete_subcategory(self,mock_response):
        mock_response.return_value = constant.sub_data["sub-category"] + "sub-category deleted"
        data = deletesubcategory()
        assert data == mock_response.return_value

    @patch('services.categories.categories_code.Categories.deletecategory')
    def test_2_delete_category(self,mock_response):
        mock_response.return_value = constant.category_data["category"] + "category deleted"
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
