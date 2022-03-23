from api.login import *
from constants import constant
from unittest.mock import patch
class Testing:


    @patch("services.login.customer_entry.Login.old_customer_login")
    def test_1_old_customer(self,mock_response):
        mock_response.return_value = constant.show_data
        data = old_login()
        assert data==mock_response.return_value

    @patch("services.login.customer_entry.Login.new_customer")
    def test_2_new_customer(self,mock_response):
        mock_response.return_value = constant.show_data
        data = new_login()
        assert data==mock_response.return_value
