from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, SKUViewSet, OrderViewSet, OrderHistoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'skus', SKUViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-histories', OrderHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
