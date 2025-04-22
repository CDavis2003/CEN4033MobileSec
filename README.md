# CEN4033MobileSec

This project is a Django-based backend for a mobile security awareness website game, focusing on educating users about mobile security through interactive game elements and various security challenges in a quiz format.

## Features
- User authentication
- Game logic and progress tracking
- Security-related questions and challenges
- Integration with a web UI for a seamless experience

## Technologies Used
- Python
- Django
- HTML/CSS
- SQLite (for local database)

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/CDavis2003/CEN4033MobileSec.git
    ```

2. Navigate to the project directory:
    ```bash
    cd CEN4033MobileSec
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000/` to start using the app.
