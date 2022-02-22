from django.db import models

# Create your models here.

from django.db import models

class  catalogmoc(models.Model):

    faculty = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    discipline = models.TextField(null=True)
    mooc = models.TextField(null=True)
    integration = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    url = models.TextField(null=True)
    plan = models.CharField(max_length=255)
    note = models.TextField(null=True)
    access = models.CharField(max_length=255, null=True)
    weeks = models.CharField(max_length=255, null=True)

