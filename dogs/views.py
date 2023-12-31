from django.shortcuts import render
from dogs.models import Category, Dog


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


def category_dogs(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'objects_list': Dog.objects.filter(category=pk),
        'title': f'Собаки породы - все наши породы {category_item.name}',
    }
    return render(request, 'dogs/dogs.html', context)
