Event Management API
This project is a Django-based REST API for managing events such as conferences, meetups, and workshops. Users can create, view, update, and delete events. The API also includes user authentication, event registration, and features like search and email notifications.

Features
Event Management: Create, view, update, and delete events.
User Authentication: Register and authenticate users.
Event Registration: Users can register for events.
Event Search: Search or filter events based on different parameters (e.g., date, location).
Email Notifications: Send email notifications to users upon event registration.
API Documentation: Auto-generated API documentation using Swagger.
Tech Stack
Backend: Python 3.12, Django 4.x, Django REST Framework
Database: SQLite (can be switched to PostgreSQL, MySQL, etc.)
API Documentation: Swagger (drf-yasg)
Authentication: Token-based authentication (Simple JWT)
Containerization: Docker
Installation and Setup
Follow these steps to get the project up and running on your local machine.

1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/event-manager-api.git
cd event-manager-api
2. Install dependencies
This project uses Poetry for dependency management. Install Poetry if you don't have it installed:

bash
Copy code
curl -sSL https://install.python-poetry.org | python3 -
Then, install the dependencies:

bash
Copy code
poetry install
3. Apply Migrations
Before running the server, apply the migrations to set up the database:

bash
Copy code
poetry run python manage.py migrate
4. Create a Superuser
Create a superuser to access the Django admin panel:

bash
Copy code
poetry run python manage.py createsuperuser
5. Run the Server
Start the Django development server:

bash
Copy code
poetry run python manage.py runserver
The server will be running at http://127.0.0.1:8000/.

API Endpoints
Here is a summary of the key endpoints in the API:

Authentication
POST /api/register/ - Register a new user.
POST /api/token/ - Get JWT token (login).
Events
GET /api/events/ - List all events.
POST /api/events/ - Create a new event.
GET /api/events/{id}/ - Retrieve a specific event.
PATCH /api/events/{id}/ - Update an event.
DELETE /api/events/{id}/ - Delete an event.
Event Registration
POST /api/events/{id}/register/ - Register for an event.
GET /api/events/{id}/check-registration/ - Check if the user is registered for an event.
API Documentation
Visit /swagger/ to view the auto-generated API documentation.
Docker Setup
To run the project using Docker:

Build the Docker image:

bash
Copy code
docker-compose build
Start the containers:

bash
Copy code
docker-compose up
The API will be accessible at http://127.0.0.1:8000/.

Event Search and Filtering (Bonus Feature)
You can search or filter events by various parameters like:

Location: /api/events/?location={city}
Date: /api/events/?date={YYYY-MM-DD}
Email Notifications (Bonus Feature)
When a user registers for an event, an email notification will be sent to them. Make sure to configure your email backend in settings.py:

python
Copy code
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
Running Tests
To run the test suite:

bash
Copy code
poetry run python manage.py test
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributions
Feel free to submit pull requests and open issues if you'd like to contribute to the project. Your contributions are welcome!

Contact
For any questions or issues, please contact:

Name: Zabutnyi Yurii
Email: zabutniy10@gmail.com