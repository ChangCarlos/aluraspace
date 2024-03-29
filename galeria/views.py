from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    # fotografias = Fotografia.objects.all()
    # alterando o código para seguir a lógica de exibir somente os publicados e ordenado pelo parâmetro passado
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicado=True)

    return render(request, 'index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'imagem.html', {'fotografia': fotografia})