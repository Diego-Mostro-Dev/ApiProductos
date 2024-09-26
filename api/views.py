from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def perform_create(self, serializer):
    product = serializer.save()
    print(f'Imagen original: {product.image}')  # Verifica el valor original de la imagen
    if product.image:
        product.image = f'https://res.cloudinary.com/tu_cloud_name/{product.image}'
        product.save()
        print(f'Imagen modificada: {product.image}')  # Verifica el valor modificado de la imagen


            