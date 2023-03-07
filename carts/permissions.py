from rest_framework import permissions
from .models import CartProduct
from rest_framework.views import Request, View
from rest_framework.views import View


class IsUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: CartProduct) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_superuser
            or obj == request.user
        )

class ViewCartPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: CartProduct):
        return (
            request.user.is_authenticated
            and obj == request.user
        )