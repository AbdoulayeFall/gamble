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

    autre_paris = models.ManyToManyField( AutrePari, related_name='u_autre_paris',blank = True,)
    matchs = models.ManyToManyField( Match, related_name='u_matchs', blank = True,)
    combats = models.ManyToManyField( Combat, related_name='u_combats', blank = True,)
    #Invitation
    inAutres = models.ManyToManyField( AutrePari, related_name='u_inAutres', blank = True,)
    inMatchs = models.ManyToManyField( Match, related_name='u_inMatchs', blank = True,)
    inCombats = models.ManyToManyField( Combat, related_name='u_inCombats', blank = True,)

    # invites = models.ManyToManyField( Pari, blank = True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
