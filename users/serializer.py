from rest_framework import serializers
from .models import User
from addresses.models import Address
from addresses.serializer import AddressSerializer
from rest_framework.validators import UniqueValidator
import ipdb


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        address = validated_data.pop("address")
        Address.objects.update(**address)

        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(validated_data["password"])
            else:
                setattr(instance, key, value)
        instance.save()

        return instance

    address = AddressSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "type_user",
            "address",
            "cart",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [UniqueValidator(queryset=User.objects.all())]
                },
            "username": {
                "validators": [
                    UniqueValidator(
                        User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
            },
        }
