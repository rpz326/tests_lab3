from django.test import TestCase
from django.urls import reverse
from recipe_catalog.models import Recipe

class TestRoutes(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="Тестовый рецепт",
            summary="Тестовое описание",
            instructions="1. Шаг 1. 2. Шаг 2.",
        )

    def test_recipe_list_route(self):
        """Тест списка рецептов."""
        response = self.client.get(reverse("recipe_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Все рецепты")

    def test_recipe_detail_route(self):
        """Тест конкретного рецепта."""
        response = self.client.get(f"/recipe/{self.recipe.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Рецепт:")
    def test_about_route(self):
        """Тест страницы о сервисе."""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "О сервисе")