
# URLS
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('upload-software/', views.upload_software, name='upload_software'),
    path('software-list/', views.software_list, name='software_list'),
    path('update/<int:id>/', views.update_software, name='update_software'),
    path('delete/<int:id>/', views.delete_software, name='delete_software'),
]

# Media URL Configuration
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)