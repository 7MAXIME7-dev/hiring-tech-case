from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Plot

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class PlotSerializer(serializers.ModelSerializer):
    area = serializers.SerializerMethodField()
    class Meta:
        model = Plot
        fields = ('id', 'user_id', 'name', 'geometry', 'area')

    def get_area(self, obj):
        if obj.geometry:
            return obj.geometry.area
        return None