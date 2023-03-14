from rest_framework import serializers
from products.models import Product 
from products.serializer import ProductForUserSerializer
from .models import FavoriteList

class FavoriteListSerializer(serializers.ModelSerializer):

    product = ProductForUserSerializer(many=True, required=False)

    def create(self, validated_data):
        user = validated_data["user"]
        product = validated_data["product"]
        favorite = FavoriteList.objects.create(user=user)
        favorite.product.add(product)
        user.favorite_list.add(favorite)
        return favorite

    class Meta:
        model = FavoriteList
        exclude = ["user"]
        read_only_fields = [
            "product",
        ]
