from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Address:
        return Address.objects.create(**validated_data)

    class Meta:
        model = Address
        fields = "__all__"
