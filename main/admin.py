from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from main.models import aluno


@admin.register(aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id_aluno', 'nome', 'email','senha')
    
    actions = ['excluir_alunos']

    def excluir_alunos(modeladmin, request, queryset):
        # Certifique-se de que 'excluir_alunos' corresponda ao nome da função de ação
        for aluno_obj in queryset:
            aluno_obj.delete()

    excluir_alunos.short_description = "Excluir alunos selecionados"
    
    def editar_link(self, obj):
        # Cria um link para a página de edição personalizada
        url = reverse('admin:main_aluno_change', args=[obj.id])
        return format_html('<a href="{}">Editar</a>', url)

    editar_link.short_description = 'Editar'
    editar_link.allow_tags = True

    

