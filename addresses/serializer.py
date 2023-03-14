from rest_framework import serializers
from .models import Address

# from users.serializer import UserSerializer
import ipdb


class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Address:
        return Address.objects.create(**validated_data)

    def update(self, instance: Address, validated_data: dict) -> Address:
        addresses = Address.objects.filter(user=self.instance.user)
        for address in addresses:
            address.current_address = False
            address.save()
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance

    # user = UserSerializer()

    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "zip_code",
            "city",
            "state",
            "country",
            "aditional_info",
            "current_address",
            "user",
        ]
        read_only_fields = [
            "user",
            "id",
        ]
        required = {"user": False}
