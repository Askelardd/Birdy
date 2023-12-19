from django.db import models

class Pergunta(models.Model):
    pergunta_texto = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to='assets/', blank=True, null=True)
    resposta1 = models.CharField(max_length=20, blank = True)
    resposta2 = models.CharField(max_length=20,blank = True)
    resposta3 = models.CharField(max_length=20,blank = True)
    resposta4 = models.CharField(max_length=20,blank = True)
    respostacerta = models.CharField(max_length=20,blank = True)
    solucao = models.ImageField(upload_to='assets/', blank=True, null=True)

    def __str__(self):
        return f"{self.pergunta_texto} - {self.imagem}- {self.resposta1}"
     