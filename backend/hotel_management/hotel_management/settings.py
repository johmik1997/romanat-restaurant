from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv
import cloudinary

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = ["*"]

# ------------------------------------
# INSTALLED APPS
# ------------------------------------
INSTALLED_APPS = [
    "axes",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework_simplejwt",

    "rest_framework",
    "django_filters",
    "corsheaders",

    "cloudinary",
    "cloudinary_storage",

    "accounts",
    "rooms",
    "reservations",
    "payments",
]

# ------------------------------------
# MIDDLEWARE  (IMPORTANT ORDER!)
# ------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    "corsheaders.middleware.CorsMiddleware",  # must be near top

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    "axes.middleware.AxesMiddleware",
]

# ------------------------------------
# TEMPLATES (FULLY FIXED)
# ------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Required for admin to work
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
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

ROOT_URLCONF = "hotel_management.urls"
WSGI_APPLICATION = "hotel_management.wsgi.application"

# ------------------------------------
# AUTH BACKENDS (FIXED ORDER)
# ------------------------------------
AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
]


# ------------------------------------
# DATABASE
# ------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# ------------------------------------
# CUSTOM USER
# ------------------------------------
AUTH_USER_MODEL = "accounts.User"

# ------------------------------------
# SIMPLE JWT
# ------------------------------------
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=12),
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": SECRET_KEY,
}

# ------------------------------------
# CORS
# ------------------------------------
CORS_ALLOW_ALL_ORIGINS = True

# ------------------------------------
# AXES CONFIG
# ------------------------------------
AXES_FAILURE_LIMIT = 5
AXES_ONLY_USER_FAILURE = True
AXES_RESET_ON_SUCCESS = True

# ------------------------------------
# CHAPA KEYS
# ------------------------------------
CHAPA_SECRET_KEY = os.getenv("CHAPA_SECRET_KEY")
CHAPA_TRANSACTION_URL = "https://api.chapa.co/v1/transaction/initialize"
CHAPA_VERIFY_URL = "https://api.chapa.co/v1/transaction/verify"
CHAPA_WEBHOOK_SECRET = os.getenv("CHAPA_WEBHOOK_SECRET")

# ------------------------------------
# CLOUDINARY
# ------------------------------------
CLOUDINARY = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}

cloudinary.config(
    cloud_name=CLOUDINARY["CLOUD_NAME"],
    api_key=CLOUDINARY["API_KEY"],
    api_secret=CLOUDINARY["API_SECRET"]
)

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# ------------------------------------
# STATIC FILES
# ------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

# ------------------------------------
# TIME + LANG
# ------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
