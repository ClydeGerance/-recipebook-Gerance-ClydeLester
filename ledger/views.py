from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **args):
        context = super().get_context_data(**args)
        ingredients = self.object.ingredients.all()
        context['recipe_ingredients'] = ingredients
        return context
