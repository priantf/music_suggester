from django.contrib import admin
from django.urls import path, include
from weather.views import custom_404, custom_401, custom_403
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

handler404 = custom_404
handler403 = custom_403
handler401 = custom_401
