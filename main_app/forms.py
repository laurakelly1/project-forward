from django.forms import ModelForm
from .models import ColorScheme, Color

class ColorSchemeForm(ModelForm):
    class Meta:
        model = ColorScheme
        fields = ['name', 'color']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ColorSchemeForm, self).__init__(*args, **kwargs)
        self.fields['color'].queryset = Color.objects.filter(user=user)