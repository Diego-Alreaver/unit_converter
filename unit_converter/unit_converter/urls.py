
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('converter/', include('converter.urls')),  # Incluimos las rutas de la app
]
