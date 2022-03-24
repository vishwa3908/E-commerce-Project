from cgitb import reset
from Config.connection import connect_mysql
import pytest
from  app import myapp
from constants import constant

class Test():

# -------- All data to be used in testing----------------

    tester = myapp.test_client()



    
#----------testing new customers--------------

    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_2_new_customer(self):
        
        response = self.tester.post("/login/new",json=constant.data)
        assert response.status_code==201
        response_data = response.json
        assert response_data==constant.show_data
        assert response.content_type=="application/json"

        #------- negative testing--------------------
        # ---If id is over limit-------
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_2_1_wrong_new_customer(self):
        wrong_data = {
                "id":333333,
                "name": constant.data["name"],
                "age":constant.data["age"],
                "gender":constant.data["gender"],
                "password":constant.data["password"]
        }
        response = self.tester.post("/login/new",json =wrong_data )
        assert response.status_code==200
        response_data = response.json
        assert response_data=="enter id between 1 and 99999"
        assert response.content_type=="application/json"

# --------if data is not inserted----------
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_2_2_wrong_new_customer(self):
        response = self.tester.post("/login/new")
        assert response.status_code==500

# -------------if same id is inserted----------
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_2_3_new_customer(self):
        
        response = self.tester.post("/login/new",json=constant.data)
        assert response.status_code==200
        response_data = response.json
        assert response_data=="Enter different id"
        assert response.content_type=="application/json"
#-------------------testing all customers records-----------------
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_3_get_all_customer(self):
        response = self.tester.get("/records")
        assert response.status_code==200
        assert response.content_type=="application/json"

    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_3_1_get_all_customer(self):
        response = self.tester.post("/records")
        assert response.status_code==500
        
#-----------checking old customer login----------------
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_4_old_customer(self):
        login_data = {
            "id": constant.data["id"],
            "name":constant.data["name"],
            "password":constant.data["password"]
        }
        response = self.tester.get("/login",json = login_data)
        assert response.status_code ==200
        response_data = response.json
        assert response_data["Id"]==constant.data["id"]
        assert response_data["Name"]==constant.data["name"].capitalize()
        assert response_data["Age"]==constant.data["age"]
        assert response_data["Gender"]==constant.data["gender"].capitalize()
        assert response.content_type=="application/json"

#------negative checking of old login--------------
        # negative test
    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_4_1_wrong_old_customer_login(self):
        data = {
            "id":constant.data["id"],
            "name":constant.data["name"],
            "password":"ppp"
        }
        response = self.tester.get("/login",json = data)
        assert response.status_code==404
        response_data = response.json
        assert response_data== "No record found"
        assert response.content_type=="application/json"

    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_4_2_wrong_old_customer_login(self):
        data = {
            "id":constant.data["id"],
            "name":"ddd",
            "password":constant.data["password"]
        }
        response = self.tester.get("/login",json = data)
        assert response.status_code==404
        response_data = response.json
        assert response_data== "No record found"
        assert response.content_type=="application/json"

    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_4_3_wrong_old_customer_login(self):
        data = {
            "id":constant.data["id"],
            "name":constant.data["name"],
            "password":1222
        }
        response = self.tester.get("/login",json = data)
        assert response.status_code==404
        response_data = response.json
        assert response_data== "No record found"
        assert response.content_type=="application/json"

    @pytest.mark.skipif(connect_mysql()==0,reason="cannot connect to database")
    def test_4_4_wrong_old_customer_login(self):
        response = self.tester.get("/login")
        assert response.status_code==500