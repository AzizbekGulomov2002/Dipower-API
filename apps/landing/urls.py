from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutUsViewSet, StatisticsViewSet, CallToUsViewSet, TeamViewSet, NewArrivalViewSet

router = DefaultRouter()
router.register(r'about-us', AboutUsViewSet)
router.register(r'statistics', StatisticsViewSet)
router.register(r'call-to-us', CallToUsViewSet)
router.register(r'team', TeamViewSet)
router.register(r'new-arrivals', NewArrivalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
