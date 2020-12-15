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

    # Parier
    # parierSurAutres = models.ManyToManyField( AutrePari, related_name='p_inAutres', blank = True,)
    # parierSurMatchs = models.ManyToManyField( Match, related_name='p_inMatchs', blank = True,)
    # parierSurCombats = models.ManyToManyField( Combat, related_name='p_inCombats', blank = True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UserMatch(models.Model):
    user = models.ForeignKey(User,
        # verbose_name=('Reviewer for semester'),
        on_delete=models.PROTECT
    )

    match = models.ForeignKey(Match,
        # verbose_name=_('Semester reviewer'),
        on_delete=models.PROTECT
    )

    pari = models.CharField(max_length=10)

class UserCombat(models.Model):
    user = models.ForeignKey(User,
        # verbose_name=('Reviewer for semester'),
        on_delete=models.PROTECT
    )

    combat = models.ForeignKey(Combat,
        # verbose_name=_('Semester reviewer'),
        on_delete=models.PROTECT
    )

    pari = models.CharField(max_length=10)

class UserAutre(models.Model):
    user = models.ForeignKey(User,
        # verbose_name=('Reviewer for semester'),
        on_delete=models.PROTECT
    )

    autre = models.ForeignKey(AutrePari,
        # verbose_name=_('Semester reviewer'),
        on_delete=models.PROTECT
    )

    pari = models.CharField(max_length=10)
