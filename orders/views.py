from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Order
from .serializer import OrderSerializer
from carts.models import CartProduct
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from users.models import User
from products.models import Product
import ipdb


class OrderViewl(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderSerializer

    def post(self, request: Request):
        cart_id = self.request.user.cart.id
        products_cart = CartProduct.objects.all().filter(cart_id=cart_id)

        salesmans = set([product.product.owner for product in products_cart])

        products_for_salesman = {}
        for salesman in salesmans:
            products_for_salesman[salesman.username] = products_cart.filter(
                product__owner=salesman
            )

        total_price = 0
        for product in products_cart:
            total_price += product.product.price

        for order in products_for_salesman:
            salesman = get_object_or_404(User, username=order)
            price_total = 0
            for product in order:
                product_get = get_object_or_404(Product, id=product)
                price_total += product_get.price
                # ipdb.set_trace()
            Order.objects.create(
                total_order=price_total,
                user=self.request.user,
                salesman=salesman
            )

        return Response(status.HTTP_201_CREATED)
