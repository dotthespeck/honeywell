from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from .models import Recipe
from .forms import RecipeForm

def index(request):
    list_of_recipes = Recipe.objects.all()
    context = {'list_of_recipes': list_of_recipes}
    return render(request, 'honeywell/index.html', context)

def detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'honeywell/detail.html', {'recipe': recipe})

def new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'honeywell/new.html', {'form': form})
