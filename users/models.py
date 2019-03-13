# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Prefer not to say')
    )
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)

    birthdate = models.DateField(max_length=8)

    PLAN_CHOICES = (
        ('Free', 'Free'),
        ('Pro', 'Pro - $9.99/mo'),
    )
    plan = models.CharField(max_length=30, choices=PLAN_CHOICES)