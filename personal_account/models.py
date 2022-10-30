from django import forms
from django import forms
from django.db import models
from django.forms import FileField


from docstore.settings import MEDIA_ROOT


# Create your models here.
class Doc(models.Model):
    title=models.CharField(max_length=100)
    descr=models.TextField()
    scan=FileField(upload_to='scans')
