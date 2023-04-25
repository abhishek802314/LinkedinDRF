from django.contrib import admin
from .models import Favourite, FavouriteFolder
# Register your models here.
admin.site.register(Favourite)
admin.site.register(FavouriteFolder)
