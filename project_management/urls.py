from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('utilisateurs/', include('utilisateurs.urls')),  
    path('', include('utilisateurs.urls')),  
    path('projets/', include('projets.urls')),
]
