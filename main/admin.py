from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from main.models import Pergunta

# @admin.register(Pergunta)
# class PerguntaAdmin(admin.ModelAdmin):
#     list_display = ('pergunta_texto', 'resposta1', 'resposta2', 'resposta3', 'resposta4')

admin.site.register(Pergunta)

