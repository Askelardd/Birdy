from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    USUARIO_CHOICES = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('admin', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=10, choices=USUARIO_CHOICES, default='aluno')
    pontos = models.IntegerField(default=0)  

    # Adicione outros campos específicos do perfil, se necessário

    def __str__(self):
        return self.user.username   


class Pergunta(models.Model):
    CATEGORIA_CHOICES = [
        ('geometria_plana', 'Geometria Plana'),
        ('operacoes_basicas', 'Operações Básicas'),
        ('fracoes', 'Frações'),
        ('porcentagens', 'Porcentagens'),
    ]

    pergunta_texto = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to='assets/', blank=True, null=True)
    resposta1 = models.CharField(max_length=20, blank=True)
    resposta2 = models.CharField(max_length=20, blank=True)
    resposta3 = models.CharField(max_length=20, blank=True)
    resposta4 = models.CharField(max_length=20, blank=True)
    respostacerta = models.CharField(max_length=20, blank=True)
    solucao = models.ImageField(upload_to='assets/', blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, blank=True,)

    def __str__(self):
        return f"{self.pergunta_texto} - {self.categoria}"
    
    
class Topico(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Questao(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    pergunta = models.TextField()

    def __str__(self):
        return self.pergunta

class Resposta(models.Model):
    questao = models.ForeignKey(Questao, related_name='respostas', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    resposta = models.TextField()

    def __str__(self):
        return self.resposta
    
