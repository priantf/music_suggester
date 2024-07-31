from django.urls import path
from .views import MusicSuggestionView, DocumentationView, custom_404, custom_403, custom_401

urlpatterns = [
    path('suggest/<str:city_name>/', MusicSuggestionView.as_view(), name='music_suggestion'),
    path('doc/', DocumentationView.as_view(), name='api_documentation'),
]

handler404 = custom_404
handler403 = custom_403
handler401 = custom_401
