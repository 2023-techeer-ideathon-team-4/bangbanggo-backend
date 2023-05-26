from rest_framework import serializers

class InformationSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=1000)
    km = serializers.FloatField()
    num_places = serializers.IntegerField(max_value=5)
