def test_index_success(client):
    # Test for page loading
    response = client.get("/")
    assert response.status_code == 200


def test_joinpage_success(client):
    # Test for joinpage loading
    response = client.get("/joinpage")
    assert response.status_code == 200


def test_index_content(client):
    # Returns main text in index/home page
    response = client.get("/")
    assert b"Your one stop forum for everthing flat-sharing related" in response.data
