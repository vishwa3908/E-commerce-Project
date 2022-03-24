#database data 
host='localhost'
user='vishwa'
password='Password.123'
database='ecommerce'










data = {"id":12,
    "name":"kevin".capitalize(),
    "password":"pass",
    "age":22,
    "gender":"m".capitalize()
    }

show_data = {"id":12,
    "name":"kevin".capitalize(),
    "age":22,
    "gender":"m".capitalize()
    }

category_data = {"admin":"vishwa3908",
    "password":"pass1234",
    "category":"Tester"
    }
# wrong credentials

wrong_category_data = {"admin":"vishwa",
    "password":"pass1234",
    "category":"Tester"
    }
# wrong category name
wrong_category_data_name = {"admin":"vishwa3908",
    "password":"pass1234",
    "category":"xxxxx"
    }

sub_data = {
    "category":category_data["category"].capitalize(),
    "sub-category":"mytest".capitalize(),
    "price":200
    }

wrong_sub_data = {
    "category":"xxxxxx",
    "sub-category":"mytest".capitalize(),
    "price":200
    }

add_cart_data = {
    "name":data["name"].capitalize(),
    "password":data["password"],
    "item-type":category_data["category"].capitalize(),
    "item":sub_data["sub-category"].capitalize()
    }

wrong_add_cart_data = {
"name":"xxxxx",
"password":data["password"],
"item-type":category_data["category"].capitalize(),
"item":sub_data["sub-category"].capitalize()
}
