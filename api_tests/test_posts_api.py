def test_get_posts(api_client):
    """
    Test GET request to retrieve all posts.

    :param api_client: Test client for API requests.
    """
    response = api_client.get('/posts') 
    response = api_client
    # Assert the status code
    assert response.status_code == 200
    response_body = response.json()
    # Assert each entry has the expected format
    for entry in response_body:
        assert 'userId' in entry
        assert 'id' in entry
        assert 'title' in entry
        assert 'body' in entry

def test_get_post_by_id(api_client):
    """
    Test GET request to retrieve a post by its ID.

    :param api_client: Test client for API requests.
    """
    # Define the ID of the post to retrieve
    post_id = 1
    response = api_client.get(f'/posts/{post_id}') 
    # Assert the status code
    assert response.status_code == 200
    # Assert the response data
    response_body = response.json()
    assert response_body['id'] == post_id
    assert 'userId' in response_body
    assert 'title' in response_body
    assert 'body' in response_body

def test_create_post(api_client):
    """
    Test POST request to create a new post.

    :param api_client: Test client for API requests.
    """
    # Define data to post
    post_data = {
        "id": 101,
        "title": "James Walmsley",
        "body": "empty body for testing"
    }

    # Sent the POST request to create the post
    response = api_client.post("/posts", json=post_data)
    
    # Assert the status code
    assert response.status_code == 201
    # Assert the response data
    response_body = response.json()

    assert 'id' in response_body
    assert response_body['id'] == post_data['id']
    assert response_body['title'] == post_data['title']
    assert response_body['body'] == post_data['body']
    

def test_update_post(api_client):
    """
    Test PUT request to update an existing post.

    :param api_client: Test client for API requests.
    """
    post_id = 1

    post_data = {
        "title": "Changing your name",
        "body": "this is an updated body"
    }

    response = api_client.put(f'/posts/{post_id}', json=post_data)
    # Assert the status code
    assert response.status_code == 200
    # Assert the response data
    response_body = response.json()
    assert response_body['id'] == 1
    assert response_body['title'] == post_data['title']
    assert response_body['body'] == post_data['body']

def test_partial_update_post(api_client):
    """
    Test PATCH request to partially update an existing post.

    :param api_client: Test client for API requests.
    """
    post_id = 1
    # Define the data to send in the request body
    post_data = {
        "title": "Updated Post Title"
    } 
    # Send a PATCH request to partially update an exisiting post
    response = api_client.patch(f'/posts/{post_id}', json=post_data)
    # Assert the status code
    assert response.status_code == 200
    # Assert the response data
    response_body = response.json()
    assert response_body['id'] == 1
    assert response_body['title'] == post_data['title']
    assert 'body' in response_body.keys()

def test_delete_post(api_client):
    """
    Test deleting a post via DELETE request.

    Args:
        api_client: An instance of the API client.

    Returns:
        None

    Raises:
        AssertionError: If the status code of the response is not 200, or if the status code of the GET request to the
        deleted post endpoint is not 404.

    """
    post_id = 101
    # Send a DELETE request to delete an exisiting post
    response = api_client.delete(f'/posts/{post_id}')
    # Assert the status code
    assert response.status_code == 200
    
    # Assert that the post has been deleted by sending a GET request
    response = api_client.get(f'/posts/{post_id}')
    assert response.status_code == 404
    