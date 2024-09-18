from rest_framework import serializers
from .models import Category, Product, SKU, ProductImages, Order, OrderItem, OrderHistory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image']

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImagesSerializer(many=True, read_only=True)
    skus = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'show_main_page', 'product_images', 'skus']

    def get_skus(self, obj):
        request = self.context.get('request')
        # Include SKU information only for GET requests
        if request and request.method == 'GET':
            skus = SKU.objects.filter(product=obj)
            return SKUSerializer(skus, many=True).data
        return []


class SKUSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = SKU
        fields = ['id', 'product', 'type_sku', 'value', 'price', 'quantity']

class OrderItemSerializer(serializers.ModelSerializer):
    sku = SKUSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'sku', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'type_order', 'order_status', 'payment_status', 'address', 'latitude', 'longitude',
                  'comment', 'created_at', 'order_items']

class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = ['id', 'order', 'user', 'status', 'date']
