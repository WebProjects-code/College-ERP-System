import os
from pathlib import Path
import environ
from datetime import timedelta

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env("DJANGO_SECRET_KEY", default="unsafe-secret")
DEBUG = env("DEBUG", default=True)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third party
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "django_filters",
    "corsheaders",

    # Local
    "accounts",
    "academics",
    "assessment",
    "attendance",
    "finance",
    "notifications",
    "erpapp"
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "collegeERPsystem.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
        ]},
    }
]

WSGI_APPLICATION = "collegeERPsystem.wsgi.application"
ASGI_APPLICATION = "collegeERPsystem.asgi.application"

# Database
DATABASES = {"default": env.db("DATABASE_URL", default="sqlite:///db.sqlite3")}

# Auth
AUTH_USER_MODEL = "accounts.User"

# Static & media
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# DRF + Simple JWT
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "PAGE_SIZE": 20,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(env("JWT_ACCESS_LIFETIME", default=15))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(env("JWT_REFRESH_LIFETIME", default=7))),
}

# Celery / Redis
CELERY_BROKER_URL = env("REDIS_URL", default="redis://localhost:6379/0")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

# CORS
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=["http://localhost:5173"])

# drf-spectacular
SPECTACULAR_SETTINGS = {"TITLE": "College ERP API", "VERSION": "1.0.0"}

# Email (example)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
