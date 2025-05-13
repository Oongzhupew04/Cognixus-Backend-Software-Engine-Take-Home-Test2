# Cognixus-Backend-Software-Engine-Take-Home-Test

## Prerequisites

* Python 3.10+
* Flask
* SQLite
* Git

## Installation

1. Install Flask (Core Framework):

    ```bash
   pip install Flask
   ```

2. Install Flask-SQLAlchemy (for database management):

   ```bash
   pip install Flask-SQLAlchemy
   ```
3. Install Flask-Login (For user authentication):

   ```bash
   pip install Flask-Login
   ```
4. Install Flask-WTF (For form handling, if you are using WTForms):

     ```bash
     pip install Flask-WTF
     ```
  
5. Install Flask-CORS (If you plan to handle cross-origin requests):

   ```bash
   pip install Flask-CORS
   ```
   
6. Install SQLAlchemy (Automatically installed with Flask-SQLAlchemy, but can be updated):

   ```bash
   pip install SQLAlchemy
   ```

7. Install Requests (For making HTTP requests to the Ngrok API):

   ```bash
   pip install requests
   ```

## Setup Docker

1. Docker Desktop (Core Installation)
    Download and Install Docker Desktop at Docker's Official website
     Verify Docker Installation:
     ```bash
     docker --version
     docker compose version
     ```
2. Docker-Compose Command to Run Your Flask App:
   ```bash
   docker compose up --build
   ```

## Running the App

1. Run main.py
2. Ctrl + click the http://127.0.0.1:5000 displayed in terminal
   set FLASK_ENV=development
   ```
3. Run the application:

   ```bash
   flask run
   ```
