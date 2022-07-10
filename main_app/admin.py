from django.contrib import admin
from .models import Project, ColorScheme, Color
# Register your models here.
admin.site.register(Project)
admin.site.register(ColorScheme)
admin.site.register(Color)