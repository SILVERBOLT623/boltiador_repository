# 🖤 bolt_project — Django Portfolio Website

> Personal portfolio of **Adrian L. Boltiador**, built with Django.

---

## 📁 Project Structure

```
bolt_project/
├── manage.py
├── requirements.txt
├── db.sqlite3                  ← auto-created after migrations
│
├── bolt_project/               ← Django project config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── bolt_app/                   ← Main Django app
    ├── __init__.py
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── static/bolt_app/
    │   ├── css/
    │   │   └── style.css
    │   └── js/
    │       └── main.js
    └── templates/bolt_app/
        ├── base.html
        ├── home.html
        ├── about.html
        ├── skills.html
        ├── projects.html
        ├── education.html
        └── contact.html
```

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/SILVERBOLT623/boltiador_repository.git
cd bolt_project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an admin superuser

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** — your portfolio is live.
Admin panel: **http://127.0.0.1:8000/admin**

---

## 🌐 Pages

| URL              | Page        | Description                              |
|------------------|-------------|------------------------------------------|
| `/`              | Home        | Hero section, tagline, profile photo     |
| `/about/`        | About       | Personal background and career goals     |
| `/skills/`       | Skills      | Categorised skills with progress bars    |
| `/projects/`     | Projects    | Project cards with tech stack and links  |
| `/education/`    | Education   | Academic background and timeline         |
| `/contact/`      | Contact     | Social links and contact form            |
| `/admin/`        | Admin Panel | Manage all portfolio content             |

---

## 🛠 Customising Your Content

All content is managed through the Django admin panel at `/admin`.

| Model              | What to fill in                                              |
|--------------------|--------------------------------------------------------------|
| **Profile**        | Name, tagline, bio, career goals, photo, social links, CV   |
| **Skill**          | Name, category (frontend/backend/etc.), proficiency (0–100) |
| **Project**        | Title, description, tech stack, GitHub URL, live URL, image |
| **Education**      | Institution, degree, field of study, years, description      |
| **ContactMessage** | Read-only — messages submitted via the contact form         |


## 🚀 Production Checklist

Before deploying to a live server:

- [ ] Set `DEBUG = False` in `settings.py`
- [ ] Set a strong, unique `SECRET_KEY` (use environment variables or `.env`)
- [ ] Add your domain to `ALLOWED_HOSTS`
- [ ] Run `python manage.py collectstatic`
- [ ] Configure a production email backend (SMTP / SendGrid / Mailgun)
- [ ] Serve media files via a CDN or cloud storage (e.g. AWS S3 with `django-storages`)
- [ ] Use a production WSGI server such as **Gunicorn** behind **Nginx**

**Example Gunicorn command:**
```bash
gunicorn bolt_project.wsgi:application --bind 0.0.0.0:8000
```

---

## 🧰 Tech Stack

| Layer      | Technology                                    |
|------------|-----------------------------------------------|
| Backend    | Django 4.x, Python 3.10+                     |
| Database   | SQLite (development) / PostgreSQL (production)|
| Frontend   | Vanilla HTML · CSS Custom Properties · JS     |
| Fonts      | Syne (display) + DM Mono (accents)            |
| Theme      | Dark minimalist — `#0a0a0f` bg · `#6c63ff` accent |
| Media      | Pillow (image handling)                       |

---

## 📦 Dependencies

```
asgiref==3.11.1
Django==5.2.12
dotenv==0.9.9
pillow==12.1.1
python-dotenv==1.2.2
sqlparse==0.5.5
tzdata==2025.3
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 👤 Author

**Adrian L. Boltiador**
- GitHub: [@adrianboltiador](https://github.com/boltiador_repository)
- Email: adrianboltiador12345@example.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).