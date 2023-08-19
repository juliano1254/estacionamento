from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    mensagem = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome