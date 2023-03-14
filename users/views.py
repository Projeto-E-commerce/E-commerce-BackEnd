from carts.models import Cart
from .models import User
from addresses.models import Address
from .serializer import UserSerializer
from rest_framework import generics
from .permissions import IsUserPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
import ipdb

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        cart = Cart.objects.create()
        return serializer.save(cart=cart)


class UserLoggedView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(
            id=self.request.user.id,
        )
        return queryset


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial,
        )
        serializer.is_valid(raise_exception=True)

        if "type_user" in self.request.data:
            if self.request.data["type_user"] == "admin":
                return Response(
                    {"message": "Permission"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
