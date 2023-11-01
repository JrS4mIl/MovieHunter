from django.db import models

# Create your models here.
class GeneralSetting(models.Model):
    title=models.CharField(max_length=20,blank=True)
    icerik=models.CharField(max_length=50,blank=True)
    paramater=models.CharField(max_length=50,blank=True)
class ImageSetting(models.Model):
    name=models.CharField(default='',max_length=200,blank=True)
    icerik=models.CharField(default='',max_length=200,blank=True)
    file=models.ImageField(default='',upload_to='moive_image')