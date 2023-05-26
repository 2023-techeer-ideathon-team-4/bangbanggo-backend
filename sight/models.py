from django.db import models

class Place(models.Model):
    place = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Input(models.Model):
    address = models.CharField(max_length=50)
    kilo = models.IntegerField()
    count = models.IntegerField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
