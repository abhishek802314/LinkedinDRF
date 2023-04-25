from django.db import models
from django.contrib.auth import get_user_model

from apps.post.models import Post

User = get_user_model()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', verbose_name="reply message", on_delete=models.SET_NULL, blank=True, null=True,related_name='children')

    def __str__(self):
        return f"{self.id}--{self.post.title}--{self.user.username} comment {self.comment}"
    
    class Meta:
        ordering = ('-create_at', )



class CommentLike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comment_like_owner')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_for_like')
    like = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.id} -- {self.comment.title}'
    
