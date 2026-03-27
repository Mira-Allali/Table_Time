# Table Time

Table Time is a lightweight full-stack task management web application designed to organize and monitor tasks with deadlines through multiple visualizations: Table, Calendar, and Agenda views.

The project follows a layered architecture using FastAPI for the backend, SQLAlchemy ORM, and a SQLite database, combined with a minimal frontend built with HTML, CSS, and vanilla JavaScript.

---

## Project Objective

The goal of this application is to provide a simple yet structured solution for:

Task organization
Deadline tracking
Status monitoring (pending / completed)

It demonstrates the implementation of a complete CRUD system, API design, and code quality enhancement using testing and linting tools.

---
## Features

- Create, update, and delete tasks
- Deadline management with datetime support
- Multiple visualization modes:
    Table view (structured overview)
    Calendar view (date-based visualization)
    Agenda view (chronological listing)
- Real-time synchronization between UI and backend API
- Task status tracking (pending / done)
- Unit testing with pytest
- Code quality enforcement using flake8
- Pagination support for scalable task retrieval

---

## Tech Stack

- Backend
    FastAPI → high-performance web framework
    SQLAlchemy → ORM for database abstraction
    Pydantic → data validation and serialization
- Frontend
    HTML / CSS / JavaScript (Vanilla)
    Jinja2 Templates
- Database
    SQLite (local, lightweight)
- Code Quality & Testing
    pytest → unit testing
    flake8 → linting and PEP8 compliance
---

## Screenshots

### Table View
![Table View](screenshots/table_view.png)

### Calendar View
![Calendar View](screenshots/calendar_view.png)

### Agenda View
![Agenda View](screenshots/agenda_view.png)

---

## Installation

### Prerequisites
- Python 3.6+
- Git

### Steps

1. Clone the repository:

```bash
git clone https://github.com/Mira-Allali/Table_Time.git
cd table_time/backend
```
2. Create and activate a virtual environment:
```bash
python -m venv env
env\Scripts\activate   # Windows
# or
source env/bin/activate  # macOS/Linux
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Start the server:
```bash
uvicorn main:app --reload
```
5. Open the app in your browser:
```bash
http://127.0.0.1:8000/ui

```
6. Testing (pytest)

Run unit tests to validate CRUD operations.

A dedicated in-memory SQLite database is used to ensure test isolation.

7. Code Quality (flake8)

Run linting to ensure code quality and adherence to PEP8 standards: flake8 .

This helps:

Detect syntax errors
Improve readability
Maintain consistent coding style

---
## Usage

- Click + New Task to add a task

- Navigate between Table, Calendar, and Agenda using the top buttons

- Edit or delete tasks using the buttons in each task row

- All operations are synchronized with the backend API
---

## Optional: One-Click Launch (Windows)

- You can create a .exe to launch the app and open the UI automatically:
```bash
python launcher.py
```
(Use PyInstaller with --onefile --noconsole to create an executable.)

---
## Workflow for the Demo 

- Run the launcher or uvicorn backend.main:app --reload.

- Open the UI at /ui.

- Demonstrate adding, editing, and deleting tasks.

- Switch between Table, Calendar, and Agenda views.

- Show that all changes persist in the SQLite database.

---

## Limitations
- No user authentication (public API)
- SQLite not suitable for large-scale production
- No real-time updates (no WebSocket)
- Basic frontend (no framework like React/Vue)

---

## Future Improvements
- Add authentication (JWT)
- Migrate to PostgreSQL
- Add notifications/reminders
- Deploy to cloud (Docker + CI/CD)
- Advanced filtering and analytics

---

## Contributing

- Fork the repository
- Create a new branch for your feature/fix
- Submit a pull request

---

## Authors

Mira Allali | PhD Researcher – Networks and Security  
Berrached Assia | PhD Researcher – Architecture  
Cherki Asma Nada | PhD Researcher – English Literature and Civilisation  
Mechache Hadil Hadjer | PhD Researcher – English Language and Culture  
Mouharar Ahlam | PhD Researcher – English Language and Culture  

```

---

## License

This repository is intended for academic and research purposes.
