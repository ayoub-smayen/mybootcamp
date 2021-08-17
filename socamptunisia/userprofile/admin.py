from django.contrib import admin

from .models import UserProfile

from articles.models import Article

admin.site.register(UserProfile)
admin.site.register(Article)