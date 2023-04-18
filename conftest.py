import pytest
from api_client import ApiClient
from utils.exceptions import InvalidEndpointException, InvalidHTTPMethodExceptions

@pytest.fixture
def api_client():
    """Fixture that returns an instance of the ApiClient class with base_url as 'https://jsonplaceholder.typicode.com'."""
    return ApiClient(base_url='https://jsonplaceholder.typicode.com')

@pytest.fixture(autouse=True)
def catch_exceptions(request):
    """Fixture that catches and fails the test if InvalidEndpointException or InvalidHTTPMethodExceptions is raised.

    Args:
        request: Fixture request object.

    Raises:
        InvalidEndpointException: If an invalid endpoint is provided.
        InvalidHTTPMethodExceptions: If an invalid HTTP method is used.
    """
    try:
        yield
    except (InvalidEndpointException, InvalidHTTPMethodExceptions) as e:
        pytest.fail(str(e))