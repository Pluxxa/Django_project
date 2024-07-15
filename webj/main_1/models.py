# main_1/models.py

from django.db import models

class Message(models.Model):
    text = models.TextField()
    x_position = models.FloatField()
    y_position = models.FloatField()
