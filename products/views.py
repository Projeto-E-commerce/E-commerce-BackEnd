from .models import Product
from .serializer import ProductSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import SalesmanPermission
import ipdb


# Create your views here.
class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [SalesmanPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
