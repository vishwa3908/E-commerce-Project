from api.login import *
from unittest.mock import patch
class Testing:
    data = {"id":12,
    "name":"kevin".capitalize(),
    "password":"pass",
    "age":22,
    "gender":"m".capitalize()}
    
    show_data = {"id":12,
        "name":"kevin".capitalize(),
        "age":22,
        "gender":"m".capitalize()}


    @patch("services.login.customer_entry.Login.old_customer_login")
    def test_1_old_customer(self,mock_response):
        mock_response.return_value = self.show_data
        data = old_login()
        assert data==mock_response.return_value

    @patch("services.login.customer_entry.Login.new_customer")
    def test_2_new_customer(self,mock_response):
        mock_response.return_value = self.show_data
        data = new_login()
        assert data==mock_response.return_value
