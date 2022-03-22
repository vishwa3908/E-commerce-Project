
from unittest.mock import patch 
from api.subcategories import *
class Test_subcategory:

    sub_data = {
        "category":"Tester",
        "sub-category":"mytest".capitalize(),
        "price":200
    }
    @patch("services.subcategory.subcategorycode.Subcategory.add_subcategory")
    def test_1_add_subcategory(self,mock_response):
        mock_response.return_value = self.sub_data["sub-category"]+"subcategory created"
        data = addsubcategory()
        assert data==mock_response.return_value

    @patch("services.subcategory.subcategorycode.Subcategory.show_subcategory")
    def test_2_show_subcategory(self,mock_response):
        mock_response.return_value = self.sub_data
        data = showsubcategory(self.sub_data["category"])
        assert data==mock_response.return_value