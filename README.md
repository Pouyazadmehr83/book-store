# 📚 Book Store - Django Powered E-Commerce Platform

A modern, production-ready online bookstore built with **Django 6.0.5**, featuring user authentication, book inventory management, and a beautiful responsive frontend.

---

## 🚀 Features

### 💻 Backend
- **Django 6.0.5** - Latest stable Django framework
- **PostgreSQL 15** - Robust relational database
- **Custom User Authentication** - Powered by django-allauth
- **Admin Dashboard** - Comprehensive Django admin interface
- **Debug Toolbar** - Development debugging and performance monitoring

### 🎨 Frontend
- **Bootstrap 5** - Modern responsive UI framework
- **Crispy Forms** - Elegant form rendering with django-crispy-forms
- **HTML5 & CSS3** - Clean semantic markup
- **JavaScript** - Interactive user experience

### 🔐 Security & Performance
- **Environment Variable Management** - Secure configuration with environs
- **Cache Middleware** - Built-in caching for optimal performance
- **CSRF Protection** - Django's built-in security features
- **Email Support** - Console backend for development, SMTP ready for production

### 📦 Deployment Ready
- **Docker & Docker Compose** - Containerized application setup
- **Development Server** - Pre-configured with hot-reload
- **Environment Configuration** - Easy switching between dev and production

---

## 🛠 Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Framework** | Django | 6.0.5 |
| **Database** | PostgreSQL | 15 |
| **Frontend** | Bootstrap 5 + HTML/CSS/JS | Latest |
| **Authentication** | django-allauth | 65.17.0 |
| **Forms** | django-crispy-forms | 2.6 |
| **ORM** | Django ORM | 6.0.5 |
| **Container** | Docker | Latest |

---

## 📋 Project Structure

```
book-store/
├── config/                 # Django project configuration
│   ├── settings.py        # Main settings file
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── accounts/              # User management app
│   ├── models.py          # Custom user model
│   └── views.py           # Authentication views
├── books/                 # Books catalog app
│   ├── models.py          # Book model
│   ├── views.py           # Book views
│   └── admin.py           # Django admin configuration
├── pages/                 # Static pages app
│   ├── views.py           # Page views (home, about, etc.)
│   └── urls.py            # Page URLs
├── templates/             # HTML templates
├── static/                # CSS, JavaScript, images
├── media/                 # User-uploaded content
├── docker-compose.yml     # Docker services configuration
├── Dockerfile             # Docker image definition
├── requirements.txt       # Python dependencies
└── manage.py              # Django CLI tool
```

---

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose (recommended)
- Python 3.12+ (for local development)
- PostgreSQL 15+ (if running locally)

### Option 1: Using Docker (Recommended) 🐳

**Step 1: Clone the repository**
```bash
git clone https://github.com/Pouyazadmehr83/book-store.git
cd book-store
```

**Step 2: Create environment file**
```bash
cp .env.example .env
```

Create a `.env` file with the following variables:
```env
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://postgres:password@db:5432/book_store_db
```

**Step 3: Build and start containers**
```bash
docker-compose up -d
```

The application will be available at: **http://localhost:8000**

**Step 4: Run migrations**
```bash
docker-compose exec web python manage.py migrate
```

**Step 5: Create superuser**
```bash
docker-compose exec web python manage.py createsuperuser
```

**Step 6: Access the admin panel**
Navigate to: **http://localhost:8000/admin**

---

### Option 2: Local Development Setup 💻

**Step 1: Clone the repository**
```bash
git clone https://github.com/Pouyazadmehr83/book-store.git
cd book-store
```

**Step 2: Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Step 3: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Create environment file**
```bash
touch .env
```

Add your configuration:
```env
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DATABASE_URL=postgres://postgres:password@localhost:5432/book_store_db
```

**Step 5: Run migrations**
```bash
python manage.py migrate
```

**Step 6: Create superuser**
```bash
python manage.py createsuperuser
```

**Step 7: Collect static files**
```bash
python manage.py collectstatic --noinput
```

**Step 8: Start development server**
```bash
python manage.py runserver
```

Access the application at: **http://localhost:8000**

---

## 📚 Key Dependencies

