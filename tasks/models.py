from django.contrib.auth.models import User
from django.db import models

from objects.models import ObjectTable


class TaskTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    task = models.TextField()
    object = models.ForeignKey(ObjectTable, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='photos/done/%Y/%m/%d/')
    done = models.BooleanField(default=False)