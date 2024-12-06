from rest_framework import serializers
from .models import DeliveryOrder

class DeliveryOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryOrder
        fields = ['id', 'customer_name', 'address', 'item', 'status']

class DeliveryOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryOrder
        fields = ['status']
