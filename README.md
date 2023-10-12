# Weather Info App

This project serves as a quick start for your Django application that leverages various technologies, including Django, Django REST framework (DRF), Celery, Redis, and PostgreSQL. All of these components are preconfigured and ready for use within Docker containers.

## Technologies

- **Django**: A powerful web framework for building web applications.
- **Django REST framework (DRF)**: A versatile library for creating APIs using Django.
- **Celery**: An asynchronous task queue for executing background tasks.
- **Redis**: Utilized as a message broker for Celery.
- **PostgreSQL**: The database system for your Django application.

## How to Launch the Project

1. Ensure Docker and Docker Compose are installed on your system.

2. Clone this repository:

   ```shell
   git clone https://github.com/nick-rebrik/API-weather.git
   ```
   
3. Navigate to the project directory:
   
   ```shell
   cd API-weather
   ```
   
4. Create and fill in the .env file according to the example env.example

5. Start Docker Compose to bring up all the containers:

   ```shell
   docker-compose up -d
   ```

## 📖 **Swagger UI**

Access a clean and interactive representation of our API endpoints with Swagger:

- [🔗 Swagger UI Documentation](http://127.0.0.1/api/doc/) (api/doc)

---
