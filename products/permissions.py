from rest_framework import permissions
from rest_framework.views import View


class SalesmanPermission(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.type_user == "salesman"
        )
