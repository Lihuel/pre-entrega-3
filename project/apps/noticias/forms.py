from django import forms
from . import models

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = models.Noticia
        fields = '__all__'