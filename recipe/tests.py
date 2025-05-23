from django.test import TestCase
from .models import Recipe, Category


class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Десерти")

    def test_create_recipe(self):
        recipe = Recipe.objects.create(
            title="Шарлотка",
            description="Простий яблучний пиріг.",
            instructions="Змішати інгредієнти та випікати 40 хвилин.",
            ingredients="яблука, яйця, борошно, цукор",
            category=self.category,
        )
