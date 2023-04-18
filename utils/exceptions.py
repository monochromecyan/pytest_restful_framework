class InvalidEndpointException(Exception):
    """
    Exception raised when an invalid endpoint is used in a request.

    Args:
        endpoint (str): The invalid endpoint used in the request.
    """
    def __init__(self, endpoint):
        self.endpoint = endpoint
    
    def __str__(self):
        return f"Invalid endpoint: {self.endpoint}"

class InvalidHTTPMethodExceptions(Exception):
    """
    Exception raised when an invalid HTTP method is used in a request.

    Args:
        method (str): The invalid HTTP method used in the request.
    """
    def __init__(self, method):
        self.method = method
        
    def __str__(self):
        return f"Invalid method: {self.method}"
    
class InvalidRequestParameterException(Exception):
    """
    Exception raised when an invalid HTTP method is used in a request.

    Args:
        method (str): The invalid HTTP method used in the request.
    """
    def __init__(self, message, parameter):
        self.message = message
        self.parameter = parameter

    def __str__(self):
        return f'{self.message}: {self.parameter}'