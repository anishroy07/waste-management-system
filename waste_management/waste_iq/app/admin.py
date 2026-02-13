from django.contrib import admin
from app.models import Complaint_portal, Driver_registration, Collected_waste

# Register your models here.
admin.site.register(Complaint_portal)

admin.site.register(Driver_registration)

admin.site.register(Collected_waste)