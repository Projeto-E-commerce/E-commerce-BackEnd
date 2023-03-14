from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
from favorits.mixins import FavoriteListMixin
from products.models import Product
from .permissions import ViewFavoriteListPermission
from .models import FavoriteList
from .serializer import FavoriteListSerializer

# Create your views here.
class FavoriteListView(FavoriteListMixin ,generics.CreateAPIView, generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ViewFavoriteListPermission]
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer


class FavoriteListGetView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ViewFavoriteListPermission]
    serializer_class = FavoriteListSerializer

    def get_queryset(self):
        return FavoriteList.objects.filter(user=self.request.user)
        
