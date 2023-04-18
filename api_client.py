from typing import Any, Dict, Optional
import requests
import logging

from utils.exceptions import InvalidEndpointException, InvalidHTTPMethodExceptions

class ApiClient:
    """
    A client for interacting with an API.

    Args:
        base_url (str): The base URL of the API.

    Attributes:
        base_url (str): The base URL of the API.
        logger (logging.Logger): A logger for logging messages.
    Raises:
        InvalidEndpointException: If the endpoint is invalid.
        InvalidHTTPMethodExceptions: If the HTTP method is not allowed.
    """
    allowed_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    def __init__(self, base_url):
        """
        Initializes an instance of ApiClient.

        Args:
            base_url (str): The base URL of the API.
        """
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)
  
    def request(self, method, endpoint, headers=None, params=None, json=None):
        """
        Sends a request to the API.

        Args:
            method (str): The HTTP method to use.
            endpoint (str): The endpoint to send the request to.
            headers (Optional[Dict[str, str]]): The headers to include in the request.
            params (Optional[Dict[str, Any]]): The query parameters to include in the request.
            json (Optional[Dict[str, Any]]): The JSON payload to include in the request.

        Returns:
            The response from the API.

        Raises:
            InvalidEndpointException: If the endpoint is invalid.
            InvalidHTTPMethodExceptions: If the HTTP method is not allowed.
        """
        url = self._construct_url(endpoint)
        self._validate_method(method)

        self.logger.info(f'Sending {method} request to {url}')
        try:
            response = requests.request(method, url, headers=headers, params=params, json=json)
            self.logger.info(f'Received {response.status_code} response from {url}')
            return response
        except requests.exceptions.HTTPError:
            raise InvalidEndpointException(f"Invalid endpoint: {url}")
        except requests.exceptions.InvalidSchema:
            raise InvalidHTTPMethodExceptions(f"Invalid HTTP method: {method}")
    
    def _construct_url(self, endpoint):
        """
        Constructs a URL for the given endpoint.

        Args:
            endpoint (str): The endpoint to construct the URL for.

        Returns:
            The URL for the given endpoint.

        Raises:
            InvalidEndpointException: If the endpoint is invalid.
        """
        if not endpoint.startswith('/'):
            self.logger.warning('Endpoint does not start with a /')
            raise InvalidEndpointException('Endpoint must start with a /')

        return self.base_url + endpoint
    
    def _validate_method(self, method):
        """
        Validates the given HTTP method.

        Args:
            method (str): The HTTP method to validate.

        Raises:
            InvalidHTTPMethodExceptions: If the HTTP method is not allowed.
        """
        if method not in self.allowed_methods:
            self.logger.warning(f'{method} is not a valid HTTP method')
            raise InvalidHTTPMethodExceptions(f'{method} is not a valid HTTP method')

    def get(self, endpoint: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None):
        """
        Send a GET request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            headers (Optional[Dict[str, str]]): A dictionary of headers to send with the request.
            params (Optional[Dict[str, Any]]): A dictionary of query parameters to send with the request.

        Returns:
            The response object returned by the API.

        Raises:
            InvalidEndpointException: If the endpoint is not valid.
            InvalidHTTPMethodExceptions: If the HTTP method is not valid.
        """
        return self.request('GET', endpoint, headers=headers, params=params)

    def post(self, endpoint: str, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None):
        """
        Send a POST request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            headers (Optional[Dict[str, str]]): A dictionary of headers to send with the request.
            json (Optional[Dict[str, Any]]): A dictionary of JSON data to send with the request.

        Returns:
            The response object returned by the API.

        Raises:
            InvalidEndpointException: If the endpoint is not valid.
            InvalidHTTPMethodExceptions: If the HTTP method is not valid.
        """
        return self.request('POST', endpoint, headers=headers, json=json)

    def put(self, endpoint: str, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None):
        """
        Send a PUT request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            headers (Optional[Dict[str, str]]): A dictionary of headers to send with the request.
            json (Optional[Dict[str, Any]]): A dictionary of JSON data to send with the request.

        Returns:
            The response object returned by the API.

        Raises:
            InvalidEndpointException: If the endpoint is not valid.
            InvalidHTTPMethodExceptions: If the HTTP method is not valid.
        """
        return self.request('PUT', endpoint, headers=headers, json=json)

    def patch(self, endpoint: str, headers: Optional[Dict[str, str]] = None, json: Optional[Dict[str, Any]] = None):
        """
        Send a PATCH request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            headers (Optional[Dict[str, str]]): A dictionary of headers to send with the request.
            json (Optional[Dict[str, Any]]): A dictionary of JSON data to send with the request.

        Returns:
            The response object returned by the API.

        Raises:
            InvalidEndpointException: If the endpoint is not valid.
            InvalidHTTPMethodExceptions: If the HTTP method is not valid.
        """
        return self.request('PATCH', endpoint, headers=headers, json=json)

    def delete(self, endpoint:str, headers: Optional[Dict[str, str]] = None):
        """
        Send a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            headers (Optional[Dict[str, str]]): A dictionary of headers to send with the request.

        Returns:
            The response object returned by the API.

        Raises:
            InvalidEndpointException: If the endpoint is not valid.
            InvalidHTTPMethodExceptions
        """
        return self.request('DELETE', endpoint, headers=headers)