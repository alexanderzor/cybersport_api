from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import viewsets
from serializers import GameSerializer, NewsSerializer, MatchSerializer, StreamSerializer, VideoSerializer
from models import Game, New, Match, Stream, Video
from rest_framework import filters
from rest_framework import generics

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = New.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('game',)

class StreamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('game',)


class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('game',)


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('game',)

from HTMLParser import HTMLParser
import urllib
class LinksParser(HTMLParser):
    result = []
    def __init__(self):
        HTMLParser.__init__(self)
        #self.result = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and ('class', 'title') in attrs:
            self.result.append(attrs[0][1])

class NewsParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.p_record = 0
        self.a_record = 0
        self.div_record = 0
        self.data = ''

    def handle_starttag(self, tag, attributes):
        if tag == 'div' and attributes == [('class', 'description')]:
            self.div_record = 1
            return
        if tag == 'div' and attributes == [('class', 'material-info')]:
            self.div_record = 0
            return

        #if tag == 'p':
            #self.p_record += 1
            #return

        #if tag == 'a' and ('rel', 'nofollow') in attributes:
            #self.a_record += 1
            #return

    #def handle_endtag(self, tag):

        #if tag == 'p' and self.p_record:
            #self.p_record -= 1
        #if tag == 'a' and self.a_record:
            #self.a_record -= 1

    def handle_data(self, data):
        if self.div_record:
            #if self.p_record or self.a_record:
            self.data += data
            self.data += '\n'


class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.title_record = 0
        self.a_record = 0
        self.div_record = 0
        self.data = ''
        self.title = ''

    def handle_starttag(self, tag, attributes):
        self.data += '<' + tag + '>'
        if tag == 'h1':
            self.title_record += 1
            return

        #if tag == 'p':
            #self.p_record += 1
            #return

        #if tag == 'a' and ('rel', 'nofollow') in attributes:
            #self.a_record += 1
            #return

    def handle_endtag(self, tag):
        self.data += '</' + tag + '>'
        if tag == 'h1':
            self.title_record -= 1
            return
        #if tag == 'p' and self.p_record:
            #self.p_record -= 1
        #if tag == 'a' and self.a_record:
            #self.a_record -= 1

    def handle_data(self, data):
        self.data += data
        if self.title_record:
            self.title = data

def parser(request):
    filehandle = urllib.urlopen('http://goodgame.ru/', '31.41.94.237:8080')
    f = filehandle.read()
    links = LinksParser()
    r = f.decode('utf-8')
    links.feed(r)
    result = links.result

    for link in result:
        if New.objects.filter(source=link).first():
            continue
        file_html = urllib.urlopen(link, '31.41.94.237:8080')
        new_html = file_html.read()
        start = new_html.index('<div class="description">')
        end = new_html.index('<a id="toComments"></a>') - 9
        #new_parser = NewsParser()
        #new = new_html.decode('utf-8')
        #new_parser.feed(new)
        #data = new_parser.data
        body = new_html[start:end].decode('utf-8')
        #html = Html.objects.create(body=data)
        parser = Parser()
        parser.feed(body)
        data = parser.data
        title = parser.title
        n = New.objects.create(title=title, description=data, source=link)

    context = {'data': 'ok'}
    return render(request, 'parser.html', context)



