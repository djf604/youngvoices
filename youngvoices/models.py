from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_quizes_taken = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)
