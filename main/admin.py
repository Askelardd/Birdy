from django.contrib import admin
from .models import aluno

@admin.register(aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id_aluno', 'nome', 'email')    