# from tests.help_test import AllApiCalls
# from unittest.mock import patch
# class Test():
#         # # -------- All data to be used in testing----------------
#     data = {"id":12,
#         "name":"kevin".capitalize(),
#         "password":"pass",
#         "age":22,
#         "gender":"m".capitalize()}
    
#     show_data = {"id":12,
#         "name":"kevin".capitalize(),
#         "age":22,
#         "gender":"m".capitalize()}

#     category_data = {"admin":"vishwa3908",
#         "password":"pass1234",
#         "category":"Tester"}

#     sub_data = {
#             "category":category_data["category"].capitalize(),
#             "sub-category":"mytest".capitalize(),
#             "price":200
#         }

#     add_cart_data = {
#         "name":data["name"].capitalize(),
#         "password":data["password"],
#         "item-type":category_data["category"].capitalize(),
#         "item":sub_data["sub-category"].capitalize()
#     }

#     @patch("tests.help_test.AllApiCalls.get_homepage")
#     def test_1_get_homepage(self,mock_response):
#         mock_response.return_value = "hello"
#         obj = AllApiCalls()
#         data = obj.get_homepage()
#         assert data==mock_response.return_value

#     @patch("tests.help_test.AllApiCalls.get_new_customer",return_value = show_data)
#     def test_2_new_customer(self,mock_response):
#         obj = AllApiCalls()
#         data = obj.get_new_customer()
#         assert data==mock_response.return_value

#     @patch("tests.help_test.AllApiCalls.get_old_customer",return_value=show_data)
#     def test_3_old_customer(self,mock_response):
#         obj = AllApiCalls()
#         data = obj.get_old_customer()
#         assert data==mock_response.return_value

#     @patch("tests.help_test.AllApiCalls.get_new_category",return_value = category_data["category"]+"Category added")
#     def test_4_new_category(self,mock_response):
#         data = AllApiCalls().get_new_category()
#         assert data == mock_response.return_value
        
#     @patch("tests.help_test.AllApiCalls.show_category",status_code=200)
#     def test_5_show_category(self,mock_response):
#         data = AllApiCalls().show_category()
        
#     @patch("tests.help_test.AllApiCalls.get_new_subcategory",return_value=sub_data["sub-category"]+"sub-category created")
#     def test_6_new_category(self,mock_response):
#         obj = AllApiCalls()
#         data = obj.get_new_subcategory()
#         assert data == mock_response.return_value

#     @patch("tests.help_test.AllApiCalls.show_sub_category",return_value=sub_data)
#     def test_7_show_subcategory(self,mock_response):
#         obj = AllApiCalls()
#         data = obj.show_sub_category()
#         assert data==mock_response.return_value

#     @patch("tests.help_test.AllApiCalls.add_cart",return_value="item added")
#     def test_8_add_cart_data(self,mock_response):
#         obj = AllApiCalls()
#         data = obj.add_cart()
#         assert data==mock_response.return_value

#     @patch("tests.help_test.AllApiCalls.show_cart",return_value="cart data")
#     def test_9_show_cart(self,mock_response):
#         obj = AllApiCalls()
#         data = obj.show_cart()
#         assert data==mock_response.return_value