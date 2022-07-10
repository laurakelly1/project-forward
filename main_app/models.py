from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=100)
    hex = models.CharField(max_length=7, default='#000000')

    def __str__(self):
        return self.name

class ColorScheme(models.Model):
    name = models.CharField(max_length=100)
    color = models.ManyToManyField(Color, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=250, blank=True)
    date_published = models.DateField('date published', blank=True, null=True)
    live_site = models.URLField('live site', blank=True)
    github = models.URLField('github link', blank=True)

    color_scheme = models.ManyToManyField(ColorScheme, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'project_id': self.id})

    def __str__(self):
        return self.name
