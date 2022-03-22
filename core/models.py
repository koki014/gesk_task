from django.db import models

# Create your models here.


class Payload(models.Model):
    device_serial = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    error = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.device_serial
    
    class Meta:
        verbose_name_plural = "Payloads"
        verbose_name = "Payload"
        ordering = ['-timestamp']
