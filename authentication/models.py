from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CREATOR='CREATOR'
    SUBSCRIBER='SUBSCRIBER'
    ROLE_CHOICES=((CREATOR,'Createur'),(SUBSCRIBER,'Abonne'))
    profile_photo=models.ImageField(verbose_name='Profil photo')
    role=models.CharField(max_length=68,choices=ROLE_CHOICES,verbose_name='Role')