# Generated by Django 5.0.2 on 2024-03-04 05:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_recipe_recipeingredient_rename_recipebook_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='name',
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='ledger.ingredient'),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='ledger.recipe'),
        ),
    ]
