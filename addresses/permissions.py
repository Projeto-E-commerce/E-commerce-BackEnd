from rest_framework import permissions
from rest_framework.views import View
from rest_framework.views import View


class IsAddressPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_superuser
            or obj.user == request.user
        )
