from django.contrib import admin

# Register your models here.
from .models import Post, RandomTable

admin.site.register(Post)
admin.site.register(RandomTable)