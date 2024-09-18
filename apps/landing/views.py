from rest_framework import viewsets
from .models import AboutUs, Statistics, CallToUs, Team, NewArrival
from .serializers import AboutUsSerializer, StatisticsSerializer, CallToUsSerializer, TeamSerializer, NewArrivalSerializer

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class CallToUsViewSet(viewsets.ModelViewSet):
    queryset = CallToUs.objects.all()
    serializer_class = CallToUsSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class NewArrivalViewSet(viewsets.ModelViewSet):
    queryset = NewArrival.objects.all()
    serializer_class = NewArrivalSerializer
