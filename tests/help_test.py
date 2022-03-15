from urllib import response
import requests


class AllApiCalls():


    # # -------- All data to be used in testing----------------
    data = {"id":12,
        "name":"kevin",
        "password":"pass",
        "age":22,
        "gender":"m"}

    check_old_data = {"id":data["id"],
                    "name":data["name"],
                    "password":data["password"]}
    
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

    url = "http://127.0.0.1:5000"

    def get_homepage(self):
        response = requests.get(self.url)
        response_data = response.json
        return response_data

    def get_new_customer(self):
        response = requests.post("{}".format(self.url)+"/login/new",json=self.data)
        return response.json()

    def get_old_customer(self):
        response = requests.get("{}".format(self.url)+"/login",json=self.check_old_data)
        return response.json()


    def get_new_category(self):
        response = requests.post("{}".format(self.url)+"/categories/add",json=self.category_data)
        return response.json()

    def show_category(self):
        response = requests.get(f"{self.url}"+"/categories")
        return response.json()

    def get_new_subcategory(self):
        response = requests.post(f"{self.url}"+"/categories/add/subcategory",json=self.sub_data)
        return response.json()

    def show_sub_category(self):
        response = requests.get(f"{self.url}"+"/categories/{}".format(self.sub_data["category"]))
        return response.json()

    def add_cart(self):
        response = requests.post(f"{self.url}"+"/records",json = self.add_cart_data)
        return response.json()
    
    def show_cart(self):
        response = requests.get(f"{self.url}"+"/records/{}".format(self.data["name"]))
        return response.json()