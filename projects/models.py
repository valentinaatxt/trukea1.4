import imp
from django.db import models
import email
import enum
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    document = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)

def _str_(self):
    return self.name
