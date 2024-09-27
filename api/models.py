import cloudinary.uploader
from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/', storage=CloudinaryStorage())

    def save(self, *args, **kwargs):
        if self.image:  # Solo si hay una imagen
            # Crear un public_id personalizado
            public_id = f"mi_prefijo_{slugify(self.name)}"
            # Subir la imagen manualmente a Cloudinary con el public_id
            upload_data = cloudinary.uploader.upload(self.image, public_id=public_id)
            # Guardar la URL completa de la imagen subida en el campo image
            self.image = upload_data['secure_url']  # Almacenar la URL segura completa
        
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
