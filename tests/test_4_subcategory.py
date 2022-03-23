from  app import myapp
from constants import constant

class Test():

# -------- All data to be used in testing----------------

    tester = myapp.test_client()

    #------------ adding sub category---------------    
        # first check sub-category else part
    
    def test_6_1_show_subcategory_else(self):
        response = self.tester.get("/categories/{}".format(constant.sub_data["category"]))
        assert response.status_code==200
        response_data = response.json
        assert response_data == "Empty"

    def test_7_add_subcategory(self):
        
        response = self.tester.post("/categories/add/subcategory",json=constant.sub_data)
        assert response.status_code==201
        assert response.content_type=="application/json"
        response_data= response.json
        assert response_data== constant.sub_data["sub-category"]+" "+"subcategory created"

    # adding sub category having category name wrong

    def test_7_1_add_subcategory(self):
        
        response = self.tester.post("/categories/add/subcategory",json=constant.wrong_sub_data)
        assert response.status_code==404
        assert response.content_type=="application/json"
        response_data= response.json
        assert response_data== "No category Found"
        
    #     ==========showing sub category================

    def test_8_show_subcategory(self): 
        response = self.tester.get("/categories/{}".format(constant.sub_data["category"]))
        assert response.status_code==200
        response_data = response.json
        assert response.headers["Content-Type"]=="application/json"
        assert response_data[0]["Item"]==constant.sub_data["sub-category"].capitalize()
        assert response_data[0]["Price"]=="Rs"+" "+str(constant.sub_data["price"])