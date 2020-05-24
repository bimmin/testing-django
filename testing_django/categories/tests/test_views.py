from django.test import TestCase

from ..models import Category


class TestCategoryList(TestCase):
    def test_category_list_should_display_on_page(self):
        Category.objects.create(name='Street Food')
        Category.objects.create(name='Elite')

        response = self.client.get('/categories/')

        self.assertContains(response, '<li>Street Food</li>')
        self.assertContains(response, '<li>Elite</li>')
