from rest_framework import generics
from .models import Coupon
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import CouponSerializer
from products.permissions import SalesmanPermission, SalesmanUpdatedPermission


class CuoponViewl(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [SalesmanPermission]
    queryset = Coupon.objects.all().order_by("id")
    serializer_class = CouponSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CouponDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [SalesmanUpdatedPermission]
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
