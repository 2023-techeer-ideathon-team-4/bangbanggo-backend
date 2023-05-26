from django.urls import path
from .views import InputPostAPIView

urlpatterns = [
    path('/sight', InputPostAPIView.as_view(), name='input-post'),
]