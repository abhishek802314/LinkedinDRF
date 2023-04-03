from rest_framework import permissions

class IsOwn(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user)
    
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
         return bool(obj == request.user)
    