from .database_setup import client

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200