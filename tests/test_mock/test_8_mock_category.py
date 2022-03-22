
from unittest.mock import patch
from api.categories import *
class Testing_mock:
    category_data = {"admin":"vishwa3908",
        "password":"pass1234",
        "category":"Tester"}

    @patch('services.categories.categories_code.Categories.show_categories')
    def test_1_show_category(self,mock_response):
        mock_response.return_value = self.category_data["category"]
        data = showcategory()
        assert data == mock_response.return_value
    
    @patch('services.categories.categories_code.Categories.add_category')
    def test_2_add_category(self,mock_response):
        mock_response.return_value = self.category_data["category"]+" Category added"
        data = addcategory()
        assert data == mock_response.return_value