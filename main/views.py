from turtle import title
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

# это не функция, апредставление либо контроллер
def index(request) -> Any:
    context: dict = {
        'title': 'мэйн',
        'content': 'главная страница мясника джонни',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False

    }

    return render(request, #т.к. директорию темплэйтс джанга будет искать автоматически, мы пишем сразу
                  'main/index.html', context)

def about(request):
    return HttpResponse('About page')