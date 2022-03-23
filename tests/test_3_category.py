
from  app import myapp
from constants import constant

class Test():

# -------- All data to be used in testing----------------

    tester = myapp.test_client()

    

#==========checking new category creation-===================
    

    def test_5_create_new_category(self):
        response = self.tester.post("/categories/add",json=constant.category_data)
        assert response.status_code==201
        assert response.content_type=="application/json"
        response_data = response.json
        assert response_data==constant.category_data["category"]+" "+"Category added"
    
    def test_5_1_wrong_category_details(self):
        response = self.tester.post("/categories/add",json=constant.wrong_category_data)  
        assert response.status_code==404  
        response_data = response.json
        assert response_data=="invalid details"    

#=========showing category check================

    def test_6_show_category(self):
        response = self.tester.get("/categories")
        assert response.status_code==200
        assert response.content_type=="application/json"
