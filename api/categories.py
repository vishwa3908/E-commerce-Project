from flask import Blueprint

from  services.categories.categories_code import Categories

mycategories = Blueprint("mycategories",__name__)


@mycategories.route("/categories")
def showcategory():
    return Categories.show_categories()

@mycategories.route("/categories/add",methods=["POST"])
def addcategory():
    return Categories.add_category()

@mycategories.route("/categories/delete",methods =["DELETE"])
def delete_category():
    return Categories.deletecategory()