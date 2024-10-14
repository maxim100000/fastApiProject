from .database_setup import client

def test_post_car():
    response = client.post("/cars", json={"name": "Ferrari", "brand": "Ferrari",
                                          "year": 2020})
    assert response.status_code == 200


def test_get_car():
    response = client.get("/cars")
    assert response.status_code == 200
