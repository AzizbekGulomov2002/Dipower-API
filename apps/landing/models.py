import uuid
from django.db import models

# Create your models here.

class AboutUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_en or "About Us"

class Statistics(models.Model):
    sellers_count = models.PositiveBigIntegerField()
    product_sale = models.PositiveBigIntegerField()
    customers = models.PositiveBigIntegerField()
    annual_gross = models.PositiveBigIntegerField()
    def __str__(self):
        return "Statistics"

class CallToUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=23)
    message = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name


    
class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.name

class NewArrival(models.Model):
    title = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name