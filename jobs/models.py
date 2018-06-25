from django.db import models

# Create your models here.
from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    summary = models.CharField(max_length=200)
    referenceurl = models.CharField(max_length=255)
