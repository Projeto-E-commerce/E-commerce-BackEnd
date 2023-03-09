from django.shortcuts import get_object_or_404
from rest_framework.views import Response, status
from rest_framework import generics
from carts.exceptions import OperationError
from carts.serializer import CartProductSerializer
from products.models import Product
from .models import CartProduct
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsUserPermission, ViewCartPermission
import ipdb

class CartCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserPermission]
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        product = self.kwargs.get("pk")
        
        get_product = get_object_or_404(
            Product,
            id=product,
        )
        serializer.save(
            cart=self.request.user.cart,
            product=get_product,
        )
        
    #     # try:            
    #     #     cart_product = CartProduct.objects.filter(
    #     #         cart=self.request.user.cart,
    #     #         product=product
    #     #     ).first()

    #     #     if cart_product.product is not None:
    #     #         raise OperationError("Product Already exist")
    #     # except OperationError as e:
    #     #     return Response(
    #     #         {"Error": e.message},
    #     #         status.HTTP_400_BAD_REQUEST,
    #     #     )


class CartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ViewCartPermission]
    queryset = CartProduct.objects.all().order_by("id")
    serializer_class = CartProductSerializer

    def get_queryset(self):
        cart = CartProduct.objects.filter(
            cart=self.request.user.cart,
            active=True,
        )
        return cart


class CartUpdateView(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    lookup_url_kwarg = "pk"
