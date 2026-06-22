from django.contrib import admin
from games.models import Game, Platform


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'rating')

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
