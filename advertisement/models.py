from django.db import models

# Create your models here.
class Advertisement(models.Model):
    image = models.ImageField(upload_to='ad/%Y/%m/%d/')
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    days_open = models.CharField(max_length=50)  # Store days as a comma-separated list
    google_maps_link = models.URLField()

    def __str__(self):
        return self.title