from django.test import TestCase
from recipe_catalog.models import Recipe

class TestContent(TestCase):
    def test_recipe_creation(self):
        """Тест создания объекта модели Recipe."""
        recipe = Recipe.objects.create(
            title="Омлет с сыром",
            summary="Простой и вкусный завтрак.",
            instructions="1. Взбейте яйца с молоком. 2. Добавьте сыр. 3. Обжарьте.",
        )
        self.assertEqual(recipe.title, "Омлет с сыром")
        self.assertEqual(recipe.summary, "Простой и вкусный завтрак.")
        self.assertEqual(recipe.instructions, "1. Взбейте яйца с молоком. 2. Добавьте сыр. 3. Обжарьте.")

    def test_sorted_list_output(self):
        """Тест сортировки списка рецептов по алфавиту."""
        Recipe.objects.create(title="Омлет с сыром")
        Recipe.objects.create(title="Картофельное пюре")
        Recipe.objects.create(title="Куриное филе на гриле")

        recipes = Recipe.objects.all().order_by("title")
        titles = [recipe.title for recipe in recipes]
        self.assertEqual(titles, ["Картофельное пюре", "Куриное филе на гриле", "Омлет с сыром"])