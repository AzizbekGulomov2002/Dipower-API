from django.contrib import admin
from apps.orders.models import Category, Product, SKU, ProductImages, Order, OrderItem, OrderHistory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_en','name_ru', 'image')
    search_fields = ('name_uz','name_en','name_ru',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_en','name_ru', 'category', 'show_main_page')
    search_fields = ('name_uz','name_en','name_ru')
    list_filter = ('category', 'show_main_page')

@admin.register(SKU)
class SKUAdmin(admin.ModelAdmin):
    list_display = ('product', 'type_sku', 'value', 'price', 'quantity')
    search_fields = ('product__name', 'type_sku', 'value')

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','order_status','created_at')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'sku', 'quantity')
    search_fields = ('order__user__username', 'sku__value')

@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'status', 'date')
    search_fields = ('order__user__username', 'status')
    list_filter = ('status',)
