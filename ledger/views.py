from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'
    login_url = reverse_lazy('login')

    def get_context_data(self, **args):
        context = super().get_context_data(**args)
        ingredients = self.object.ingredients.all()
        context['recipe_ingredients'] = ingredients
        return context

class CustomLoginView(DjangoLoginView):
    def get_success_url(self) -> str:
        return reverse_lazy('recipe_list')
            