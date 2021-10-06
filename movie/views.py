from django.shortcuts import render
from .models import movie
# Create your views here.
def search(request):
    x=request.GET['search']
    info=movie.objects.filter(name__icontains=x)
    context={"info":info}
    return render(request, 'movie/search.html', context)

def movieinfo(request, item_id):
    x=movie.objects.get(id=item_id)
    return render(request, 'movie/movieinfo.html',{'x':x})

def checkout(request):
    return render(request, 'movie/checkout.html')