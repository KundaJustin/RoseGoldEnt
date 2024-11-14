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