from django.test import TestCase

from ..models import Food
from categories.models import Category


class TestFood(TestCase):
    def test_food_should_have_name_and_category_field(self):
        #Given
        food_name = 'Shimi Shabu'
        category_name = 'Buffet'
        category = Category.objects.create(name=category_name)

        #When
        food = food.objects.create(name=food_name, category=category_gory)

        #Then
        self.assertEqual(food.name, food_name)
        self.assertEqual(food.category.name, category.name)