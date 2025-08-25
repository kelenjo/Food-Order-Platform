from flask_login import current_user
from src.models import User


def test_login(client):
    with client:
        client.post("/login", data={"username": "mari", "password": "Mari123"})
        print(client.get().data)
        assert current_user.is_authenticated == True

        client.get('/logout')
        assert current_user.is_authenticated == False

        client.post("/login", data={"username": "mari", "password": "Mari13"})
        print(client.get().data)
        assert current_user.is_authenticated == False


def test_register_get(client):
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data or b"username" in response.data


def test_register_post_valid(client, app):
    response = client.post("/register", data={
        "username": "gio",
        "email": "gio@gmail.com",
        "password": "Gio123"
    }, follow_redirects=True)

    assert b"Sagol shen daregistrirdi" in response.data

    with app.app_context():
        user = User.query.filter_by(username="gio").first()
        assert user is not None
        assert user.email == "gio@gmail.com"


def test_logout(client, app):
    # with app.app_context():
    #     user = User("mari", "mari@gmail.com", "Mari123")
    #     user.create()

    with client:
        client.post("/login", data={"username": "mari", "password": "Mari123"})
        assert current_user.is_authenticated == True

        response = client.get("/logout", follow_redirects=True)
        assert not current_user.is_authenticated


def test_edit(client, app):

    with client:
        client.post("/login", data={"username": "mari", "password": "Mari123"})

        client.post("/edit/1", data={"username": "marikuna", "email": "mari@gmail.com", "password": "Mari1234"})

    with app.app_context():
        user = User.query.get(1)
        assert user.username=="marikuna"


def test_delete(client, app):

    with client:
        client.post("/login", data={"username": "mari", "password": "Mari123"})
        response = client.get(f'/delete/{1}', follow_redirects=True)
        assert response.status_code == 200

    with app.app_context():
        user = User.query.get(1)
        assert user is None


