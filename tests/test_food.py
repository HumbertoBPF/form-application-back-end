from database.db import DB

url = "/getAlimentacao"


def test_food(client):
    response = client.get(url)
    assert response.status_code == 200
    assert response.json == DB
