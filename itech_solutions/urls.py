from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from . import views
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# from .views import SoftwareViewSet

# Router for API routes
# router = DefaultRouter()
# router.register(r'api/software', SoftwareViewSet, basename='software')

urlpatterns = [
    # Web-based routes
    path('home/', login_required(views.home), name='home'),  # Home page
    path('contact/', login_required(views.contact), name='contact'),
    path('upload-software/', login_required(views.upload_software), name='upload_software'),
    path('software-list/', login_required(views.software_list), name='software_list'),
    path('update/<int:id>/', login_required(views.update_software), name='update_software'),
    path('delete/<int:id>/', login_required(views.delete_software), name='delete_software'),


        path('softwares',views.getsoftware.as_view(),name='softwares-all'),
        # path('softwares/id/<int:id>',getstudentById.as_view(),name='softwares-by-id'),
        path('softwares/create',views.createsoftware.as_view(),name='softwares-create'),
        path('softwares/update/id/<int:id>',views.updatesoftware.as_view(),name='softwares-update'),
        path('softwares/update/<int:id>',views.updatesoftware.as_view(),name='softwares-update'),
        path('softwares/delete/id/<int:id>',views.deletesoftware.as_view(),name='softwares-delete'),


         path('', lambda request: redirect('login/')), 
         path('register/', views.register_view, name='register'),
            path('login/', views.login_view, name='login'),
            path('logout/', views.logout_view, name='logout'),

    # API routes
    # path('', include(router.urls)), 
]

# Media URL Configuration
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
