from django.urls import path
from .views import InformationPostAPIView

urlpatterns = [
    path('api/information/', InformationPostAPIView.as_view()),
]