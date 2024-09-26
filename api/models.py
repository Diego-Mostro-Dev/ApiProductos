
from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = CloudinaryField('image', null=True, blank=True ,resource_type='image')  # Usar Cloudinary para imágenes

    def __str__(self):
        return self.name
