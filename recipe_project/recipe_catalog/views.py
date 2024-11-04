import requests
from django.shortcuts import render
from django.conf import settings

API_KEY = "d7a1dab7d21149f8a233065b48dfe1d8"

def recipe_list(request):
    url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}"
    response = requests.get(url)
    recipes = response.json().get('results', [])
    return render(request, 'recipe_catalog/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}"
    response = requests.get(url)
    recipe = response.json()
    return render(request, 'recipe_catalog/recipe_detail.html', {'recipe': recipe})

def about(request):
    return render(request, 'recipe_catalog/about.html')
