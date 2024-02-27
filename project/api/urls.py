from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView


urlpatterns = [
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
