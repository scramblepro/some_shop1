from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# это не функция, а представление либо контроллер
def index(request):
    
    categories = Categories.objects.all()

    context = {
        'title': 'магазинный магазин',
        'content': 'Магазин мебели HOME',
        'categories': categories

    }

    return render(request, #т.к. директорию темплэйтс джанга будет искать автоматически, мы пишем сразу
                  'main/index.html', context)

def about(request):
    context = {
        'title': 'магазинный магазин',
        'content': 'делаем что любим и любим что делаем',
        'text_on_page': 'почему мы игнорим заявки'

    }

    return render(request, #т.к. директорию темплэйтс джанга будет искать автоматически, мы пишем сразу
                  'main/about.html', context)