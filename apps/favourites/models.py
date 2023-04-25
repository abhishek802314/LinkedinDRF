from django.db import models
from django.contrib.auth.models import User
from apps.post.models import Post


class FavouriteFolder(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='favourite_folder_user', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title} {self.user.username}'
    

class Favourite(models.Model):
    folder = models.ForeignKey(FavouriteFolder, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.post.title}'
    
    class Meta:
        unique_together = (('post', 'user', ), )
    