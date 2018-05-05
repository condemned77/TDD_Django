from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        # does the 'resolve' function find a 'view function', when "/" is called
        found = resolve("/")
        # the 'view function' expected to be found is called 'home_page'
        self.assertEqual(found.func, home_page)
