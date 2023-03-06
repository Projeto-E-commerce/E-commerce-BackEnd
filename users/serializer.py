from rest_framework import serializers
from .models import User
from addresses.serializer import AddressSerializer
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

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
        read_only_fields = ["type_user"]
