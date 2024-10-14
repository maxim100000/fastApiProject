from .database_setup import client 


def test_post_user():
    response = client.post("/users", json={"name": "John Doe", "email": "j@j.com"})
    assert response.status_code == 200 

def test_get_user():
    response = client.get("/users")
    assert response.status_code == 200
    
def test_update_user():
    response = client.patch("/users/2", json={"email": "grut@g.com"})
    assert response.status_code == 200    
    
def test_delete_user():
    response = client.delete("/users/2")
    assert response.status_code == 200    
    