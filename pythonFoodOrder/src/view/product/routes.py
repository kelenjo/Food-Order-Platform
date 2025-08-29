from flask import Blueprint, render_template
from src.models.product import Product, Category

product_blueprint = Blueprint("product", __name__)


@product_blueprint.route("/menu")
def menu():
    categories = Category.query.all()

    products = Product.query.all()

    return render_template("product/menu.html", categories=categories, products=products)


@product_blueprint.route("/product/<int:product_id>")
def view(product_id):
    product = Product.query.get(product_id)
    print(product)
    return render_template("product/view_product.html", product=product)