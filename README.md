# SmartCare

A healthcare management REST API built with Django REST Framework. Handles doctors, patients, appointments, services, and contact requests.

## Project Structure

```
SmartCare/
├── backend/
│   ├── manage.py
│   ├── smart_care/        # Django settings, urls, wsgi
│   ├── appintment/        # Appointment booking
│   ├── contact_us/        # Contact form
│   ├── doctor/            # Doctor profiles, specializations, reviews
│   ├── patient/           # Patient profiles, auth
│   └── service/           # Medical services
├── frontend/              # Frontend (coming soon)
├── .env
└── requirements.txt
```

## Tech Stack

- Python 3.10
- Django 5.x
- Django REST Framework
- drf-yasg (Swagger/ReDoc API docs)
- django-environ (env config)
- django-filter
- SQLite (dev) / PostgreSQL (prod)
- Pillow (image uploads)

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/SmartCare.git
cd SmartCare
```

### 2. Create and activate virtual environment

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r ../requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside `backend/`:

```env
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### 5. Run migrations

```bash
python3 manage.py migrate
```

### 6. Create superuser

```bash
python3 manage.py createsuperuser
```

### 7. Start the server

```bash
python3 manage.py runserver
```

## API Documentation

Once the server is running, visit:

| URL | Description |
|-----|-------------|
| `http://localhost:8000/swagger/` | Swagger UI |
| `http://localhost:8000/redoc/` | ReDoc UI |
| `http://localhost:8000/admin/` | Django Admin |

## API Endpoints

| Prefix | Description |
|--------|-------------|
| `/api/patient/` | Patient registration, login, logout, profile |
| `/api/doctor/` | Doctor list, specializations, designations, available times, reviews |
| `/api/appintment/` | Book and manage appointments |
| `/api/service/` | Medical services |
| `/api/contact_us/` | Contact form submissions |

## Patient Auth Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/api/patient/register/` | Register new patient |
| POST | `/api/patient/login/` | Login |
| POST | `/api/patient/logout/` | Logout |
| GET | `/api/patient/active/<uid>/<token>/` | Email activation |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for development |
| `EMAIL` | Gmail address for sending emails |
| `EMAIL_PASSWORD` | Gmail app password |

## Deployment

- Set `DEBUG=False` in `.env`
- Add your domain to `ALLOWED_HOSTS` in `settings.py`
- Configure PostgreSQL and update `DATABASES` in settings
- Run `python3 manage.py collectstatic`
