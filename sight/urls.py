from django.urls import path
from .views import InputPostAPIView

urlpatterns = [
    path('api/v1/input/', InputPostAPIView.as_view(), name='input-post'),
]