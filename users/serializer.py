from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.forms.models import model_to_dict

from addresses.serializer import AddressSerializer


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(validated_data["password"])
            else:
                setattr(instance, key, value)
        instance.save()

        return instance

    def to_representation(self, instance):
        user_address = [
            model_to_dict(address) for address in instance.address_user.all()
        ]
        address_obj = [
            address for address in user_address if address["current_address"]
        ]
        return {
            "user_id": instance.id,
            "username": instance.username,
            "email": instance.email,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "type_user": instance.type_user,
            "address_user": address_obj[0] if len(address_obj) > 0 else None,
        }

    address_user = AddressSerializer(many=True, required=False)

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
            "cart",
            "favorite_list",
            "address_user",
        ]
        extra_kwargs = {
            "favorite_list": {"read_only": True},
            "password": {"write_only": True},
            "cart": {"write_only": True},
            "email": {
                "validators": [UniqueValidator(queryset=User.objects.all())],
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
