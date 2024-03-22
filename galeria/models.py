from django.db import models
from datetime import datetime
# sempre que alterar o models, realizar o migration

class Fotografia(models.Model):
    # Criar uma lista para definir a categoria. Deve ser uma tupla pois o método charfield entende tuplas
    opcoes_categorias = [

        ('Nebulosa', 'NEBULOSA'),
        ('Estrela', 'ESTRELA'),
        ('Galáxia', 'GALÁXIA'),
        ('Planeta', 'PLANETA')

    ]

    nome = models.CharField(max_length=150, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes_categorias, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)
    publicado = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'