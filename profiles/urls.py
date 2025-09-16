from django.urls import path
from .views import RegisterView, ProfileV1View, ProfileV2View
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/v1/register/', RegisterView.as_view(), name='register'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/profile/', ProfileV1View.as_view(), name='profile_v1'),
    path('api/v2/profile/', ProfileV2View.as_view(), name='profile_v2'),
]
