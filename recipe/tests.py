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

    
