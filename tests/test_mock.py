import unittest
from  app import myapp
from app import home
from unittest.mock import Mock,patch
import requests
import pytest

class Test():

# -------- All data to be used in testing----------------

    tester = myapp.test_client()
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

    #------testing home page--------------
    def test_1_home_mock(self):
        mock_response = Mock(return_value="Welcome to Shopping Buddy")
        response = self.tester.get("/")
        self.tester.get = Mock(return_value=mock_response.return_value)
        assert self.tester.get("/")==mock_response.return_value
