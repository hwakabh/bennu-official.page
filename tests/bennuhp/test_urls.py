from django.test import TestCase
from django.urls import reverse, resolve

from bennuhp.views import *


class TestUrls(TestCase):
    # Initial setup for class instantiation
    @classmethod
    def setUpTestData(self):
        pass

    # Common setup logics for each test case here
    def setUp(self):
        pass


    def test_healthz_url(self):
        url = reverse('bennuhp:healthz')
        self.assertEqual(resolve(url).func.view_class, HealthzView)

    def test_home_url(self):
        url = reverse('bennuhp:root')
        self.assertEqual(resolve(url).func.view_class, AppRootTemplateView)

    def test_biography_url(self):
        url = reverse('bennuhp:bio')
        self.assertEqual(resolve(url).func.view_class, BioTemplateView)

    def test_discography_url(self):
        url = reverse('bennuhp:disco')
        self.assertEqual(resolve(url).func.view_class, DiscoListView)

    def test_lives_url(self):
        url = reverse('bennuhp:live')
        self.assertEqual(resolve(url).func.view_class, LivesListView)
