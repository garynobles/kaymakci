# models.py
from django.db import models

class Attachment(models.Model):
    file = models.FileField(upload_to='testing/tests')
