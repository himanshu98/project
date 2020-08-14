from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=122)
    qty=models.IntegerField(default=0)
    url=models.CharField(max_length=122)
    time=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    
