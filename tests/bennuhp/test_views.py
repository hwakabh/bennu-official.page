from django.test import TestCase

from bennuhp.views import *


class TestsRoutesStatusCode(TestCase):
    def setUp(self):
        # Common setup logics for each test case here
        pass

    def test_healthz_success(self):
        resp = self.client.get('/home/')
        self.assertEqual(resp.status_code, 200)

    def test_healthz_body_ok(self):
        resp = self.client.get('/healthz')
        body = {'status': 'ok'}
        self.assertJSONEqual(resp.content, body)

    def test_home_success(self):
        resp = self.client.get('/home/')
        self.assertEqual(resp.status_code, 200)

    def test_bio_success(self):
        resp = self.client.get('/biography/')
        self.assertEqual(resp.status_code, 200)

    def test_disco_success(self):
        resp = self.client.get('/discography/')
        self.assertEqual(resp.status_code, 200)

    def test_live_success(self):
        resp = self.client.get('/lives/')
        self.assertEqual(resp.status_code, 200)

