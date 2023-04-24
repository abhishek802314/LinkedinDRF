from rest_framework import permissions


class IsSender(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.sender == request.user)
    

class IsReceiver(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.receiver == request.user)