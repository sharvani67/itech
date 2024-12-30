from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from . import views
# from .views import SoftwareViewSet

# Router for API routes
# router = DefaultRouter()
# router.register(r'api/software', SoftwareViewSet, basename='software')

urlpatterns = [
    # Web-based routes
    path('home/', views.home, name='home'),  # Home page
    path('contact/', views.contact, name='contact'),
    path('upload-software/', views.upload_software, name='upload_software'),
    path('software-list/', views.software_list, name='software_list'),
    path('update/<int:id>/', views.update_software, name='update_software'),
    path('delete/<int:id>/', views.delete_software, name='delete_software'),


        path('softwares',views.getsoftware.as_view(),name='softwares-all'),
        # path('softwares/id/<int:id>',getstudentById.as_view(),name='softwares-by-id'),
        path('softwares/create',views.createsoftware.as_view(),name='softwares-create'),
        path('softwares/update/id/<int:id>',views.updatesoftware.as_view(),name='softwares-update'),
        path('softwares/update/<int:id>',views.updatesoftware.as_view(),name='softwares-update'),
        path('softwares/delete/id/<int:id>',views.deletesoftware.as_view(),name='softwares-delete'),

    # API routes
    # path('', include(router.urls)), 
]

# Media URL Configuration
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
