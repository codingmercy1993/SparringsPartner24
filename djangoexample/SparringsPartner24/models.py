from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class UserProfile(AbstractUser):
    # add additional fields in here
    PhoneNumber = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

class FighterProfile(models.Model):
    userprofile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    BirthDay = models.DateField(blank=True, null=True)
    Location = models.CharField(max_length=200, blank=True, null=True)
    Weight = models.IntegerField(blank=True, null=True)
    MartialArt = models.CharField(max_length=200, blank=True, null=True)
    Gym = models.CharField(max_length=300, blank=True, null=True)
    Trainer = models.CharField(max_length=200, blank=True, null=True)
    FightRecord = models.IntegerField(blank=True, null=True)


class SearchProfile(models.Model):
    userprofile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    MaxWeight = models.IntegerField(blank=True, null=True)
    MinWeight = models.IntegerField(blank=True, null=True)
    MartialArt = models.CharField(max_length=200, blank=True, null=True)
    MaxDistance = models.IntegerField(blank=True, null=True)
    MinAge = models.IntegerField(blank=True, null=True)
    MaxAge = models.IntegerField(blank=True, null=True)

