
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Cambiado a ImageField

    def __str__(self):
        return self.name
