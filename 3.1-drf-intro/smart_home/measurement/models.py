from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class Measurement(models.Model):

    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', null=True)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
