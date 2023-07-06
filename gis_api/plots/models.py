from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Plot(models.Model):
    name = models.CharField(max_length=100)
    geometry = models.GeometryField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)