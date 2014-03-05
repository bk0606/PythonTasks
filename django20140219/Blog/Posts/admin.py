from django.contrib import admin

# Register models here.
from django.contrib import admin
from Posts.models import Post

admin.site.register(Post)