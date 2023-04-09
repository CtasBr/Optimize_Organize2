from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    s_name = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    p_series = models.CharField(max_length=4, blank=True)
    p_number = models.CharField(max_length=6, blank=True)
    org = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=100, blank=True)



