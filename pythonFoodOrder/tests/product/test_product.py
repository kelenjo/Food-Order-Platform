
def test_view(client):
    response = client.get('/view/1')

    assert response.status_code == 200

    assert b"11.0" in response.data

    response = client.get('/view/7')

    assert response.status_code == 200

    assert b"Product not found" in response.data


