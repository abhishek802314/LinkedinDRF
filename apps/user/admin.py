from django.contrib import admin
from .models import User, Skills , Position, EducationInformation
# Register your models here.
admin.site.register(User)
admin.site.register(Skills)
admin.site.register(Position)
admin.site.register(EducationInformation)