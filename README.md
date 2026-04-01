# 3D Visual Art Studio

A full-stack application featuring a FastAPI backend, a React frontend, and a PostgreSQL database.

## Project Structure

- **backend/**: FastAPI application with SQLAlchemy ORM.
- **frontend/**: React application using Three.js and MediaPipe.
- **docker-compose.yml**: Orchestration for the entire stack.

## Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local backend development)
- Node.js 18+ (for local frontend development)

## Setup and Installation

### 1. Environment Configuration

Before running the project, copy the `.env.example` file to create your own `.env` file and customize your settings (e.g., database passwords):

```bash
cp .env.example .env
```

### 2. Running with Docker

To build and start all services (Database, Backend, and Frontend):

```bash
docker-compose up --build -d
```

### Accessing the Services

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **PostgreSQL**: localhost:5433 (via Docker host mapping)

To stop the services:

```bash
docker-compose down
```

## Local Development Setup

### Backend (PyCharm)

1. Open the `backend/` directory in PyCharm.
2. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update your local environment variables (or `.env` file) to point to the local database:
   `DATABASE_URL=postgresql://postgres:your_password@localhost:5433/art_studio_db`
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend (IntelliJ / WebStorm)

1. Open the `frontend/` directory in IntelliJ.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```
## API Documentation

Once the backend is running, you can access the interactive API documentation at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
