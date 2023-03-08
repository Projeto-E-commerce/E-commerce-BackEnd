from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from carts.serializer import CartSerializer
from products.models import Product
from .models import Cart, CartProduct
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsUserPermission, ViewCartPermission
import ipdb


class CartCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserPermission]
    queryset = CartProduct.objects.all()
    serializer_class = CartSerializer

    ipdb.set_trace()
    def perform_create(self, serializer):
        product = self.kwargs.get("pk")
        get_product = get_object_or_404(Product, id=product)
        serializer.save(cart=self.request.user.cart, product=get_product)


class CartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ViewCartPermission]
    queryset = CartProduct.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        cart = CartProduct.objects.filter(cart=self.request.user.cart)
        return cart


class CartUpdateView(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [ViewCartPermission]
    queryset = CartProduct.objects.all()
    serializer_class = CartSerializer

    lookup_url_kwarg = "pk"
