
# URLS
from django.urls import path
from . import views

urlpatterns = [
    path('', views.software_list, name='software_list'),
    path('add/', views.add_software, name='add_software'),
    path('delete/<int:id>/', views.delete_software, name='delete_software'),
    path('update/<int:id>/', views.update_software, name='update_software'),
]

# Media URL Configuration
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)