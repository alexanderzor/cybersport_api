from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    number = models.IntegerField()
    #def __unicode__(self):
        #return self.number
    def imageURL(self):
        return self.image.url


class New(models.Model):
    title = models.CharField(max_length=300)
    imageURL = models.URLField(null=True)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    source = models.URLField(blank=True)
    game = models.ForeignKey(Game, related_name='news', null=True)
    watch_count = models.IntegerField(null=True)
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Stream(models.Model):
    title = models.CharField(max_length=200)
    imageUrl = models.URLField()
    channel = models.CharField(max_length=200)
    watchers_count = models.IntegerField()
    url_high = models.URLField()
    url_low = models.URLField()
    url_sound = models.URLField()
    videoType = models.IntegerField() #(direct = 1, youtube = 2, twitch = 3)
    duration = models.DurationField()
    game = models.ForeignKey(Game, related_name='streams', null=True)

class Match(models.Model):
    competitor1 = models.CharField(max_length=200, null=True)
    competitor2 = models.CharField(max_length=200, null= True)
    competitor1ImageUrl = models.URLField()
    competitor2ImageUrl = models.URLField()
    startDate = models.DateTimeField(null=True)
    endDate = models.DateTimeField(null=True)
    gameUrl = models.URLField(blank=True, null=True)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    game = models.ForeignKey(Game, related_name='matches', null=True)




class Video(models.Model):
    title = models.CharField(max_length=200)
    watchCount = models.IntegerField(null=True)
    duration = models.DurationField(null=True)
    date = models.DateTimeField()
    videoType = models.IntegerField() # (direct = 1, youtube = 2, twitch = 3)
    videoUrl = models.URLField()
    game = models.ForeignKey(Game, related_name='videos', null=True)

