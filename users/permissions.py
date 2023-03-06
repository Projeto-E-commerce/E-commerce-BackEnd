from rest_framework import permissions
from .models import User
from rest_framework.views import Request, View
from rest_framework.views import View


class IsUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_superuser
            or obj == request.user
        )


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )
