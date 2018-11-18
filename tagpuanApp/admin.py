from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Lost)
admin.site.register(Found)
admin.site.register(Tag)
admin.site.register(Attach)
admin.site.register(Category)
admin.site.register(Landmark)

