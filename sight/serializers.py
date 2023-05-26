from rest_framework import serializers
from .models import Input, Place
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['place']

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ['address', 'kilo', 'count']

