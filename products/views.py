from .models import Product
from .serializer import ProductSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import SalesmanPermission, SalesmanUpdatedPermission
from products.filters import ProductFilter
from django_filters import rest_framework as filters
from products.mixins import ProductsMixin


class ProductView(ProductsMixin, generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [SalesmanPermission]

    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [SalesmanUpdatedPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "pk"
