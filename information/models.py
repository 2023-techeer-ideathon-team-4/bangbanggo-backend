from django.db import models

class information(models.Model):
    information_id = models.IntegerField(),
    address = models.CharField(max_length=1000),
    km = models.FloatField,
    num_places = models.models.IntegerField(max_length=5),
    created_at = models.DateTimeField(),
    updated_at = models.DateTimeField(),
