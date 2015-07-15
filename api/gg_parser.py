from HTMLParser import HTMLParser
import urllib
from models import New
result = []


class LinksParser(HTMLParser):
    def handle_starttag(self, tag, attrs):

        if tag == 'a' and ('class', 'title') in attrs:
            result.append(attrs[0][1])
            return result


class NewsParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.p_record = 0
        self.a_record = 0
        self.div_record = 0
        self.data = []

    def handle_starttag(self, tag, attributes):
        if tag == 'div' and attributes == [('class', 'description')]:
            self.div_record = 1
            return
        if tag == 'div' and attributes == [('class', 'material-info')]:
            self.div_record = 0
            return

        if tag == 'p':
            self.p_record += 1
            return

        if tag == 'a' and ('rel', 'nofollow') in attributes:
            self.a_record += 1
            return

    def handle_endtag(self, tag):

        if tag == 'p' and self.p_record:
            self.p_record -= 1
        if tag == 'a' and self.a_record:
            self.a_record -= 1

    def handle_data(self, data):
        if self.div_record:
            if self.p_record or self.a_record:
                self.data.append(data)
                print data


def parse():
    #index_file = urllib.urlopen('http://goodgame.ru/', '91.204.112.237:8080')
    try:
        index_file = urllib.urlopen('http://goodgame.ru/', '91.204.112.237:8080')
        index_html = index_file.read()
        links = LinksParser()
        links.feed(index_html)
    except UnicodeDecodeError:
        pass
    for link in result:
        try:
            file_html = urllib.urlopen(link, '91.204.112.237:8080')
            new_html = file_html.read()
            new_parser = NewsParser()
            data = new_parser.feed(new_html)
        except UnicodeDecodeError:
            continue
    return result

