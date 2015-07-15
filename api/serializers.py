from rest_framework import serializers
from models import Game, New, Stream, Match, Video


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'imageURL')


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = New
        fields = ('title', 'date', 'description', 'source', 'game', 'watch_count', 'imageURL')

class StreamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stream
        fields = ('title', 'imageUrl', 'channel', 'watchers_count',
                  'url_high', 'url_low', 'url_sound', 'videoType', 'duration')


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ('competitor1ImageUrl', 'competitor2ImageUrl', 'startDate', 'endDate',
                  'gameUrl', 'score1', 'score2')


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'watchCount', 'duration', 'date',
                  'videoType', 'videoUrl')
