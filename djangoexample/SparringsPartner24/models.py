from django.db import models
import datetime
from django.utils import timezone

class UserProfile(models.Model):
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    MailAdress = models.EmailField()
    PhoneNumber = models.IntegerField(blank=True, null=True)


class FighterProfile(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
    BirthDay = models.DateField(blank=True, null=True)
    Location = models.CharField(max_length=200, blank=True, null=True)
    Weight = models.IntegerField(blank=True, null=True)
    MartialArt = models.CharField(max_length=200, blank=True, null=True)
    Gym = models.CharField(max_length=300, blank=True, null=True)
    Trainer = models.CharField(max_length=200, blank=True, null=True)
    FightRecord = models.IntegerField(blank=True, null=True)


class SearchProfile(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default = 1)
    MaxWeight = models.IntegerField(blank=True, null=True)
    MinWeight = models.IntegerField(blank=True, null=True)
    MartialArt = models.CharField(max_length=200, blank=True, null=True)
    MaxDistance = models.IntegerField(blank=True, null=True)
    MinAge = models.IntegerField(blank=True, null=True)
    MaxAge = models.IntegerField(blank=True, null=True)

