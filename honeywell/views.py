from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Recipe

def index(request):
    list_of_recipes = Recipe.objects.all()
    context = {'list_of_recipes': list_of_recipes}
    return render(request, 'honeywell/index.html', context)

def detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'honeywell/detail.html', {'recipe': recipe})
