import requests
from django.http import JsonResponse
from .openweather import get_temperature
from .spotify import get_music_by_genre
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class MusicSuggestionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, city_name):
        try:

            temperature = get_temperature(city_name)

            if temperature == 'City not found':
                return JsonResponse({'error': 'City not found'}, status=404)
            
            if temperature > 25:
                genre = 'Pop' 
            elif 10 <= temperature <= 25:
                genre = 'Rock'
            else:
                genre = 'Classical'

            playlist = get_music_by_genre(genre)
            
            return JsonResponse({
                'city': city_name,
                'temperature': temperature,
                'genre': genre,
                'playlist': playlist
            }, json_dumps_params={'ensure_ascii': False})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': f'Error fetching weather data: {str(e)}'}, status=500)
        except KeyError as e:
            return JsonResponse({'error': f'Missing expected data in weather response: {str(e)}'}, status=500)
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=500)


class DocumentationView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        documentation = {
            "description": "API para sugerir músicas baseado na temperatura da cidade.",
            "endpoints": {
                "/suggest/<city_name>/": {
                    "description": "Retorna uma playlist de acordo com a temperatura atual da cidade.",
                    "method": "GET",
                    "parameters": {
                        "city_name": "Nome da cidade para obter a temperatura atual."
                    },
                    "responses": {
                        "200": {
                            "description": "Requisição bem-sucedida.",
                            "example": {
                                "city": "São Paulo",
                                "temperature": 28,
                                "genre": "pop",
                                "playlist": [
                                    {"name": "Song1", "artist": "Artist1", "url": "https://spotify.com/track1"},
                                    {"name": "Song2", "artist": "Artist2", "url": "https://spotify.com/track2"},
                                ]
                            }
                        },
                        "500": {
                            "description": "Erro interno do servidor."
                        }
                    }
                },
                "/api/token/": {
                    "description": "Gera um token JWT para autenticação.",
                    "method": "POST",
                    "parameters": {
                        "username": "Nome de usuário.",
                        "password": "Senha do usuário."
                    },
                    "responses": {
                        "200": {
                            "description": "Token gerado com sucesso.",
                            "example": {
                                "refresh": "refresh_token_value",
                                "access": "access_token_value"
                            }
                        },
                        "401": {
                            "description": "Credenciais inválidas."
                        }
                    }
                },
                "/api/token/refresh/": {
                    "description": "Renova um token JWT usando o refresh token.",
                    "method": "POST",
                    "parameters": {
                        "refresh": "Refresh token."
                    },
                    "responses": {
                        "200": {
                            "description": "Token renovado com sucesso.",
                            "example": {
                                "access": "new_access_token_value"
                            }
                        },
                        "401": {
                            "description": "Refresh token inválido ou expirado."
                        }
                    }
                }
            }
        }
        return JsonResponse(documentation, json_dumps_params={'ensure_ascii': False})


def custom_404(request, exception):
    return JsonResponse({'error': 'Endpoint not found'}, status=404)

def custom_403(request, exception):
    return JsonResponse({'error': 'Forbidden'}, status=403)

def custom_401(request, exception):
    return JsonResponse({'error': 'Unauthorized'}, status=401)