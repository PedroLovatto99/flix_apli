from django.contrib import admin
from .models import *


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality')

admin.site.register(Actor, ActorAdmin)
