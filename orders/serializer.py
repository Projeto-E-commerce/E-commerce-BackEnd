from rest_framework import serializers
from .models import Order
from django.core.mail import send_mail
from django.conf import settings


class OrderSerializer(serializers.ModelSerializer):
    products_list = serializers.JSONField()

    def create(self, validated_data: dict):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data: dict):
        if instance.status is not validated_data["status"]:
            send_mail(
                subject="order status",
                message=f'order status has been updated to {validated_data["status"]}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[instance.user.email],
                fail_silently=False,
            )
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
