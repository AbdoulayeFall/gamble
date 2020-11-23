import uuid

from django.db import models

from enum import Enum, unique

@unique
class PariType(Enum):
    MATCH = 'Match'
    COMBAT = 'Combat'
    AUTREPARI = 'AutrePari'

class Pari(models.Model):
    name = models.CharField(max_length=100)
    resultat = models.CharField(max_length=100)
    jour = models.DateField()

    class Meta:
        abstract = True

class Match(Pari):
    equipe1 = models.CharField(max_length=100)
    equipe2 = models.CharField(max_length=100)

class Combat(Pari):
    joueur1 = models.CharField(max_length=100)
    joueur2 = models.CharField(max_length=100)

class AutrePari(Pari):
    description = models.CharField(max_length=100)
