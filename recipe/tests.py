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


    

    
