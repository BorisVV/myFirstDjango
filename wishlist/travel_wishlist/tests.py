from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Place

class TestViewHomePageIsEmpty(TestCase):
    """docstring for TestViewHomePageIsEmpty."""
    def test_load_home_page_shows_empty(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(reverse('place_list'))
        self.assertFalse(response.context['places']) # Empty lists are false
