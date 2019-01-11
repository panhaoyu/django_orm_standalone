import django as _django
from django.conf import settings as _settings
import db.models

_DATABASE = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'db.sqlite3',
}


def setup(database=None, models=None):
    if database is None:
        database = _DATABASE
    if models is None:
        models = list()
    _settings.configure(
        DATABASES=database,
        INSTALLED_APPS=['django_orm_standalone.db'],
    )
    _django.setup()


def register(model):
    setattr(db.models, model.__name__, model)
