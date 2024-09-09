from django.shortcuts import render
from django.template import context

from goods.models import Products

# Create your views here.
def catalog(request):

    goods = Products.objects.all()

    context = {
        'title': 'Hohome - КатАлог каталОг ка ко коу коу',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context) 

def product(request):
    return render(request, 'goods/product.html')