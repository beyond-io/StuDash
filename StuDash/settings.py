import os
import warnings
from django.utils.translation import ugettext_lazy as _
from pathlib import Path


warnings.simplefilter("error", DeprecationWarning)

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = os.path.join(BASE_DIR, "content")

SECRET_KEY = "NhfTvayqggTBPswCXXhWaN69HuglgZIkM"

DEBUG = True
ALLOWED_HOSTS = []

SITE_ID = 1

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Vendor apps
    "bootstrap4",
    # Application apps
    "main",
    "accounts",
    "forumMessages",
    "grades.apps.GradesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "StuDash.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(CONTENT_DIR, "templates"),
        ],
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

WSGI_APPLICATION = "StuDash.wsgi.application"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = ""
EMAIL_HOST_USER = "apikey"
DEFAULT_FROM_EMAIL = "orteach123@gmail.com"
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

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

DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = True
LOGIN_VIA_EMAIL_OR_USERNAME = False
LOGIN_REDIRECT_URL = "home"
# LOGIN_URL = "accounts:log_in"
USE_REMEMBER_ME = True

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = False

SIGN_UP_FIELDS = [
    "username",
    "first_name",
    "last_name",
    "email",
    "password1",
    "password2",
]
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ["first_name", "last_name", "email", "password1", "password2"]

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = "en"
LANGUAGES = [
    ("en", _("English")),
]

TIME_ZONE = "UTC"
USE_TZ = True

STATIC_ROOT = os.path.join(CONTENT_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(CONTENT_DIR, "media")
MEDIA_URL = "/media/"

STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, "assets"),
]

LOCALE_PATHS = [os.path.join(CONTENT_DIR, "locale")]
