from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название рецепта")
    image = models.ImageField(upload_to='recipes/', blank=True, null=True, verbose_name="Изображение")
    summary = models.TextField(verbose_name="Описание", blank=True)
    instructions = models.TextField(verbose_name="Рецепт", blank=True)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE, verbose_name="Рецепт")
    name = models.CharField(max_length=100, verbose_name="Ингредиент")
    quantity = models.CharField(max_length=100, verbose_name="Количество", blank=True)

    def __str__(self):
        return f"{self.name} ({self.quantity})"