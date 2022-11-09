from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import index, n_times_string


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')

        self.assertEquals(resolve(url).func, index)

    def test_n_times_string_is_resolved(self):
        url = reverse("multiply")

        self.assertEquals(resolve(url).func, n_times_string)


