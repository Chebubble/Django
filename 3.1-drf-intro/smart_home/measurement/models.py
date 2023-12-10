from django import utils
from django.db import models
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=10, blank=True)
    def __str__(self) -> str:
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Измерение #{self.id} на датчике {self.sensor}'

<<<<<<< HEAD
=======

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.name
    
    
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Измерение №{self.id} на датчике {self.sensor}'
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
