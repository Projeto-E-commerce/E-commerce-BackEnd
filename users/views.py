from .models import User
from addresses.models import Address
from .serializer import UserSerializer
from rest_framework import generics
from .permissions import IsUserPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import ipdb


# Create your views here.
class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        address = self.request.data.pop("address")
        address_obj = Address.objects.create(**address)
        return serializer.save(address=address_obj)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
