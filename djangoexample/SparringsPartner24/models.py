from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class UserProfile(AbstractUser):
    # add additional fields in here
    phone_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

class FighterProfile(models.Model):
    userprofile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length = 400, blank = True, null = True)
    gender = models.CharField(max_length = 40, blank= True, null = True)
    birthday = models.DateField(blank=True, null=True)
    experience_years = models.IntegerField(blank = True, null = True)
    location = models.CharField(max_length=200, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    martial_art = models.CharField(max_length=200, blank=True, null=True)
    gym = models.CharField(max_length=300, blank=True, null=True)
    trainer = models.CharField(max_length=200, blank=True, null=True)
    fight_record = models.IntegerField(blank=True, null=True)


class SearchProfile(models.Model):
    userprofile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    max_distance = models.IntegerField(blank=True, null=True)
    martial_art = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=40, blank=True, null=True)

    max_weight = models.IntegerField(blank=True, null=True)
    min_weight = models.IntegerField(blank=True, null=True)

    max_age = models.IntegerField(blank=True, null=True)
    min_age = models.IntegerField(blank=True, null=True)

    max_fights = models.IntegerField(blank=True, null = True)
    min_fights = models.IntegerField(blank = True, null = True)
    
    max_experience_years = models.IntegerField(blank = True, null = True)
    min_experience_years = models.IntegerField(blank=True, null = True)


    

