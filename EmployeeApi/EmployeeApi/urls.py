from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyApi.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('getToken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('refreshToken/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('verifyToken/', TokenVerifyView.as_view(), name='token_verify'),
]
