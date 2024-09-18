from rest_framework import serializers
from .models import AboutUs, Statistics, CallToUs, Team, NewArrival

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'

class CallToUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallToUs
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class NewArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewArrival
        fields = '__all__'
