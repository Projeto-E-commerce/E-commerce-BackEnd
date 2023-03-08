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

    def post(self, request):
        cart_id = self.request.user.cart.id
        products_cart = CartProduct.objects.all().filter(cart_id=cart_id)

        salesmans = set([product.product.owner for product in products_cart])

        order_return = {}
        for salesman in salesmans:
            products_for_salesman = products_cart.filter(product__owner=salesman)

            price_total = 0
            products_list = []
            for product in products_for_salesman:
                product_get = get_object_or_404(Product, id=product.product.id)
                price_total += product_get.price * product.product_count
                products_list.append(
                    {
                        "id": product_get.id,
                        "name": product_get.name,
                        "category": product_get.category,
                        "description": product_get.description,
                        "price": str(product_get.price * product.product_count),
                        "count": product.product_count,
                    }
                )

            Order.objects.create(
                total_order=price_total,
                user=self.request.user,
                salesman=salesman,
                products_list=products_list,
            )

            order_return[salesman.username] = products_list

        return Response(order_return, status.HTTP_201_CREATED)
