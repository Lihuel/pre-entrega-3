from django import forms

from . import models

class EquipoForm(forms.ModelForm):
    class Meta:
        model = models.Equipo
        fields = '__all__'