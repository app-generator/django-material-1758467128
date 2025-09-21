# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Users(models.Model):

    #__Users_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    full_name = models.TextField(max_length=255, null=True, blank=True)
    hashed_password = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)
    hourly_rate = models.CharField(max_length=255, null=True, blank=True)
    xp = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    streak = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    phone_number = models.TextField(max_length=255, null=True, blank=True)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Time_Entries(models.Model):

    #__Time_Entries_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    start_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    location = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)
    hours = models.CharField(max_length=255, null=True, blank=True)
    rate = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)

    #__Time_Entries_FIELDS__END

    class Meta:
        verbose_name        = _("Time_Entries")
        verbose_name_plural = _("Time_Entries")


class Plans(models.Model):

    #__Plans_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    title = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    period = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    published = models.BooleanField()
    created_by = models.IntegerField(null=True, blank=True)

    #__Plans_FIELDS__END

    class Meta:
        verbose_name        = _("Plans")
        verbose_name_plural = _("Plans")



#__MODELS__END
