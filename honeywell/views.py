from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Recipe

def index(request):
    list_of_recipes = Recipe.objects.all()
    template = loader.get_template('honeywell/index.html')
    context = {
        'list_of_recipes': list_of_recipes,
    }
    return HttpResponse(template.render(context, request))

