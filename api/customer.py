from flask import Blueprint
from  services.customer.customer_code import Customer

mycustomer = Blueprint("mycustomer",__name__)


@mycustomer.route("/records",methods = ["POST"])
def add_customer_cart():
    return Customer.add_customer_cart()

@mycustomer.route("/records/<id>")
def show_customer_cart(id):
    return Customer.customer_cart(id)


@mycustomer.route("/records",methods=["DELETE"])
def remove_cart_item():
    return Customer.remove_cart()

@mycustomer.route("/records")
def show_customer_record():
    return Customer.customer_details()