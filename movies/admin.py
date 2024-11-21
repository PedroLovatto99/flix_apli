from django.contrib import admin
from movies.models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'gender', 'release_date', 'resume')

admin.site.register(Movie, MovieAdmin)
