from django.db import models
from app.views import Complaint_portal, Driver_registration, Collected_waste


# Create your models here.
class Complaint_portal(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    mob_no = models.CharField(max_length=12, blank=False)
    email = models.CharField(max_length=200, blank=False)
    subject = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    datetime = models.DateTimeField()
    image = models.ImageField(null=True, blank=False, upload_to='image')
    
    def __str__(self):
        return self.name
    

class Driver_registration(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    mob_no = models.CharField(max_length=12, blank=False)
    email = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200, blank=False)
    pin_code = models.CharField(max_length=12, blank=False)
    ward_no = models.CharField(max_length=12, blank=False)

    def __str__(self):
        return self.name


class Collected_waste(models.Model):
    dry_waste = models.IntegerField(blank=True)
    wet_waste = models.IntegerField(blank=True)
    plastic_waste = models.IntegerField(blank=True)
    medical_waste = models.IntegerField(blank=True)
    E_waste = models.IntegerField(blank=True)
    remarks = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    