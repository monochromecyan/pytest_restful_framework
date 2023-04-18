import pytest
from utils.exceptions import InvalidEndpointException, InvalidHTTPMethodExceptions, InvalidRequestParameterException


def test_create_post_negative(api_client):
    """
    Test negative cases for creating a post.

    Args:
        api_client: An instance of the API client.

    Raises:
        InvalidEndpointException: If the endpoint is invalid.
        InvalidHTTPMethodExceptions: If the HTTP method is invalid.
    """
    # Attempt to create a post with missing or invalid data
    with pytest.raises(InvalidEndpointException):
        api_client.post('/invalid-endpoint', json={})
    
    with pytest.raises(InvalidHTTPMethodExceptions):
        api_client.post('/posts', json={}, method='INVALID_METHOD')

def test_get_post_negative(api_client):
    """
    Test negative cases for retrieving a post.

    Args:
        api_client: An instance of the API client.

    Raises:
        InvalidEndpointException: If the endpoint is invalid.
    """
    with pytest.raises(InvalidEndpointException):
        # Attempt to retrieve a post that doesn't exist
        api_client.get('/posts/999')
    
    with pytest.raises(InvalidEndpointException):
        # Attempt to retrieve a post with an invalid endpoint
        api_client.get('/invalid')
    
def test_update_post_negative(api_client):
    """
    Test negative cases for updating a post.

    Args:
        api_client: An instance of the API client.

    Raises:
        InvalidEndpointException: If the endpoint is invalid.
        InvalidHTTPMethodExceptions: If the HTTP method is invalid.
    """
    with pytest.raises(InvalidEndpointException):
        # Attempt to update a post that doesn't exist
        api_client.put('/posts/9990', json={"id": 101, "title": "Wallie", "body": "This is not here"})
    
    with pytest.raises(InvalidEndpointException):
        # Attempt to update a post with an invalid endpoint
        api_client.put('/invalid', json={"id": 101, "title": "Wallie", "body": "This is not here"})
    
    with pytest.raises(InvalidHTTPMethodExceptions):
        # Attempt to update a post using an invalid HTTP method
        api_client.post('/posts/1', json={"id": 101, "title": "Wallie", "body": "This is not here"})

def test_get_invalid_endpoint(api_client):
    """
    Test for an invalid endpoint.

    Args:
        api_client: An instance of the API client.

    Raises:
        InvalidEndpointException: If the endpoint is invalid.
    """
    endpoint = "/invalid_endpoint"
    with pytest.raises(InvalidEndpointException) as execinfo:
        api_client.get(endpoint=endpoint)
    assert "Invalid endpoint" in str(execinfo.value)

def test_get_posts_invalid_parameter(api_client):
    """
    Test for an invalid parameter when retrieving posts.

    Args:
        api_client: An instance of the API client.

    Raises:
        InvalidRequestParameterException: If the request parameter is invalid.
    """
    # Attempt to retrieve posts with an invalid parameter
    with pytest.raises(InvalidRequestParameterException):
        api_client.get('/posts?invalid_param=1')
