from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.models import Product
from .permissions import ViewFavoriteListPermission
from .models import FavoriteList
from .serializer import FavoriteListSerializer

# Create your views here.
class FavoriteListView(generics.CreateAPIView, generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ViewFavoriteListPermission]
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer
    
    def perform_create(self, serializer):
        # filter = self.queryset.all()
        product = self.kwargs.get("pk")
        # for item in filter:
        #    product_list = item.product.all()
        #    for p in product_list:
        #         import ipdb
        #         ipdb.set_trace()
               
        #    if item.product["id"] == product:
        #        raise TypeError("Item ja está nos favoritos")

        get_product = get_object_or_404(Product, pk=product)
        return serializer.save(product=get_product, user=self.request.user)



class FavoriteListGetView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ViewFavoriteListPermission]
    serializer_class = FavoriteListSerializer

    def get_queryset(self):
        return FavoriteList.objects.filter(user=self.request.user)
        
