from django.db import models

class aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    senha = models.CharField(max_length=70)  # Este campo pode armazenar senhas criptografadas, ou você pode usar o modelo User do Django.

    def __str__(self):
        return f"{self.id_aluno} - {self.nome} - {self.senha} "
