from django import forms
from paciente.models import Paciente
class FormAddPaciente(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'