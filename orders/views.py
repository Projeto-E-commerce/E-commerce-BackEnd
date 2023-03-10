from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from orders.mixins import OrderMixin
from .models import Order
from .serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import IsSalesmanPermission


class OrderViewl(OrderMixin, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderSerializer


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
