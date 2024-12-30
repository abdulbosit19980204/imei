from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class IsJtonOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.__dict__)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.jton == request.user.jton
