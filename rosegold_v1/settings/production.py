from .base import *

DEBUG = False
SECRET_KEY = "django-insecure-pm^-sh-=6#kz(_ux(c*%bbri8hto_ihp5=ecp!8bf54+9x46yo"
ALLOWED_HOSTS = [".vercel.app", "localhost", ".rosegold-ent.com"]


if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
else:
    SECURE_HSTS_SECONDS = 0
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

CACHE_TTL = 60 * 15

DEFAULT_FILE_STORAGE = "rosegold_v1.storage_backends.MediaRootS3Boto3Storage"

STATICFILES_STORAGE = "rosegold_v1.storage_backends.StaticRootS3Boto3Storage"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get(
    "AWS_SECRET_ACCESS_KEY"
)
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "subist")
AWS_DEFAULT_ACL = "public-read"
AWS_QUERYSTRING_AUTH = False

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400z"}
AWS_LOCATION = "statics_v2"

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, "")