### Backend
- **Django** - Web framework
- **psycopg2-binary** - PostgreSQL adapter
- **django-allauth** - User authentication system
- **django-crispy-forms** - Form rendering
- **pillow** - Image processing
- **python-dotenv** - Environment variable management

### Development
- **django-debug-toolbar** - Debugging and profiling
- **dj-database-url** - Database URL parsing
- **environs** - Environment variable validation

---

## 🔧 Management Commands

### Database
```bash
# Apply migrations
python manage.py migrate

# Create migration for changes
python manage.py makemigrations

# Revert migrations
python manage.py migrate app_name 0001
```

### Development
```bash
# Start development server
python manage.py runserver

# Create superuser account
python manage.py createsuperuser

# Collect static files for production
python manage.py collectstatic
```

### Shell
```bash
# Interactive Django shell
python manage.py shell
```

---

## 🐳 Docker Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f web

# Execute command in container
docker-compose exec web python manage.py migrate

# Rebuild containers
docker-compose up --build
```

---

## 📝 Environment Variables

### Required
- `DJANGO_SECRET_KEY` - Secret key for security
- `DATABASE_URL` - Database connection string

### Optional (with defaults)
- `DJANGO_DEBUG` - Debug mode (default: False)
- `DJANGO_ALLOWED_HOSTS` - Allowed hostnames
- `DJANGO_SECURE_SSL_REDIRECT` - Force HTTPS (default: True)
- `EMAIL_HOST_USER` - SMTP email address
- `EMAIL_HOST_PASSWORD` - SMTP password

---

## 🔐 Security Features

✅ **CSRF Protection** - Built-in Django security  
✅ **Password Validation** - Strong password enforcement  
✅ **Session Security** - Secure session handling  
✅ **Environment Variables** - Sensitive data protection  
✅ **SQL Injection Prevention** - ORM protection  
✅ **XFrame Options** - Clickjacking protection  

---

## 📊 Database Schema

The application includes the following main models:

- **CustomUser** - Extended user model with custom fields
- **Book** - Book inventory with details, pricing, and inventory
- **Category** - Book categories and subcategories
- **Order** - User book purchases and order tracking
- **Review** - User book reviews and ratings

---

## 🎯 Admin Panel Features

The Django admin provides:
- 📖 Book management (add, edit, delete, search)
- 👥 User account management
- 📋 Order tracking and management
- ⭐ Review moderation
- 🔍 Advanced search and filtering
- 📊 Admin dashboard with statistics

---

## 📱 Responsive Design

- ✅ Mobile-first approach
- ✅ Bootstrap 5 breakpoints
- ✅ Touch-friendly interface
- ✅ Fast loading times
- ✅ SEO optimized

---

## 🚀 Production Deployment

### Prepare for Production

1. **Update environment variables:**
```env
DJANGO_DEBUG=False
DJANGO_SECURE_SSL_REDIRECT=True
DJANGO_SESSION_COOKIE_SECURE=True
DJANGO_CSRF_COOKIE_SECURE=True
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

2. **Collect static files:**
```bash
python manage.py collectstatic --noinput
```

3. **Run migrations:**
```bash
python manage.py migrate
```

### Deployment Options

- **Heroku** - Cloud platform with easy setup
- **AWS** - Scalable cloud infrastructure
- **DigitalOcean** - Affordable VPS hosting
- **PythonAnywhere** - Python-specific hosting

---

## 📞 Support & Troubleshooting

### Common Issues

**Port 8000 already in use:**
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>
```

**Database connection error:**
- Verify PostgreSQL is running
- Check `DATABASE_URL` in `.env`
- Ensure database exists and user has permissions

**Static files not loading:**
```bash
python manage.py collectstatic --clear --noinput
```

**Module not found errors:**
```bash
pip install --upgrade -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**Pouya Zadmehr**  
GitHub: [@Pouyazadmehr83](https://github.com/Pouyazadmehr83)

---

## 📞 Contact & Support

For questions, bug reports, or feature requests, please open an issue on GitHub.

---

## 🙏 Acknowledgments

- Django community
- Bootstrap team
- Font Awesome for icons
- All contributors and supporters

---

<div align="center">

**Made with ❤️ by Pouya Zadmehr**

[![GitHub](https://img.shields.io/badge/GitHub-Pouyazadmehr83-blue?style=flat-square&logo=github)](https://github.com/Pouyazadmehr83)

</div>
