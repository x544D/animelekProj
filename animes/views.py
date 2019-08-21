from django.shortcuts import render
from django.http import HttpResponse
from animes.models import Animes

# Create your views here.

def single_animes_view(request,_id):
    obj = Animes.objects.get(id=_id)
    ret = {
         
        'animeObject':obj
    }
    return render(request, "anime_details.html", ret)


def list_animes_view(request):
    objects = Animes.objects.all()
    ret = {
        'animesList':objects        
    }
    return render(request, "animes.html", ret)

