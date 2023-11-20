from django import forms
from .models import aluno

class alunoForm(forms.ModelForm):
    class Meta:
        model = aluno
        fields = ['nome', 'email', 'senha']