from turtle import title
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

# это не функция, апредставление либо контроллер
def index(request) -> Any:
    context: dict = {
        'title': 'магазинный магазин',
        'content': 'Магазин мебели HOME'

    }

    return render(request, #т.к. директорию темплэйтс джанга будет искать автоматически, мы пишем сразу
                  'main/index.html', context)

def about(request) -> Any:
    context: dict = {
        'title': 'магазинный магазин',
        'content': 'делаем что любим и любим что делаем',
        'text_on_page': 'почему мы игнорим заявки'

    }

    return render(request, #т.к. директорию темплэйтс джанга будет искать автоматически, мы пишем сразу
                  'main/about.html', context)