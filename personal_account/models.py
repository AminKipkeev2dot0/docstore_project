from contextlib import nullcontext
from email.policy import default
from multiprocessing.sharedctypes import Value
from django import forms
from django.db import models




from docstore.settings import MEDIA_ROOT


# Create your models here.
class Doc(models.Model):
    title=models.CharField(null=True,max_length=100)
    descr=models.TextField(null=True)
    scan=models.FileField(null=True,upload_to='docs/')    

