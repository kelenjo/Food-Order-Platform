from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
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
    cart_items = Cart.query.filter_by(user_id=current_user.id).order_by(Cart.id.asc()).all()
    total_price = 0
    for item in cart_items:
        total_price += Product.query.get(item.product_id).price * item.quantity
    return render_template('product/cart.html', cart_items=cart_items, total_price=total_price)


@product_blueprint.route('/add-to-cart/<int:product_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)

    # Check if item already in cart
    cart_item = Cart.query.filter_by(user_id=current_user.id, product_id=product.id).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = Cart(user_id=current_user.id, product_id=product.id, quantity=1)
        cart_item.create()

    # flash(f"{product.name} added to your cart!", "success")
    return redirect(url_for('product.menu', added=product.name))


@product_blueprint.route('/remove_from_cart', methods=['POST'])
@login_required
def remove_from_cart():
    data = request.get_json()
    item = Cart.query.get(data.get('item_id'))
    if item and item.user_id == current_user.id:
        item.delete()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})


@product_blueprint.route('/update_cart_quantity', methods=['POST'])
@login_required
def update_cart_quantity():
    data = request.get_json()
    item = Cart.query.get(data.get('item_id'))
    if item and item.user_id == current_user.id:
        item.quantity = int(data.get('quantity', 1))
        item.save()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})


@product_blueprint.route("/product/<int:product_id>")
def view(product_id):
    product = Product.query.get(product_id)
    print(product)
    return render_template("product/view_product.html", product=product)


@product_blueprint.context_processor
def cart_context():
    if current_user.is_authenticated:
        cart_items = Cart.query.filter_by(user_id=current_user.id).all()
        cart_count = sum(item.quantity for item in cart_items)
    else:
        cart_count = 0
    return dict(cart_count=cart_count)
