from django.db import models
from django.contrib.auth.models import AbstractUser,Group

class User(AbstractUser):
    CREATOR='CREATOR'
    SUBSCRIBER='SUBSCRIBER'
    ROLE_CHOICES=((CREATOR,'Createur'),(SUBSCRIBER,'Abonne'))
    profile_photo=models.ImageField(verbose_name='Profil photo')
    role=models.CharField(max_length=68,choices=ROLE_CHOICES,verbose_name='Role')
    follows=models.ManyToManyField('self',limit_choices_to={'role':CREATOR},symmetrical=False,verbose_name='suit')
    def save(self):
        super.save()
        if self.role == self.CREATOR:
            group=Group.objects.get(name='creators')
            group.user_set.add(self)
        elif self.role==self.SUBSCRIBER:
            group=Group.objects.get(name='subscribers')
            group.user_set.add(self)