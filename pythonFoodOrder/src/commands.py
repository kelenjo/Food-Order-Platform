from flask.cli import with_appcontext
import datetime
import click
from src.ext import db
from src.models import Product, Person, IDcard, User


def init_db():

    db.drop_all()
    db.create_all()


@click.command("init_db")
@with_appcontext
def init_db_command():
    click.echo("Initializing db...")

    init_db()

    click.echo("Initializing is over!")


def populate_db():
    products = [
        {
            "id": 0,
            "name": "შაურმა პატარა",
            "price": 11,
            "image": "shaurma.jfif",
            "description": "ლავაში, ღორის ხორცი 200გ, პომიდორი, ხახვი, სალათის ფურცელი(აისბერგი), წიწაკა, მაიონეზი, კეტჩუპი"
        },
        {
            "id": 1,
            "name": "შაურმა სტანდარტი",
            "price": 13,
            "image": "shaurma.jfif",
            "description": "ლავაში, ღორის ხორცი 250გ, პომიდორი, ხახვი, სალათის ფურცელი(აისბერგი), წიწაკა, მაიონეზი, კეტჩუპი"
        },
        {
            "id": 2,
            "name": "შაურმა დიდი",
            "price": 18,
            "image": "shaurma.jfif",
            "description": "ლავაში, ღორის ხორცი 300გ, პომიდორი, ხახვი, სალათის ფურცელი(აისბერგი), წიწაკა, მაიონეზი, კეტჩუპი"
        },
        {
            "id": 3,
            "name": "კოლა",
            "price": 3,
            "image": "cola.jfif",
            "description": "ცივი გაზიანი სასმელი, კოკა-კოლა 500მლ"
        },
        {
            "id": 4,
            "name": "სპრაიტი",
            "price": 3,
            "image": "sprite.jfif",
            "description": "ცივი გაზიანი სასმელი, სპრაიტი 500მლ"
        },
        {
            "id": 5,
            "name": "ბურგერი",
            "price": 10,
            "image": "burger.png",
            "description": "ბურგერის ბული, ღორის ხორცი 200გ, ყველი, პომიდორი, სალათის ფურცელი, კეტჩუპი, მაიონეზი"
        }
    ]

    for product in products:
        new_product = Product(name=product["name"], price=product["price"], description=product["description"],
                              image=product["image"])
        db.session.add(new_product)

    idcard = IDcard(serial_number="01201115242", expiry_data=datetime.datetime.now())
    db.session.add(idcard)
    db.session.commit()
    person = Person(name="Giorgi", surname="Kelenjeridze", birthday=datetime.datetime.now(), idcard_id=idcard.id)
    db.session.add(person)
    user = User("mari", "marikuna@gmail.com", "Mari123")
    db.session.add(user)
    db.session.commit()


@click.command("populate_db")
@with_appcontext
def populate_db_command():

    populate_db()




