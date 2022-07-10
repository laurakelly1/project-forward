from django.db import models

# Create your models here.
class ColorScheme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date_published = models.DateField('date published')
    live_site = models.URLField('live site')
    github = models.URLField('github link')

    color_scheme = models.ManyToManyField(ColorScheme)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)
    hex = models.CharField(max_length=7, default='#000000')
    color_scheme = models.ForeignKey(ColorScheme, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
