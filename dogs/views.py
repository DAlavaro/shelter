from django.shortcuts import render

from dogs.models import Category


def index(request):
    context = {
        'objects_list': Category.objects.all()[0:3],
        'title': 'Главная страница'
    }
    return render(request, 'dogs/index.html', context)


def categories(request):
    context = {
        'objects_list': Category.objects.all(),
        'title': 'Питомник - Все наши породы'
    }
    return render(request, 'dogs/categories.html', context)
