from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class IsOwnerOnly(BasePermission):
    """
    Only the owner of the object can access it (read or write).
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
