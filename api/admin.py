from django.contrib import admin
from api.models import Product

class ProductAdmin(admin.ModelAdmin):
    # Campos que quieres mostrar en la lista de productos
    list_display = ('id', 'name', 'price', 'image_url') 
    
    # Campos por los que se puede buscar
    search_fields = ('name', 'description')  
    
    # Puedes agregar filtros por precio
    list_filter = ('price',)  
    
    # Opcional: puedes establecer el orden de los productos
    ordering = ('-price',)  # Ordenar por precio de mayor a menor

    # Personalizar los nombres de los encabezados
    def get_list_display(self, request):
        return (
            'id', 
            'get_name_display',  # Cambiamos 'name' por 'get_name_display'
            'get_price_display',  # Cambiamos 'price' por 'get_price_display'
            'get_image_url_display',  # Cambiamos 'image_url' por 'get_image_url_display'
        )

    # Métodos para obtener los nombres en español
    def get_name_display(self, obj):
        return obj.name
    get_name_display.short_description = 'Nombre'  # Título que se mostrará en el encabezado

    def get_price_display(self, obj):
        return obj.price
    get_price_display.short_description = 'Precio'  # Título que se mostrará en el encabezado

    def get_image_url_display(self, obj):
        return obj.image_url
    get_image_url_display.short_description = 'URL de la Imagen'  # Título que se mostrará en el encabezado

# Registramos el modelo junto con la clase personalizada
admin.site.register(Product, ProductAdmin)
