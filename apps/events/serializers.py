from rest_framework import serializers
from .models import Event


class OwnEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('owner', )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'image',
            'event_type',
            'description',
            'timezone',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'speakers',
            'link_to_event',
            'address'
        )
        read_only_fields = ('owner', )