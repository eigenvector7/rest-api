from django.test import TestCase
from django.urls import resolve
from . import views


# Create your tests here.
class SmokeTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.home_page)
