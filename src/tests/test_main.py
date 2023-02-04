

def test_root(test_main):
    response = test_main.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello EMN"}