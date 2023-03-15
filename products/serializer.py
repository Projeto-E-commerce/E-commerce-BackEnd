from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data: dict) -> Product:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    owner = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "storage",
            "price",
            "description",
            "owner",
            "product_URL"
        ]
        read_only_fields = ["owner"]
        required = {"product": False}


class ProductForUserSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "price",
            "description",
            "owner",
        ]
        read_only_fields = ["owner"]
        required = {"product": False}
