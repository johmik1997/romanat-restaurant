from rest_framework import permissions
from .models import RolePermission

class RoleBasedPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # Must be authenticated
        if not request.user or not request.user.is_authenticated:
            return False

        # Superuser always allowed
        if request.user.is_superuser:
            return True

        required_perm = getattr(view, "required_permission", None)

        # No permission required for this view
        if required_perm is None:
            return True

        user_role = request.user.role
        if not user_role:
            return False

        return RolePermission.objects.filter(
            role=user_role,
            permission__name=required_perm
        ).exists()
