
from django.shortcuts import get_object_or_404
from favorits.exceptions import ProductAlreadyFavorited
from favorits.models import FavoriteList
from products.models import Product
from rest_framework.views import Response, status

class FavoriteListMixin():
    def create(self, request, *args, **kwargs):
        product = kwargs.get("pk")
        get_product = get_object_or_404(Product, pk=product)
        filter = FavoriteList.objects.filter(
            user=self.request.user,
            product=get_product,
        ).exists()
        try:
            if filter:
                raise ProductAlreadyFavorited(
                        "You have already Favorited this product."
                    )
        except ProductAlreadyFavorited as e:
            return Response(
                    {"Error": e.message},
                    status.HTTP_400_BAD_REQUEST,
                )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        product = self.kwargs.get("pk")
        get_product = get_object_or_404(Product, pk=product)
        return serializer.save(product=get_product, user=self.request.user)
    
