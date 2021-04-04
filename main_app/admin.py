from django.contrib import admin
from .models import Bounty, Post, Comment

# Register your models here.
admin.site.register(Bounty)
admin.site.register(Post)
admin.site.register(Comment)