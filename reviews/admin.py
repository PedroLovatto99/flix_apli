from django.contrib import admin
from .models import *


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars', 'comment')

admin.site.register(Review, ReviewAdmin)
