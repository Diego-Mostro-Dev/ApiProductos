from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r"products", views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Esto maneja todas las rutas de los productos
    path('docs/', include_docs_urls(title="API Documentation"))  # Ruta para la documentación
]
