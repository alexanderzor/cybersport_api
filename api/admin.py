from django import forms
from django.contrib import admin

from models import New, Game, Stream, Match, Video

class NewsAdmin(admin.ModelAdmin):

    list_display = ('title', 'date',)

    class Meta:
        model = New

admin.site.register(New, NewsAdmin)

class GameAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)

    class Meta:
        model = Game

admin.site.register(Game, GameAdmin)
class StreamAdmin(admin.ModelAdmin):

    list_display = ('title','channel',)

    class Meta:
        model = Stream

admin.site.register(Stream, StreamAdmin)
class MatchAdmin(admin.ModelAdmin):

    list_display = ('competitor1', 'competitor2',)

    class Meta:
        model = Match

admin.site.register(Match, MatchAdmin)

class VideoAdmin(admin.ModelAdmin):

    list_display = ('title', 'date',)

    class Meta:
        model = Video

admin.site.register(Video, VideoAdmin)

