from .base import *
from .base import env

DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-9t%_eb7utjc&rto!%29crd7l7i%c(i-6&u1gukg@*fu%p$dlxw",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]