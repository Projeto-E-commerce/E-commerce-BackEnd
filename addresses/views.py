from .models import Address
from .serializer import AddressSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
import ipdb


class AddressView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Address.objects.filter(
            user=self.request.user,
            # current_address=True,
        )
        return queryset


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
