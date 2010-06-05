# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase


class LolTest(TestCase):

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_lol(self):
        url = reverse('lol')
        data = {'lol': 'Bonjour'}
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Partagé' in response.content)

    def test_share(self):
        url = reverse('share')
        data = {'text': 'Bonjour', 'loltext': 'Lol Bonjour', 'action': 'share'}
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
