from flask import Blueprint
from  services.subcategory.subcategorycode import Subcategory

mysubcategory = Blueprint("mysubcategory",__name__)

@mysubcategory.route("/categories/<sub>")
def showsubcategory(sub):
    return Subcategory.show_subcategory(sub)


@mysubcategory.route("/categories/delete/subcategory",methods=["DELETE"])
def deletesubcategory():
    return Subcategory.delete_this_subcategory()

@mysubcategory.route("/categories/add/subcategory",methods=["POST"])
def addsubcategory():
    return Subcategory.add_subcategory()