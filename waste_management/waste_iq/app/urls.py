from django.contrib import admin
from django.urls import path, include
from app import views
from .views import authView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Admin Login', admin.site.urls),
    path('', views.index, name='home'),
    path('about us', views.about_us, name='about us'),
    path('Dashboard', views.dashboard, name='Dashboard'),
    path('Complaint portal', views.Complaint_portal, name='Complaint portal'),
    path('Recycling guide', views.recycling_guide, name='Recycling guide'),
    path('Collected waste', views.Collected_waste, name='Collected waste'),
    path('signup/', authView, name='authView'),
    path('User Login', include('django.contrib.auth.urls')),
    path('Driver registration', views.Driver_registration, name='Driver registration')
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "WasteIQ Admin"
admin.site.site_title = "WasteIQ"
admin.site.index_title = "Welcome to WasteIQ Admin"
