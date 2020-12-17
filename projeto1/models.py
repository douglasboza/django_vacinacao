from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 255)
    create_at = models.DateTimeField(auto_now_add = True)


# Create your models here.
