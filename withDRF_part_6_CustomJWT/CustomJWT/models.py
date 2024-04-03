from django.db import models

# Create your models here.
class AJIO(models.Model):
    ProductName = models.CharField(max_length=255)
    Price = models.CharField(max_length=255)
    MRP = models.CharField(max_length=255)
    Discount = models.CharField(max_length=255)
    URL = models.CharField(max_length=255)
