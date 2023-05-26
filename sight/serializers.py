from rest_framework import serializers
from .models import Input, Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class InputSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Input
        fields = ['addr', 'kilo', 'place']

