from django.contrib import admin
from .models import Post, PostImage, PostsLike, PostTag
# Register your models here.

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostsLike)
admin.site.register(PostTag)
