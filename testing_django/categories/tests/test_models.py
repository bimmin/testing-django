from django.test import TestCase

from ..models import Category


class TestCategory(TestCase):
    def test_category_should_have_name_field(self):
        name = 'Personal'
        category = Category.objects.create(name=name)
        self.assertEqual(category.name, name)