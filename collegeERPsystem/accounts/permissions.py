from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"

class IsSelfOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == "admin" or obj.id == request.user.id
