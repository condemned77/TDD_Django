from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):
  def test_root_url_resolves_to_home_page_view(self):
      # does the 'resolve' function find a 'view function', when "/" is called
      found = resolve("/")
      # the 'view function' expected to be found is called 'home_page'
      self.assertEqual(found.func, home_page)

  def test_home_page_returns_correct_html(self):
    # assemble
    request   = HttpRequest()

    # act
    response  = home_page(request)

    # assert
    received_bytes  = response.content
    html            = received_bytes.decode('utf8')
    self.assertTrue(html.startswith('<html>'))
    self.assertIn('<title>To-Do lists</title>', html)
    self.assertTrue(html.endswith('</html>'))

