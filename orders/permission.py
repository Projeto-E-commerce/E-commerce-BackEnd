from rest_framework import permissions
from rest_framework.views import View


class IsSalesmanPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj) -> bool:
        return request.user.is_authenticated and obj.salesman == request.user
