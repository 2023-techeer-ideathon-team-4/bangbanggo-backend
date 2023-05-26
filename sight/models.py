from django.db import models

class Input(models.Model):
    address = models.CharField(max_length=50)
    kilo = models.IntegerField()
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Place(models.Model):
    place = models.CharField(max_length=50)
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
