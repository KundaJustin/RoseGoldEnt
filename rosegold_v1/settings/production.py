from .base import *

DEBUG = True
SECRET_KEY = "django-insecure-pm^-sh-=6#kz(_ux(c*%bbri8hto_ihp5=ecp!8bf54+9x46yo"
ALLOWED_HOSTS = [".vercel.app", "localhost"]


DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = "your-cloudflare-access-key-id"
AWS_SECRET_ACCESS_KEY = "your-cloudflare-secret-access-key"
AWS_STORAGE_BUCKET_NAME = "your-r2-namespace"
AWS_S3_ENDPOINT_URL = "<https://storage.developers.cloudflare.com>"
