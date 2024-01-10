from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class IndexURLTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)


class IndexViewTestCase(TestCase):
    def test_index_view(self):
        url = reverse('index')

        response = self.client.get(url)
        self.assertTemplateUsed(response, 'index.html')
        # self.assertEqual(response.context['text'], 'Hello World!')
