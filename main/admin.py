from django.contrib import admin
from .models import article, comments, user_profile


admin.site.register(article)
admin.site.register(comments)
admin.site.register(user_profile)
