from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User=get_user_model()

class PostTag(models.Model):
    title=models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='users_tag', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='user_posts', on_delete=models.CASCADE)
    tags=models.ManyToManyField(PostTag,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}---{self.user}"

    class Meta:
        ordering = ('create_at',)



class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_image/')

    def __str__(self):
        return f"{self.post.title}---{self.post.user}"   


class PostVideo(models.Model):
    post = models.ForeignKey(Post, related_name='post_video', on_delete=models.CASCADE)
    video = models.FileField(upload_to='post_video/')

    def __str__(self):
        return f"{self.post.title}---{self.post.user.email}"  


class PostsLike(models.Model):
    
    post=models.ForeignKey(Post, related_name='list_of_likes', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)
    like=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user}: {self.post}: {self.like}'