from django.contrib import admin
from apps.orders.models import Category, Product, SKU, ProductImages, Order, OrderItem, OrderHistory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'show_main_page')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'show_main_page')

@admin.register(SKU)
class SKUAdmin(admin.ModelAdmin):
    list_display = ('product', 'type_sku', 'value', 'price', 'quantity')
    search_fields = ('product__name', 'type_sku', 'value')

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ('product__name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'type_order', 'order_status', 'payment_status', 'created_at')
    search_fields = ('user__username', 'type_order')
    list_filter = ('order_status', 'payment_status')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'sku', 'quantity')
    search_fields = ('order__user__username', 'sku__value')

@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'status', 'date')
    search_fields = ('order__user__username', 'status')
    list_filter = ('status',)
