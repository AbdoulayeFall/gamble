from django.contrib import admin

from .models import Match, Combat, AutrePari
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'pari'


admin.site.register([Match, Combat, AutrePari])
# Register your models here.
