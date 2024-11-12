import datetime
import os
from pathlib import Path

import wagtail

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-z*(=z4%-z0%wr#$npmtzk25sw7i#^%)uq=01gz80x$h7*pvawx"
)

DEBUG = os.environ.get("DEBUG", True)

ALLOWED_HOSTS = ["api.subist.com", "18.156.78.98", "localhost", "172.27.0.6"]

INSTALLED_APPS = [
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "daphne",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "subapp",
    "social",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "subist_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates"),
            os.path.join(
                os.path.dirname(os.path.dirname(wagtail.__file__)),
                "wagtail",
                "templates",
            ),
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

ASGI_APPLICATION = "subist_api.asgi.application"

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL],
        },
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DATABASE_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("DATABASE_USER", None),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", None),
        "HOST": os.environ.get("DATABASE_HOST", None),
        "PORT": os.environ.get("DATABASE_PORT", None),
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


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

if DEBUG == False:
    DEFAULT_FILE_STORAGE = "subist_api.storage_backends.MediaRootS3Boto3Storage"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get(
    "AWS_SECRET_ACCESS_KEY"
)
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "subist")
AWS_DEFAULT_ACL = "public-read"
AWS_QUERYSTRING_AUTH = False

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_LOCATION = "statics"

if DEBUG == True:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATIC_URL = "/static/"
else:
    STATICFILES_STORAGE = "subist_api.storage_backends.StaticRootS3Boto3Storage"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"

if DEBUG == False:
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, "")
else:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 30,
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=100),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(hours=10),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
}

CELERY_BROKER_URL = os.environ.get(
    "CELERY_BROKER_URL", "amqp://guest:guest@rabbitmq:5672//"
)
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "rpc://")

CSRF_TRUSTED_ORIGINS = [
    "http://api.subist.com",
    "https://api.subist.com",
    "http://localhost:3000",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://subist-client.vercel.app",
    "https://subist-client-subists-projects.vercel.app",
    "https://subist-client-git-main-subists-projects.vercel.app",
    "https://subist-client-my1gmnj88-subists-projects.vercel.app",
    "https://www.subist.com",
    "https://subist.com",
]

WAGTAILADMIN_BASE_URL = "subist.com"
WAGTAIL_SITE_NAME = "Subist"
