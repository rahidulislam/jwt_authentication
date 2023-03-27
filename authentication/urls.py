from django.urls import path
from .views import HomeAPIView, LogoutAPIView

app_name = "authentication"

urlpatterns = [
    path('', HomeAPIView.as_view(), name='home'),
    path('logout/', LogoutAPIView.as_view(), name='logout')
]
