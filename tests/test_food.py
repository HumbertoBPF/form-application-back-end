from database.db import DB


def test_food(client):
    response = client.get("/getAlimentacao")
    assert response.status_code == 200
    assert response.json == DB
