# Blog Posting Platform ✅

A simple, responsive Django-based blogging platform that supports user accounts, post creation/editing, comments, categories, search, and a small weather lookup feature. This repository is configured for local development using SQLite and Django 5.

---

## 🔎 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Quickstart — Clone, Setup & Run (Windows)](#-quickstart--clone-setup--run-windows)
- [Environment Variables](#-environment-variables)
- [Development Notes](#-development-notes)
- [Running Tests](#-running-tests)
- [Security & Production Tips](#-security--production-tips)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✅ Features

- User registration, login, profile editing (with avatar upload)
- Create, edit, delete blog posts
- Post categories (Sport, Politics, Economics, Weather, Health, Education)
- Post comments and a comment count view
- Search posts and view by category
- Password reset via email (configure SMTP credentials)
- Simple weather lookup using OpenWeatherMap API (code in `myblog/weather.py`)

---

## 🔧 Tech Stack

- Python (3.11+ recommended)
- Django 5.0.6
- SQLite (default; file: `db.sqlite3`)
- django-crispy-forms + Bootstrap 5 for forms
- Requests for external API calls

These dependencies are listed in `requirements.txt`.

---

## 🚀 Quickstart — Clone, Setup & Run (Windows)

1. Clone the repo:

```bash
git clone https://github.com/chandansubedi/blog-posting-platform.git
cd blog-posting-platform
```

2. Create a virtual environment and activate it (Windows PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1   # or venv\Scripts\activate for cmd
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file (or set environment variables) — see [Environment Variables](#-environment-variables) below.

5. Apply database migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

6. (Optional) Collect static files for production:

```bash
python manage.py collectstatic
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Open your browser at: `http://127.0.0.1:8000/`

---

## 🔐 Environment Variables

For local dev, create a `.env` file in the project root or export these variables in your environment. Example `.env` (DO NOT commit this file):

```env
# Django
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email (for password reset functionality)
EMAIL_HOST_PASSWORD=your-email-app-password

# OpenWeather API (recommended) — replace the hardcoded API key in myblog/weather.py with this env var
OPENWEATHER_API_KEY=your_openweather_api_key
```

Tip: update `myblog/weather.py` to read the API key from the environment instead of a hard-coded string:

```python
import os
api_key = os.environ.get('OPENWEATHER_API_KEY')
```

---

## 🛠 Development Notes

- Database: SQLite by default (`db.sqlite3`) — easy for local development.
- Static files: `STATIC_ROOT` is set to `asset/`. In dev, Django serves static files automatically.
- Media files (user avatars, uploads): stored under `media/`. Ensure `MEDIA_URL`/`MEDIA_ROOT` are configured when deploying.
- Time zone: default set to `Asia/Kathmandu` in `blogApp/settings.py`.
- Email: To enable password reset emails, set up an SMTP account and provide `EMAIL_HOST_PASSWORD` in environment variables.

---

## ✅ Running Tests

If tests are implemented in the app files, run:

```bash
python manage.py test
```

---

## ⚠️ Security & Production Tips

- **Never** commit `SECRET_KEY`, API keys, or credentials. Use environment variables or a secrets manager.
- Set `DEBUG = False` in production and add your domain(s) to `ALLOWED_HOSTS`.
- Use a stronger production database (Postgres, MySQL) for deployed apps.
- Configure HTTPS and proper email backend credentials.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request. If you plan to add features, describe them first so we can align changes and tests.

---

## 📄 License

This project does not contain a license file. Add a LICENSE if you want to make it open-source with a specific license.

---

If you want, I can also:

- Add a sample `.env.example` file
- Replace the hard-coded OpenWeather API key with environment lookup code in `myblog/weather.py`
- Create basic unit tests or CI workflow

💡 **Next steps:** update `myblog/weather.py` to use `OPENWEATHER_API_KEY` from env and remove the hard-coded key to keep credentials secure.
