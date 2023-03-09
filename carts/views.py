from rest_framework.views import Response, status
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

    def post(self, request, *args, **kwargs):
        product_id = kwargs["pk"]
        cart_product = CartProduct.objects.filter(
            cart=self.request.user.cart,
            product__id=product_id,
            active=True,
        ).first()
        if cart_product is not None:
            cart_product.product_count += int(self.request.data["product_count"])
            cart_product.save()
            serializer = CartProductSerializer(cart_product)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            get_product = get_object_or_404(
                Product,
                id=product_id,
            )
            cart_order = CartProduct.objects.create(
                cart=self.request.user.cart,
                product=get_product,
                product_count=int(self.request.data["product_count"]),
            )
            serializer = CartProductSerializer(cart_order)
            return Response(
                serializer.data,
                status.HTTP_201_CREATED,
            )


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
