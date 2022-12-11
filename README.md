# [Django Admin Star](https://github.com/app-generator/django-admin-star)

Modern template for **Django Admin Interface** coded on top of **Star Admin**, an open-source `Boostrap 5` design from `BootstrapDash`.

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

<br>

**Links & Resources**

- UI Kit: [Star Admin BS5](https://github.com/BootstrapDash/star-admin2-free-admin-template) by `BootstrapDash`
- [Django Admin Star](#) - `LIVE Demo` (soon)
- [Django Admin Star]() - `playground project` (soon)

<br />

![Star Admin - Full-Stack Starter generated by AppSeed.](https://user-images.githubusercontent.com/51070104/168732392-51748c85-f2c2-45ad-978c-2b64e52292e2.png)

<br />

## Why `Django Admin Star`

- Modern `Bootstrap 5` Design
- `Responsive Interface`
- `Minimal Template` overriding
- `Easy integration`

Star Admin 2 Free is a free admin dashboard template built with Bootstrap 5. We took the original Star Admin Pro and gave it a design overhaul along with newly written code to create our best template yet. This is a modern-looking dashboard with a clean and elegant design. 

<br />

## How to use it

<br />

> **Install the package** via `PIP` 

```bash
$ pip install django-admin-star
// OR
$ pip install git+https://github.com/app-generator/django-admin-star.git
```

<br />

> Add `admin_star` application to the `INSTALLED_APPS` setting of your Django project `settings.py` file (note it should be before `django.contrib.admin`):

```python
    INSTALLED_APPS = (
        ...
        'admin_star.apps.AdminStarConfig',
        'django.contrib.admin',
    )
```

<br />

> Add `LOGIN_REDIRECT_URL` and `EMAIL_BACKEND` of your Django project `settings.py` file:

```python
    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

<br />

> Add `admin_material` urls in your Django Project `urls.py` file

```python
    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_material.urls')),
    ]
```

<br />

> **Collect static** if you are in `production environment`:

```bash
$ python manage.py collectstatic
```

<br />

> **Start the app**

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`

<br />

## Screenshots

@ToDo

<br />

---
[Django Admin Star](https://github.com/app-generator/django-admin-star) - Modern Admin Interface provided by **[AppSeed](https://appseed.us/)**
