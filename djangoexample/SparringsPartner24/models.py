from django.db import models
import datetime
from django.utils import timezone

class UserProfile(models.Model):
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    MailAdress = models.EmailField()


class FighterProfile(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
    BirthDay = models.DateField()
    Location = models.CharField(max_length=200)
    Weight = models.IntegerField()
    MartialArt = models.CharField(max_length=200)
    Gym = models.CharField(max_length=300)
    Trainer = models.CharField(max_length=200)
    FightRecord = models.IntegerField()


class SearchProfile(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default = 1)
    MaxWeight = models.IntegerField()
    MinWeight = models.IntegerField()
    MartialArt = models.CharField(max_length=200)
    MaxDistance = models.IntegerField()

