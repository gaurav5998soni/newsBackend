from django.db import models
from django.conf import settings
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time  = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='my_iamge/', null=True)
    image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.image_url = "http://gourav5998soni.pythonanywhere.com"+str(self.image.url)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class Trending(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time  = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='my_iamge/', null=True)
    image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.image_url = "http://gourav5998soni.pythonanywhere.com"+str(self.image.url)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class TimeLineData(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time  = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='my_iamge/', null=True)
    image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.image_url = "http://gourav5998soni.pythonanywhere.com"+str(self.image.url)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class Ad(models.Model):
    image = models.ImageField(upload_to='my_iamge/', null=True)
    image_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.image_url = "http://gourav5998soni.pythonanywhere.com"+str(self.image.url)
        super().save(*args, **kwargs)

