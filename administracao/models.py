from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 255)
    create_at = models.DateTimeField(auto_now_add = True)


class ProfissionalSaude(models.Model):
    funcao = models.CharField(max_length = 255)
    pessoas = models.ForeignKey(Pessoa, related_name='pessoa', on_delete=models.CASCADE)


# Create your models here.
