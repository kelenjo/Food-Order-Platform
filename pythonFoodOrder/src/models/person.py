from src.ext import db
from src.models import BaseModel


class Person(BaseModel):

    __tablename__ = "persons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    birthday = db.Column(db.Date)

    idcard_id = db.Column(db.Integer, db.ForeignKey("idcards.id"))

    idcard = db.relationship("IDcard", back_populates="person")


class IDcard(BaseModel):

    __tablename__ = "idcards"
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String)
    expiry_data = db.Column(db.Date)

    person = db.relationship("Person", back_populates="idcard", uselist=False)

