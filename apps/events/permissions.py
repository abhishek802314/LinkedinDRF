from rest_framework import permissions
from apps.subscriptions.models import Follower


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.owner == request.user)
    

class EventsPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        elif obj.is_publicly_available==True:
            return True
        elif obj.only_contacts==True:
            followers=Follower.objects.filter(to_user=obj.owner)
            if request.user.id in [i.from_user.id for i in followers]:
                return True
            return False
        elif obj.is_nobody==False:
            return True
        return False


        