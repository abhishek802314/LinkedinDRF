from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Event(models.Model):

    EVENTTYPE=(
        ('Online','Online'),
        ('Offline','Offline')
    )

    owner=models.ForeignKey(User, on_delete=models.CASCADE,related_name='events_owner')
    image=models.ImageField(upload_to='events/')
    event_type=models.CharField(max_length=30,choices=EVENTTYPE)
    description=models.TextField()
    timezone=models.CharField(max_length=255)
    start_date=models.DateField()
    start_time=models.TimeField()
    end_date=models.DateField()
    end_time=models.TimeField()
    speakers=models.ManyToManyField(User)
    link_to_event=models.CharField(max_length=1000,null=True,blank=True)
    address=models.CharField(max_length=255,null=True,blank=True)
    is_published=models.BooleanField(default=True)

    only_contacts=models.BooleanField(default=False)
    is_publicly_available=models.BooleanField(default=True)
    is_nobody=models.BooleanField(default=False)

    # Schedule a post ///Запланировать публикацию
    schedule_post_date=models.DateField(null=True,blank=True)
    schedule_post_time=models.TimeField(null=True,blank=True)

    def __str__(self):
        return f'{self.owner}-event type:{self.event_type} '('id','from_user','to_user','create_at',)