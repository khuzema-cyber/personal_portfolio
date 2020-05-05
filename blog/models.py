from django.db import models

# Create your models here.
class project_blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    describtion = models.TextField()
    image = models.ImageField(upload_to='blog/image' , blank=True)