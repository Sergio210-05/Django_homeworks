from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.id}: {self.name}, {self.description}'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(max_length=512, width_field=100, height_field=60, null=True)

    def __str__(self):
        return f'{self.sensor}: {self.temperature}, {self.created_at}'
