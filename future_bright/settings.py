from pathlib import Path
from environ import Env
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment
env = Env()
env.read_env(BASE_DIR / '.env')  # Reads variables from .env file

# Get environment (development or production)
ENVIRONMENT = env('ENVIRONMENT', default='production')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENVIRONMENT == 'development'

ALLOWED_HOSTS = ['*']  # Adjust this in production

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Custom apps
    'pages',
    'blog',
    'courses',
    'contact',
    'accounts',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # For serving static files in production
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'accounts.middleware.AdminAccessMiddleware', 
]

ROOT_URLCONF = "future_bright.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "future_bright.wsgi.application"

# Database configuration

# Database configuration (use Render PostgreSQL always)
DATABASE_URL = env('DATABASE_URL')  # Set this in both local and Render environments
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Use Cloudinary for media files
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Cloudinary credentials (you can also load from environment variables)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME')  ,
    'API_KEY': env('API_KEY')  ,
    'API_SECRET': env('API_SECRET')  ,
}

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# Authentication
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

print("Cloud name from env:", env('CLOUD_NAME'))

