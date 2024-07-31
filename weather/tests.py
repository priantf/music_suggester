from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class MusicSuggestionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.token = 'your_access_token'
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {self.access_token}'

    @patch('weather.views.requests.get')
    def test_music_suggestion_pop(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'main': {'temp': 30}
        }
        response = self.client.get(reverse('music_suggestion', args=['Rio de Janeiro']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['genre'], 'Pop')

    @patch('weather.views.requests.get')
    def test_music_suggestion_rock(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'main': {'temp': 20}
        }
        response = self.client.get(reverse('music_suggestion', args=['São Paulo']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['genre'], 'Rock')

    @patch('weather.views.requests.get')
    def test_music_suggestion_classical(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'main': {'temp': 5}
        }
        response = self.client.get(reverse('music_suggestion', args=['Curitiba']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['genre'], 'Classical')

    @patch('weather.views.requests.get')
    def test_city_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        response = self.client.get(reverse('music_suggestion', args=['CidadeInexistente']))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], 'City not found')
