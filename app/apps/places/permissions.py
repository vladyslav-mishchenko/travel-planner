from rest_framework import permissions


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    - Read-only for everyone (GET, HEAD, OPTIONS)
    - Create, update, delete only for superusers
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser
