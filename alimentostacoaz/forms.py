from django import forms
from alimentostacoaz.models import Alimento


class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = '__all__'
