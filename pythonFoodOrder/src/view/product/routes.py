from flask import Blueprint, render_template, jsonify, request
from flask_login import current_user, login_required
from src.models.product import Product, Category, Cart

product_blueprint = Blueprint("product", __name__)


@product_blueprint.route("/menu")
def menu():
    categories = Category.query.all()

    products = Product.query.all()

    return render_template("product/menu.html", categories=categories, products=products)


@product_blueprint.route('/cart')
@login_required
def cart():
    cart_items = current_user.cart
    total_price = sum(item.quantity * item.products.price for item in cart_items)
    return render_template('product/cart.html', cart_items=cart_items, total_price=total_price)


@product_blueprint.route('/add-to-cart', methods=['POST'])
@login_required
def add_to_cart():
    data = request.get_json()
    item_id = data.get('item_id')
    product = Product.query.get(item_id)

    if not product:
        return jsonify({'status': 'error'})

    # Check if item already in cart
    cart_item = Cart.query.filter_by(user_id=current_user.id, product_id=product.id).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = Cart(user_id=current_user.id, product_id=product.id, quantity=1)
        cart_item.create()

    return jsonify({'status': 'success', 'item_name': product.name})


@product_blueprint.route("/product/<int:product_id>")
def view(product_id):
    product = Product.query.get(product_id)
    print(product)
    return render_template("product/view_product.html", product=product)