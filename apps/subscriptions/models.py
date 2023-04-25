from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.create_at
    
    class Meta:
        ordering = ('create_at', )
        unique_together = (('from_user', 'to_user', ), )
    
