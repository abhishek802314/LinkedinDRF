import datetime
import pytz

from django.utils import timezone
from rest_framework import mixins,permissions, filters
from rest_framework.viewsets import GenericViewSet

from .serializers import OwnEventSerializer, EventSerializer
from .permissions import IsOwner, EventsPermissions
from .models import Event


class OwnEventsApiViewSet(GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin):
    queryset = Event.objects.all()
    serializer_class = OwnEventSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Event.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    

class EventApiViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [EventsPermissions]


    def get_queryset(self):
        for i in Event.objects.all():
            if i.schedule_post_date is not None and i.schedule_post_time is not None:
                date=datetime.datetime.combine(i.schedule_post_date,i.schedule_post_time)
                tmzone=pytz.timezone('Asia/Bishkek')
                dttime = tmzone.localize(date) 
                
                if (timezone.now() - dttime) > timezone.timedelta(minutes=1):
                    i.is_published=True
                    i.schedule_post_date=None
                    i.schedule_post_time=None
                    i.save()
        return Event.objects.filter(is_published=True)