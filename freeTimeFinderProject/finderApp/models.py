from django.db import models

# Create your models here.
class StartTimeRange(models.Model):
    range = models.CharField(max_length=255)

    def __str__(self):
        return self.range   

class EndTimeRange(models.Model):
    range = models.CharField(max_length=255)

    def __str__(self):
        return self.range  
