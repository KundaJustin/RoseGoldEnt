from .base import *

DEBUG = False
SECRET_KEY = "django-insecure-pm^-sh-=6#kz(_ux(c*%bbri8hto_ihp5=ecp!8bf54+9x46yo"
ALLOWED_HOSTS = [".vercel.app", "localhost", ".rosegold-ent.com"]


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