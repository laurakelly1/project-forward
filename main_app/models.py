from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your models here.
PROJECT_TYPE = (
    ('P', 'Personal Project'),
    ('O', 'Other'),
)

class Color(models.Model):
    name = models.CharField(max_length=100)
    hex = models.CharField(max_length=7, default='#000000')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ColorScheme(models.Model):
    name = models.CharField(max_length=100)
    background = models.ManyToManyField(Color, blank=True, related_name='background')
    heading = models.ManyToManyField(Color, blank=True, related_name='heading')
    color = models.ManyToManyField(Color, blank=True, related_name='color')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('color_scheme_detail', kwargs={'color_scheme_id': self.id})
   
class Project(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=250, blank=True)
    date_published = models.DateField('date published', blank=True, null=True)
    live_site = models.URLField('live site', blank=True)
    github = models.URLField('github link', blank=True)
    project_type = models.CharField(max_length=1, choices=PROJECT_TYPE, default=PROJECT_TYPE[0][0])

    color_scheme = models.ManyToManyField(ColorScheme, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'project_id': self.id})

    def __str__(self):
        return self.name
