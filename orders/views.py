from rest_framework.views import Response, status
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Order
from .serializer import OrderSerializer
from carts.models import CartProduct
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from products.models import Product
from .permission import IsSalesmanPermission
from .exceptions import StorageError


class OrderViewl(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderSerializer

    def post(self, request):
        cart_id = self.request.user.cart.id
        products_cart = CartProduct.objects.all().filter(
            cart_id=cart_id,
            active=True,
        )

        salesmans = set([product.product.owner for product in products_cart])

        order_return = {}
        for salesman in salesmans:
            products_for_salesman = products_cart.filter(
                product__owner=salesman,
            )

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
                try:
                    if product.product_count > product_get.storage:
                        raise StorageError("This amount is not available.")
                    product_get.storage -= product.product_count
                    product_get.save()
                except StorageError as e:
                    return Response(
                        {"Error": e.message},
                        status.HTTP_400_BAD_REQUEST,
                    )

                product.active = False
                product.save()

            Order.objects.create(
                total_order=price_total,
                user=self.request.user,
                salesman=salesman,
                products_list=products_list,
            )

            order_return[salesman.username] = products_list

        return Response(order_return, status.HTTP_201_CREATED)


class OrderListClientView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user).order_by("-ordered_at")
        return queryset


class OrderListSalesmanView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.filter(salesman=self.request.user).order_by("-ordered_at")
        return queryset


class OrderEditView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSalesmanPermission]
    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderSerializer
