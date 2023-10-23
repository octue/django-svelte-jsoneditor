import os


def get_db_conf():
    """
    Configures database according to the DATABASE_ENGINE environment
    variable. Defaults to SQlite.
    This method is used to let tests run against different database backends.
    """
    database_engine = os.environ.get("DATABASE_ENGINE", "sqlite")
    if database_engine == "sqlite":
        return {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
    elif database_engine == "postgres":
        return {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "postgres_db",
            "USER": "postgres_user",
            "PASSWORD": "postgres_password",
            "HOST": "localhost",
            "PORT": "5432",
        }


# ---------------------------------------------------------------------------
# GENERIC DJANGO SETTINGS FOR THE TEST APP (scroll down for the good stuff)
# ---------------------------------------------------------------------------

DEBUG = True

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",  # Gives us shell_plus and reset_db for manipulating the test server
    "debug_toolbar",  # Allows us to inspect SQL statements made when making queries in the admin
    "django_svelte_jsoneditor",
    "tests.server.example",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Required for django_debug_toolbar
if DEBUG:
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "django_svelte_jsoneditor", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
            ],
            "debug": DEBUG,
        },
    },
]

ALLOWED_HOSTS = [
    "localhost",
    ".loca.lt",
]  # Adding loca.lt allows developers to expose the example server using localtunnel

DATABASES = {"default": get_db_conf()}

ROOT_URLCONF = "tests.server.urls"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

SECRET_KEY = "secretkey"

ASGI_APPLICATION = "tests.server.asgi.application"

# STATIC FILES (FOR LOCAL DEVELOPMENT OF WIDGETS)
STATIC_URL = "static/"
STATIC_ROOT = "./staticfiles"
