from flask import Blueprint, render_template
from src.models.product import Product

product_blueprint = Blueprint("product", __name__)


@product_blueprint.route("/menu")
def menu():
    products = Product.query.all()
    return render_template("product/menu.html", products=products)


@product_blueprint.route("/view/<int:product_id>")
def view(product_id):
    product = Product.query.get(product_id)
    print(product)
    return render_template("product/view_product.html", product=product)