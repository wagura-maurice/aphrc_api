# Practical Assessment: Blogging Platform

This assessment constitutes 55% of the interview evaluation.

## Requirements:
- Python/Django
- Vue.js
- CSS

## Description:
Create a simple blogging platform using Python/Django, Vue.js, and CSS. The platform should fulfill the following requirements:

1. **Backend Functionality**:
   - Allow users to create blog titles, categories, bodies, and specify the date created, date updated, and creator.
   
2. **Frontend Display**:
   - Display blogs as articles in 2 columns with 6 blogs per page.
   - Implement pagination to enable users to view more blogs.
   
3. **Article Details**:
   - Allow users to view each blog article in detail.
   - Display the blog title, category, article content, date created, and creator.

## Features:

### 1. Catalogs
- **List and Create Catalogs**: Users can view a list of catalogs and create new catalogs.
- **Retrieve, Update, and Delete Catalogs**: Users can retrieve, update, or delete specific catalogs.

### 2. Categories
- **List and Create Categories**: Users can view a list of categories and create new categories.
- **Retrieve, Update, and Delete Categories**: Users can retrieve, update, or delete specific categories.

### 3. User Authentication
- **User Sign-In**: Users can sign in to the platform.
- **User Sign-Out**: Users can sign out of the platform.

## Endpoints:

### Catalogs
- **List and Create Catalogs**: `/api/post/catalogs/` (GET, POST)
- **Retrieve, Update, and Delete Catalogs**: `/api/post/catalogs/<int:pk>/` (GET, PUT/PATCH, DELETE)

### Categories
- **List and Create Categories**: `/api/post/categories/` (GET, POST)
- **Retrieve, Update, and Delete Categories**: `/api/post/categories/<int:pk>/` (GET, PUT/PATCH, DELETE)

### User Authentication
- **User Sign-In**: `/api/auth/sign-in/` (POST)
- **User Sign-Out**: `/api/auth/sign-out/` (POST)

## Blogging Platform

This is a simple blogging platform developed using Python/Django, CSS, and Vue.js.

### Features:

#### 1. Catalogs
- **List and Create Catalogs**: Users can view a list of catalogs and create new catalogs.
  - **Endpoint**: `/api/post/catalogs/`
  - **Method**: GET (List), POST (Create)
  - **Example Request**: `GET /api/post/catalogs/`
  - **Example Response**:
    ```json
    [
        {
            "id": 1,
            "title": "Sample Catalog 1",
            "content": "This is a sample catalog content.",
            "created_at": "2024-03-18T08:00:00Z",
            "updated_at": "2024-03-18T08:00:00Z",
            "owner": "user1@example.com",
            "category": "Category A"
        },
        {
            "id": 2,
            "title": "Sample Catalog 2",
            "content": "This is another sample catalog content.",
            "created_at": "2024-03-18T09:00:00Z",
            "updated_at": "2024-03-18T09:00:00Z",
            "owner": "user2@example.com",
            "category": "Category B"
        },
        ...
    ]
    ```

- **Retrieve, Update, and Delete Catalogs**: Users can retrieve, update, or delete specific catalogs.
  - **Endpoint**: `/api/post/catalogs/<int:pk>/`
  - **Method**: GET (Retrieve), PUT/PATCH (Update), DELETE (Delete)
  - **Example Request**: `GET /api/post/catalogs/1/`
  - **Example Response**:
    ```json
    {
        "id": 1,
        "title": "Sample Catalog 1",
        "content": "This is a sample catalog content.",
        "created_at": "2024-03-18T08:00:00Z",
        "updated_at": "2024-03-18T08:00:00Z",
        "owner": "user1@example.com",
        "category": "Category A"
    }
    ```

#### 2. Categories
- **List and Create Categories**: Users can view a list of categories and create new categories.
  - **Endpoint**: `/api/post/categories/`
  - **Method**: GET (List), POST (Create)
  - **Example Request**: `GET /api/post/categories/`
  - **Example Response**:
    ```json
    [
        {
            "id": 1,
            "name": "Category A",
            "description": "This is Category A"
        },
        {
            "id": 2,
            "name": "Category B",
            "description": "This is Category B"
        },
        ...
    ]
    ```

- **Retrieve, Update, and Delete Categories**: Users can retrieve, update, or delete specific categories.
  - **Endpoint**: `/api/post/categories/<int:pk>/`
  - **Method**: GET (Retrieve), PUT/PATCH (Update), DELETE (Delete)
  - **Example Request**: `GET /api/post/categories/1/`
  - **Example Response**:
    ```json
    {
        "id": 1,
        "name": "Category A",
        "description": "This is Category A"
    }
    ```

### Authentication

#### 1. User Sign-Up
- **Sign-Up**: Users can sign up for an account on the platform.
  - **Endpoint**: `/api/auth/sign-up/`
  - **Method**: POST
  - **Request Body**:
    ```json
    {
        "username": "new_user",
        "email": "new_user@example.com",
        "password": "new_password"
    }
    ```
  - **Example Response**:
    ```json
    {
        "message": "User successfully registered."
    }
    ```

#### 2. User Sign-In
- **Sign-In**: Users can sign in to the platform.
  - **Endpoint**: `/api/auth/sign-in/`
  - **Method**: POST
  - **Request Body**:
    ```json
    {
        "username": "user1",
        "password": "password123"
    }
    ```
  - **Example Response**:
    ```json
    {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMSwidXNlcm5hbWUiOiJ1c2VyMSIsImV4cCI6MTY0NzEzMDY0OSwiZW1haWwiOiJ1c2VyMUBleGFtcGxlLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc19hZG1pbiI6dHJ1ZX0.m7heEslklOQzJ0WkQD9vV_cX6Q1tySpsdrZaYK6wRNE",
        "message": "Sign-in successful."
    }
    ```

#### 3. User Sign-Out
- **Sign-Out**: Users can sign out of the platform.
  - **Endpoint**: `/api/auth/sign-out/`
  - **Method**: POST
  - **Example Request**: `POST /api/auth/sign-out/`
  - **Example Response**:
    ```json
    {
        "message": "Sign-out successful."
    }
    ```
    
## Conclusion:
This assessment evaluates your ability to develop a simple blogging platform using Python/Django, Vue.js, and CSS. Make sure to demonstrate proficiency in backend development, frontend design, and user authentication.
