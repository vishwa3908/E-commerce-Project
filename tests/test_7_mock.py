
from unittest import mock
from unittest.mock import patch
from services.categories.categories_code import Categories
from api.login import *
from app import myapp
from services.login.customer_entry import Login
class Testing:

    @patch("services.login.customer_entry.Login.old_customer_login",return_value="fff")
    @patch("api.login.old_login",return_value="fff")
    def test_22(self,mock_response,mock_data):
        data = old_login()
        assert data == "fff"

    @patch("services.categories.categories_code.Categories.show_categories")
    def test_1_1_home(self,mock_response):
        mock_response.return_value = "hello"
        obj = Categories()
        data = obj.show_categories()
        assert data=="hello"
    @patch("services.categories.categories_code.Categories.add_category")
    def test_2_add(self,mock_response):
        mock_response.return_value = "ggg"
        obj = Categories()
        data = Categories.add_category()
        assert data == "ggg"