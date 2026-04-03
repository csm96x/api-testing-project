import requests

def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
	    
    assert response.status_code == 200
	
    data = response.json()
	
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    
    
def test_create_post():
    response= requests.post(     "https://jsonplaceholder.typicode.com/posts",
    json={
        "title": "test",
        "body": "hello",
        "userID": 1
    }
   )
    
    assert response.status_code==201
    
    data = response.json()
    assert data["title"] == "test"
    
    
    
def test_post_content():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    
    assert response.status_code == 200
    
    data= response.json()
    
    assert data["id"]==1
    assert "title" in data
    assert "body" in data
    
    
    
    
    
def test_invalid_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
    
    assert response.status_code == 404