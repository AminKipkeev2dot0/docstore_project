from contextlib import nullcontext
from email.policy import default
from multiprocessing.sharedctypes import Value
from django import forms
from django.db import models
from django.forms import ModelForm



from docstore.settings import MEDIA_ROOT


# Create your models here.
class Doc(models.Model):
    title=models.CharField(null=True,max_length=100)
    descr=models.TextField(null=True)
    scan=models.FileField(upload_to='docs/',null=True, blank=True ) 

    class Meta:
        verbose_name_plural = 'Documents'
        verbose_name = 'Document'   




