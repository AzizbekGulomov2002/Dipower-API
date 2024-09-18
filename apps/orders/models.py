from django.db import models
import uuid
from django.forms import ValidationError
from apps.users.models import User

class TranslatableModel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Category(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Product(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    show_main_page = models.BooleanField()

    def __str__(self):
        return self.name

class SKU(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class TypeChoice(models.TextChoices):
        SIZE = 'size', 'Size'
        COLOR = 'color', 'Color'

    product = models.ForeignKey(Product, related_name='skus', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    type_sku = models.CharField(max_length=255, choices=TypeChoice.choices, default=TypeChoice.COLOR, null=True,
                                blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(null=True, blank=True)

    def __str__(self):
        return f"SKU {self.type_sku} + {self.value} for {self.product.name}"

class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"
    
    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

# Create your models here.
class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        DELIVERED = 'delivered', 'Delivered'
        CANCELED = 'canceled', 'Canceled'
        SUCCESS = 'success', 'Success'

    class TypeOrder(models.TextChoices):
        CASH = 'cash', 'Cash'
        STRIPE = 'stripe', 'Stripe'

    class PaymentStatus(models.TextChoices):
        FAILED = 'failed', 'Failed'
        CANCELED = 'canceled', 'Canceled'
        SUCCEEDED = 'succeeded', 'Succeeded'
        EXPIRED = 'expired', 'Expired'
        PENDING = 'pending', 'Pending'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    type_order = models.CharField(max_length=20, choices=TypeOrder.choices, default=TypeOrder.STRIPE)
    order_status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Orders'

    @property
    def total_quantity(self):
        return sum(item.quantity for item in self.products.all())
    
    @property
    def total_sum(self):
        return sum(item.price * item.quantity for item in self.skus.all())

    def save(self, *args, **kwargs):
        latest_order = Order.objects.last()
        if latest_order and latest_order.total_sum >= self.free_delivery:
            self.free_delivery = self.delivery_price + self.free_delivery
        else:
            self.free_delivery = 0
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()

    def clean(self):
        if self.sku.quantity is None:
            raise ValidationError(f"SKU {self.sku.value} has no available quantity.")
        
        if int(self.sku.quantity) < int(self.quantity):
            raise ValidationError(
                f"Insufficient quantity for SKU {self.sku.value}. Available: {self.sku.quantity}, Requested: {self.quantity}")

    def restore_product_quantity(self):
        if self.order.type_order == 'cash':
            self.sku.quantity += self.quantity
            self.sku.save()

    def __str__(self):
        return f"{self.quantity} of SKU {self.sku.value}"

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Order Items'

class OrderHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, related_name='order_histories', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='order_histories', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Order Histories'
        ordering = ['-date']