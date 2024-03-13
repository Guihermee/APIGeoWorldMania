from django.db import models

# Create your models here.

class Bandeira(models.Model):
    nome = models.CharField(max_length=100)
    # imagem = models.ImageField(upload_to='bandeiras/', use_url=True)
    imagem = models.URLField()
    descricao = models.TextField()
    continente = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Pais(models.Model):
    nome = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    continente = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
