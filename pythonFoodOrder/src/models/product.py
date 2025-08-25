from src.ext import db
from src.models import BaseModel


class Product(BaseModel):

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    description = db.Column(db.String)
    image = db.Column(db.String)

    def __init__(self, name, price, description, image):
        self.name = name
        self.price = price
        self.description = description
        self.image = image

    def __repr__(self):
        return f"This is {self.name} and costs {self.price}$"

