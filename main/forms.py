from django import forms
from .models import aluno


class RegistarAluno(forms.ModelForm):
    class Meta:
        model = aluno
        fields = ['nome', 'email', 'senha']
        
