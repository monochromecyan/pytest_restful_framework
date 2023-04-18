# Test Framework

This is a test framework for testing API endpoints using Python and Pytest. The tests are executed using an API client to send HTTP requests and validate the responses.

## Prerequisites

To run this test framework, you will need to have the following installed on your Windows machine:

- Python 3
- Docker Desktop

## Assumptions and Challenges

There is not much error handling from `https://jsonplaceholder.typicode.com` so all of my negative tests fail. In normal circumstances I would not include these but I wanted to include the logic of what these tests could be like.

Further to this I would include unit testing for the api_client class to ensure ensure that the code was production ready.

### Design of Framework

The framework has two core directories, `api_tests` containing all api tests and `utils` which houses all the exception classes.

At the root of the test framework, we have the ApiClient which makes use of OOP, allowing the tests to reuse requests.

The `conftest.py` contains the fixtures for the framework, such as the `baseUrl`.

As stated below this framework makes use of Docker, as well as the implmentation of CircleCI.

## Installation and Running Tests

1. Clone the repository to your local machine.
2. Open a command prompt or PowerShell terminal in the root directory of the project.
3. Create a virtual environment for the project by running the following command:

```bash
python -m venv venv
```

4. Activate the virtual environment by running the following command:

```bash
venv\Scripts\activate
```

5. Install the required Python packages by running the following command:

```bash
pip install -r requirements.txt
```

6. To run the tests using Pytest, activate the virtual environment by running the following command:

```bash
pytest -s
```

Pytest will discover and execute all the tests in the `api_tests` directory. The test results will be displayed in the terminal.

## Using Docker and running tests

6. Build the Docker image for the API client by running the following command:

```bash
docker build -t api_client .
```

7. Run the tests by running the Docker container based on the image you just built:

```bash
docker run api_client
```

### Docker Cleanup

To stop and clean up all your Docker resources, you can use the following commands:

1. Stop all running containers:

```bash
docker stop $(docker ps -aq)
```

2. Remove all stopped containers:

```bash
docker rm $(docker ps -aq)
```

3. Remove all images:

```bash
docker rmi $(docker images -q)
```

### CircleCI integration

You can access the CircileCI builds here `https://app.circleci.com/pipelines/github/monochromecyan`. Permission will need to be granted by the author to view them.

## Configuration

The API client is configured to use the https://jsonplaceholder.typicode.com as the base URL for the API requests. If you need to test a different API, you can modify the `base_url` parameter in the `ApiClient` constructor.

## Troubleshooting

#### 'docker' is not recognized as the name of a cmdlet, function, script file, or operable program

If you get this error when trying to run the Docker build command, make sure that Docker Desktop is installed and running on your machine. You can download Docker Desktop from the official website at https://www.docker.com/products/docker-desktop.

#### Pytest is not recognized as a command

If you get this error when trying to run the Pytest command, make sure that Pytest is installed in the virtual environment. You can install it by running the following command:

```bash
pip install pytest
```
