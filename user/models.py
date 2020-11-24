import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _

from pari.models import *


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True
    )

    email = models.EmailField(_('email address'), unique=True)
    # paris = models.ManyToManyField( Pari, blank = True,)
    autre_paris = models.ManyToManyField( AutrePari, blank = True,)
    matchs = models.ManyToManyField( Match, blank = True,)
    combats = models.ManyToManyField( Combat, blank = True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
