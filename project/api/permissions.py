from rest_framework import permissions


class IsUserOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and view.kwargs["user_pk"] == str(request.user.id))
