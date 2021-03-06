from django.forms import ModelForm
from .models import ColorScheme, Color, Project

class ColorSchemeForm(ModelForm):
    class Meta:
        model = ColorScheme
        fields = ['name', 'background', 'heading', 'color']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ColorSchemeForm, self).__init__(*args, **kwargs)
        self.fields['background'].queryset = Color.objects.filter(user=user)
        self.fields['heading'].queryset = Color.objects.filter(user=user)
        self.fields['color'].queryset = Color.objects.filter(user=user)

class ProjectsForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'developer', 'description', 'date_published', 'live_site', 'github', 'color_scheme', 'project_type']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProjectsForm, self).__init__(*args, **kwargs)
        self.fields['color_scheme'].queryset = ColorScheme.objects.filter(user=user)