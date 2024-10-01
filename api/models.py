from django.db import models
from django.utils.text import slugify
import cloudinary.uploader

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # Cambiado a ImageField

    def save(self, *args, **kwargs):
        if self.image:  # Si hay una imagen cargada
            public_id = f"mi_prefijo_{slugify(self.name)}"
            upload_data = cloudinary.uploader.upload(self.image, public_id=public_id)  # Subir la imagen a Cloudinary
            self.image = upload_data['secure_url']  # Almacenar la URL segura completa en el campo de imagen
        
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
