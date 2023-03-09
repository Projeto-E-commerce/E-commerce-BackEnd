from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    products_list = serializers.JSONField()

    def create(self, validated_data: dict):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "ordered_at",
            "user",
            "total_order",
            "salesman",
            "products_list",
        ]
        read_only_fields = [
            "ordered_at",
            "user",
            "total_order",
            "salesman",
            "products_list",
        ]
