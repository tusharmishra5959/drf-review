from rest_framework import permissions


class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Custom permissions for user to edit their own profile, otherwise get and post only
    """

    def has_permission(self, request, view):
        """
        This method is only called for two methods get and post.
        So it is true as we allow get and post methods for everyone.
        """

        return True

    def has_object_permission(self, request, view, obj):
        """
        Called when manipulating already present in database
        """

        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return request.user == obj
        return False


class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """."""

    def has_permission(self, request, view):
        """."""

        return True

    def has_object_permission(self, request, view, obj):
        """."""

        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return request.user.profile == obj
        return False
