from unittest.mock import patch
from api.customer import *
from constants import constant
class Testing_cart:

    @patch("services.customer.customer_code.Customer.add_customer_cart")
    def test_1_add_cart(self,mock_response):
        mock_response.return_value = "Item added in cart"
        data = add_customer_cart()
        assert data==mock_response.return_value

    @patch("services.customer.customer_code.Customer.customer_cart")
    def test_1_show_cart(self,mock_response):
        mock_response.return_value =constant.sub_data
        data = show_customer_cart(constant.data["name"])
        assert data==mock_response.return_value

    @patch("services.customer.customer_code.Customer.customer_details")
    def test_1_show_records(self,mock_response):
        mock_response.return_value =constant.data
        data = show_customer_record()
        assert data==mock_response.return_value
