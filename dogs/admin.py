from django.contrib import admin

from dogs.models import Dog, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'descriptions')


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'photo', 'birth_day')
    list_filter = ('category',)
