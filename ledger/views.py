from django.shortcuts import render
import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
data_dir = os.path.join(BASE_DIR, 'data')
templates_dir = os.path.join(BASE_DIR, 'templates')

def recipe_list(request):
    recipe_list_file = os.path.join(data_dir, 'Recipe List Context.txt')
    with open(recipe_list_file, 'r') as file:
        ctx = {'recipe_list': file.read().split('\n')}
    html_file_path = os.path.join(templates_dir, 'recipe_list.html')
    return render(request, html_file_path, ctx)

def recipe_detail_1(request):
    recipe_detail_file = os.path.join(data_dir, 'Recipe 1.txt')
    with open(recipe_detail_file, 'r') as file:
        recipe_detail = json.load(file)
    ctx = {'recipe_detail': recipe_detail}
    html_file_path = os.path.join(templates_dir, 'recipe_detail_1.html')
    return render(request, html_file_path, ctx)

def recipe_detail_2(request):
    recipe_detail_file = os.path.join(data_dir, 'Recipe 2.txt')
    with open(recipe_detail_file, 'r') as file:
        recipe_detail = json.load(file)
    ctx = {'recipe_detail': recipe_detail}
    html_file_path = os.path.join(templates_dir, 'recipe_detail_2.html')
    return render(request, html_file_path, ctx)
