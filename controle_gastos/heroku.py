import environ

from controle_gastos.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRETY_KEY = env('SECRETY_KEY')

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default":env.db(),
}
