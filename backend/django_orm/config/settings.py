import os
from pathlib import Path

import dj_database_url

def normalize_pg_url_for_django(url: str) -> str:
    if not url:
        return url

    replacements = {
        "postgresql+psycopg://": "postgresql://",
        "postgresql+psycopg2://": "postgresql://",
        "postgres+psycopg://": "postgres://",
        "postgres+psycopg2://": "postgres://",
    }

    for src, dst in replacements.items():
        if url.startswith(src):
            return url.replace(src, dst, 1)

    return url


RAW_DATABASE_URL = os.getenv("DATABASE_URL")
if RAW_DATABASE_URL:
    os.environ["DATABASE_URL"] = normalize_pg_url_for_django(RAW_DATABASE_URL)


# =============================================================================
# Core Paths & Environment
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-dev-only-do-not-use-in-prod",
)

DEBUG = True  # Dev only (laptop / ngrok)


# =============================================================================
# Hosts & Trust Boundaries
# -----------------------------------------------------------------------------
# Explicitly allow ngrok for public contract testing.
# In production this should be locked down tightly.
# =============================================================================

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "django",
    ".ngrok-free.dev",  # dev-only public tunnel
    "16.176.161.31",   # EC2 public IP
]

# =============================================================================
# Installed Applications
# =============================================================================

INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Cross-cutting infrastructure
    "corsheaders",
    "djmoney",
    "simple_history",

    # 2SMAiRT apps
    "core",
    "project",
    # "lookup",
    "utils",
    "or",
]

# =============================================================================
# Middleware Stack
# -----------------------------------------------------------------------------
# Ordering matters. CORS must be first. WhiteNoise early.
# =============================================================================

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",

    "simple_history.middleware.HistoryRequestMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =============================================================================
# URL Configuration
# =============================================================================

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"


# =============================================================================
# Templates
# =============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =============================================================================
# Databases
# -----------------------------------------------------------------------------
# Primary DB is schema-based (project-per-schema).
# Secondary DB used by Mayan EDMS.
# =============================================================================
#
# DATABASES = {
#     "default": dj_database_url.config(
#         default="postgres://smairt_user:smairt_pass@postgres:5432/prj00002_db_dev",
#         conn_max_age=600,
#     ),
#     "mayan": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("MAYAN_DATABASE_NAME"),
#         "USER": os.getenv("MAYAN_DATABASE_USER"),
#         "PASSWORD": os.getenv("MAYAN_DATABASE_PASSWORD"),
#         "HOST": os.getenv("MAYAN_DATABASE_HOST"),
#         "PORT": os.getenv("MAYAN_DATABASE_PORT", 5432),
#         "OPTIONS": {"options": "-c search_path=public"},
#     },
# }
#
# # Project schema first, then public fallback
# DATABASES["default"]["OPTIONS"] = {
#     "options": "-c search_path=prj00002,public"
# }


DATABASES = {
    "default": dj_database_url.config(
        default="postgres://smairt_user:smairt_pass@localhost:5432/smairt_lite",
        conn_max_age=600,
    )
}

# =============================================================================
# Auth & Internationalisation
# =============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# =============================================================================
# Static Files
# =============================================================================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# =============================================================================
# Async / Background
# =============================================================================

# CELERY_BROKER_URL = "redis://redis:6379/2"

CELERY_BROKER_URL = os.getenv(
    "CELERY_BROKER_URL",
    "redis://localhost:6379/2",
)


# =============================================================================
# Defaults & Formatting
# =============================================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_THOUSAND_SEPARATOR = True
NUMBER_GROUPING = 3


# =============================================================================
# CORS – Contract Exposure (DEV ONLY)
# -----------------------------------------------------------------------------
# This allows Emergent / external frontends to call Django-hosted contracts.
# Lock this down in prod.
# =============================================================================

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Example prod hardening:
# CORS_ALLOWED_ORIGINS = [
#     "https://app.yourdomain.com",
# ]
