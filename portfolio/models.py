from django.db import models

# Create your models here.

class project(models.Model):

    title = models.CharField(max_length=200)
    describtion = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/image/')
    urls = models.URLField(blank= True)

class project2(models.Model):

    title = models.CharField(max_length=200)
    describtion = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio2/image/' ,blank=True)
    urls = models.URLField(blank=True)
