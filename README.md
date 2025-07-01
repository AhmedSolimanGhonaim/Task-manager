# Tasker API

A simple task management API with a modern React frontend.

---

## Installation

```bash
pip install -r requirements.txt
```

## Run the application

```bash
python tasker/app/main.py
```

## Access API documentation

[http://localhost:8000/docs](http://localhost:8000/docs)

## Example API calls

```bash
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Sample Task", "priority": "high"}'
```

---

## Frontend (React)

The `frontend/` directory contains a modern React app to interact with the Tasker API.

### Setup & Run

```bash
cd frontend
npm install
npm start
```

The frontend will run on [http://localhost:3000](http://localhost:3000) by default.

---

## Project Structure

- `tasker/` - Python backend (FastAPI)
- `frontend/` - React frontend
- `README.md` - This file

---

## Docker Usage

You can run the entire stack (backend + frontend) using Docker Compose:

### Build and Start
```bash
docker-compose up --build
```

- Backend (FastAPI): [http://localhost:8000](http://localhost:8000)
- Frontend (React): [http://localhost:3000](http://localhost:3000)

### Stopping
Press `Ctrl+C` in the terminal, then run:
```bash
docker-compose down
```

### Troubleshooting
- If you see `address already in use`, make sure nothing else is running on ports 8000 or 3000.
- Free up the port or change the port mapping in `docker-compose.yml`.

---

## API Examples

### Create a Task
```bash
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Sample Task", "priority": "high"}'
```

### List All Tasks
```bash
curl http://localhost:8000/tasks
```

### Get Task by ID
```bash
curl http://localhost:8000/tasks/1
```

### Update a Task
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Title", "priority": "low"}'
```

### Delete a Task
```bash
curl -X DELETE http://localhost:8000/tasks/1
```

### Create Multiple Tasks
```bash
curl -X POST "http://localhost:8000/tasks/group" \
     -H "Content-Type: application/json" \
     -d '[{"title": "Task 1", "priority": "high"}, {"title": "Task 2", "priority": "low"}]'
```

### Filter by Status
```bash
curl http://localhost:8000/tasks/status/pending
```

### Filter by Priority
```bash
curl http://localhost:8000/tasks/priority/high
```

---


```


