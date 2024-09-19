from django.contrib import admin
from .models import AboutUs, Statistics, CallToUs, Team, NewArrival

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'title_ru', 'title_en', 'image']
    
@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ['sellers_count', 'product_sale', 'customers', 'annual_gross']
    
@admin.register(CallToUs)
class CallToUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email']
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'twitter', 'instagram', 'linkedin']
    search_fields = ['name', 'position']

@admin.register(NewArrival)
class NewArrivalAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'title_ru', 'title_en', 'image']
    search_fields = ['title_uz', 'title_ru', 'title_en',]
