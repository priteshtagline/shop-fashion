from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Color


class ColorForm(ModelForm):
    """
    Color model form override with Django ModelForm.
    color_code field type change text to color. 
    So, Django admin color_code field in open colorpicker and choice the color.
    """
    class Meta:
        model = Color
        fields = '__all__'
        widgets = {
            'color_code': TextInput(attrs={'type': 'color'}),
        }
