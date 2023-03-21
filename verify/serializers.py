from rest_framework.serializers import ModelSerializer
from .models import Aza
from django.contrib.auth.models import User


class AzaSerializer(ModelSerializer):
    class Meta:
        model = Aza
        fields = ['number', 'code']
