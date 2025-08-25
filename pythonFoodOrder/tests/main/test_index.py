# from tests.conftest import client, app, server


def test_main(client):
    response = client.get('/')
    assert response.status_code == 200


def test_feedback(client):
    response = client.get('/feedback')
    assert response.status_code == 200

