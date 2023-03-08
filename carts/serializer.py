from rest_framework import serializers
from .models import CartProduct
from rest_framework.validators import UniqueValidator
from products.serializer import ProductSerializer
import ipdb


class CartProductSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    total_price = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> CartProduct:
        return CartProduct.objects.create(**validated_data)
    
    def get_total_price(self, instance):
        instance.total_price = instance.product.price * instance.product_count
        instance.save()
        return instance.total_price

    def update(self, instance: CartProduct, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = CartProduct
        fields = "__all__"
        read_only_fields = ["cart", "product", "total_price"]
