from src.ext import db
from src.models import BaseModel


class Product(BaseModel):

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    description = db.Column(db.String)
    image = db.Column(db.String)

    category_id = db.Column(db.Integer, db.ForeignKey('Categories.id'), nullable=False)
    categories = db.relationship("Category", back_populates="products")
    cart = db.relationship("Cart", back_populates="products")

    def __init__(self, name, price, description, image, category_id):
        self.name = name
        self.price = price
        self.description = description
        self.image = image
        self.category_id = category_id

    def __repr__(self):
        return f"This is {self.name} and costs {self.price}$"


class Category(BaseModel):

    __tablename__ = "Categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    products = db.relationship("Product", back_populates="categories")


class Offer(BaseModel):

    __tablename__ = "offers"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)  # path to static image
    active = db.Column(db.Boolean, default=True)

    def __init__(self, title, description, image, active):
        self.title = title
        self.description = description
        self.image = image
        self.active = active

    def __repr__(self):
        return f"This is offer: {self.title}"


class Cart(BaseModel):

    __tablename__ = "Cart"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, default=1)

    users = db.relationship("User", back_populates="cart")
    products = db.relationship("Product", back_populates="cart")

