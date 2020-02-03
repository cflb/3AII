from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=200)
    noticia = models.TextField(verbose_name='Notícia')
    data_public = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo