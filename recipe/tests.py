from django.test import TestCase
from .models import Category, Recipe

# Create your tests here.
class CategoryModelTest(TestCase):
    def setUp(self):
        # Створення тестових даних
        self.category = Category.objects.create(name="Desserts")

    def test_category_creation(self):
        """Тест для перевірки створення об'єкта Category"""
        self.assertEqual(self.category.name, "Desserts")
        self.assertIsInstance(self.category, Category)

    
    def test_category_str_method(self):
        """Тест для перевірки методу __str__"""
        self.assertEqual(str(self.category), "Desserts")

    def test_category_iter_method(self):
        """Тест для перевірки методу __iter__"""
        category_dict = dict(self.category)
        self.assertIn("id", category_dict)
        self.assertIn("name", category_dict)
        self.assertEqual(category_dict["name"], "Desserts")

    
    def test_category_save_and_retrieve(self):
        """Тест для перевірки збереження та отримання об'єкта"""
        saved_category = Category.objects.get(id=self.category.id)
        self.assertEqual(saved_category.name, self.category.name)

        
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

        self.assertEqual(recipe.title, "Шарлотка")
        self.assertEqual(recipe.description, "Простий яблучний пиріг.")
        self.assertIn("яблука", recipe.ingredients)
        self.assertEqual(recipe.category, self.category)
        self.assertEqual(str(recipe), "Шарлотка")

        self.assertIsNotNone(recipe.created_at)
        self.assertIsNotNone(recipe.updated_at)

