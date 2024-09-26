from django.contrib import admin
from api.models import Product

class ProductAdmin(admin.ModelAdmin):
    # Campos que quieres mostrar en la lista de productos
    list_display = ('name', 'price', 'description', 'image')  
    
    # Campos por los que se puede buscar
    search_fields = ('name', 'description')  
    
    # Puedes agregar filtros por precio
    list_filter = ('price',)  
    
    # Opcional: puedes establecer el orden de los productos
    ordering = ('-price',)  # Ordenar por precio de mayor a menor

# Registramos el modelo junto con la clase personalizada
admin.site.register(Product, ProductAdmin)
