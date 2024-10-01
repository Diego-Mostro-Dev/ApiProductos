from django.db import models
from django.utils.text import slugify
import cloudinary.uploader

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image_file = models.ImageField(upload_to='uploads/', null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def save(self, *args, **kwargs):
        if self.image_file:
            public_id = f"mi_prefijo_{slugify(self.name)}"
            upload_data = cloudinary.uploader.upload(self.image_file, public_id=public_id)
            self.image_url = upload_data['secure_url']  # Asegúrate de usar 'secure_url' directamente.
            self.image_file = None  # Limpia el campo después de subir
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
