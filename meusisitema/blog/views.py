from django.shortcuts import render
from blog.models import Noticia


# Create your views here.
def index(request):

    noticias = Noticia.objects.all()
   
    print(noticias)
    return render(request, 'index.html', {'noticias': noticias})