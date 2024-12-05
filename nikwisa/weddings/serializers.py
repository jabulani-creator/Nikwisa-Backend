# weddings/serializers.py
from rest_framework import serializers
from .models import Wedding

class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = '__all__'  # Adjust fields if necessary

