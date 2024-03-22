# Arquivo que configura a página de admin

from django.contrib import admin
from galeria.models import Fotografia

# classe para personalizar o layout dos dados da galeria

class ListandoFotografias(admin.ModelAdmin):
    # personalizando a lista de itens de acordo com qual coluna desejo visualizar, e onde posso clicar
    list_display = ('id', 'nome', 'legenda', 'publicado')
    list_display_links = ('id', 'nome')
    # cria um campo de busca (se houver apenas um item, adicionar uma vírgula para ser tratado como tupla)
    search_fields = ('nome',)
    # cria um campo de filtro para acessar diretamente os dados de cada categoria
    list_filter = ('categoria',)
    # permite a interação com o campo sem ter que acessá-lo diretamente
    list_editable = ('publicado',)
    # limitando itens por página
    list_per_page = 10

# método que configura tudo o que foi criado
admin.site.register(Fotografia, ListandoFotografias)