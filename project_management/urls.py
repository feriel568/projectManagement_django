from django.contrib import admin
from django.urls import path, include
from utilisateurs import views as utilisateurs_views
urlpatterns = [
    path('admin/', admin.site.urls),



    path('utilisateurs/', include('utilisateurs.urls')), 

    path('projets/', include('projets.urls')),
    path('', utilisateurs_views.home, name='home'),
    path('', include('utilisateurs.urls')),  
]
