# CRUD API

Create Read Update Delete

## Table of Contents

- [Getting Started](#getting-started)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [1. Home (GET)](#1-home-get)
  - [2. Login (POST)](#2-login-post)
  - [3. Sign Up (POST)](#3-sign-up-post)
  - [4. Get Task (GET)](#4-get-task-get)
  - [5. Create Task (POST)](#5-create-task-post)
  - [6. Update Task (PUT)](#6-update-task-put)
  - [7. Delete Task (DELETE)](#7-delete-task-delete)

## Getting Started

To set up and run the API locally for development.

```bash
    # Clone the repository
    git clone https://github.com/yourusername/your-api.git
    cd your-api

    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate    # Windows

    # Install dependencies
    pip install -r requirements.txt

    # Run the application
    python main.py



    ## Viewing The App

    Go to `http://127.0.0.1:5000`

```

## Endpoints

List of all API endpoints.

#### 1. Home (GET)

- URL: /
- Request: None
- Response:
- Status Code: 200 OK

#### 2. Login (POST)

- URL: /login
- Request:

  - Content Type: application/json
  - Request Body:

  ```bash
      {
      "email": "user@example.com",
      "password": "password123"
      }
  ```

- Response:
  - Status Code: 200 OK

#### 3. Sign Up (POST)

- URL: /sign-up
- Request:

  - Content Type: application/json
    -Request Body:

  ```bash
      {
      "email": "newuser@example.com",
      "password": "newpassword123",
      "name": "New User"
      }

  ```

- Response:
  - Status Code: 201 Created

#### 4. Get Task (GET)

- URL: /tasks/{id}
- Request: None
- Response
  - Status Code: 200 OK
    Content: Describe the expected response data.

#### 5. Create Task (POST)

- URL: /tasks
- Request:

  - Content Type: application/json
  - Request Body:

  ```bash
      {
      "description": "Task description"
      }

  ```

- Response:
  - Status Code: 201 Created

#### 6. Update Task (PUT)

- URL: /tasks/{id}
- Request:

  - Content Type: application/json
  - Request Body:

  ```bash

      {
      "description": "Updated task description"
      }
  ```

- Response:
  - Status Code: 200 OK

##### 7. Delete Task (DELETE)

- URL: /tasks/{id}
- Request: None
- Response:
  - Status Code: 204 No Content

## Design Choices and Development Challenges for Flask API:

### Design Choices:

- Flask Framework: I chose Flask as the web framework for building this API due to its simplicity and flexibility. Flask allows for rapid development while providing essential tools for creating web applications.

- RESTful Architecture: I followed a RESTful architecture for designing the API endpoints. Each endpoint is named logically and performs specific actions. RESTful design makes it easier for developers to understand and use the API.

- Authentication: I implemented user authentication using Flask-Login. Users can log in, sign up, and access protected routes based on their login status.

- Database: SQLAlchemy is used as the Object-Relational Mapping (ORM) tool to interact with the database. It allows for easy manipulation of data models and database operations.

- Unit Testing: I integrated unit tests to ensure the correctness of the API endpoints. Unit tests help identify issues early in development and maintain the reliability of the API.

### Development Challenges:

- Authentication and Security: Implementing secure authentication and authorization mechanisms was a crucial challenge. I had to ensure that user data remains confidential and that only authorized users can access certain routes.

- Database Schema: Designing an appropriate database schema for the application's needs required careful consideration. Defining relationships between tables, setting up foreign keys, and handling migrations were part of this challenge.

- Error Handling: Implementing effective error handling and providing informative error messages to clients was a challenge. Ensuring that the API returns appropriate error responses for various scenarios, including validation errors and unauthorized access, required attention to detail.

- Unit Testing: Writing unit tests for all API endpoints and ensuring comprehensive test coverage was time-consuming but necessary. Ensuring that the tests accurately reflect the behavior of the endpoints and are maintainable was a challenge.

- Documentation: Creating clear and concise documentation for the API, including usage examples and sample requests/responses, is essential but can be a time-consuming task.

- Frontend Integration: If integrating the API with a frontend application, ensuring that the API endpoints align with frontend requirements and data structures is important. This requires close collaboration between frontend and backend developers.
