# -*- coding: utf-8 -*-
# This is beerware. Just send me a beer if you use this piece of code commercialy
# Feel free to copying and it's always legal until you are good.
# Illegal copying of this code prohibited by real patsan's law!
# 2013, @bobuk
import json

__version__ = "0.1"

try:
    pyver = 2
    import urllib2
    import urllib
    url_open = urllib2.urlopen
    url_quote = urllib.quote_plus
except:
    pyver = 3
    import urllib.request, urllib.parse
    url_open = urllib.request.urlopen
    url_quote = urllib.parse.quote_plus
    unicode = str

class PredictLang(object):
    '''Simple enum with list of supported languages. Currently it is only `ru' and `eng'.'''
    ru = 'ru'
    en = 'en'

class Prediction(object):
    '''Response from completer.
    If you use predictor.complete() - look at implementation of Prediction.new_words().
    For complete_list just use Prediction.variants attribute. It contains a list of potential replacers.'''
    def __init__(self, words):
        self.words = words

    def fromJson(self, json):
        self.is_end = json.get('endOfWord')
        self.pos = json.get('pos', 0)
        self.src = json.get('src')
        self.text = json.get('text')
        self.variants = json.get('data', [])
        self.variants.insert(0, self.words)
        return self

    def new_words(self):
        '''Return a new string with default replacement.'''
        words = unicode(self.words)
        if self.pos == 0:
            return words
        return words[:self.pos] + self.text

class YaPredictor(object):
    '''Pretty naive implementation of predictive input trough Yandex Predicition API.
    Typical usage is:
    >> p = YaPredictor(PredictLang.ru)
    >> p.complete_list('проверка').variants
    ["проверка", проверка наличия","проверка скорости","проверка наличия номеров","проверка на",
     "проверка скорости интернета","проверка орфографии","проверках","проверка и","проверками","проверкам"]
    >> p.complete('провер').new_words()
    проверка
    '''

    URL = "http://predictor.yandex.net/suggest.json/"
    URL_COMPLETE = URL + 'complete'
    URL_GET = URL + 'get'
    URL_S = "?site=mt-{lang}&q={words}&v=0"

    def __init__(self, language):
        self.lang(language)

    def lang(self, language):
        '''Set prediction language. From PredictLang enum.'''
        self.mt_lang = language

    def get_complete_url(self, words, full = False):
        url = (self.URL_GET if full else self.URL_COMPLETE) + self.URL_S
        return url.format(lang = self.mt_lang, words = url_quote(words))

    def complete(self, words):
        '''Return one prediction for given words.'''
        data = url_open(self.get_complete_url(words)).read()
        jdict = json.loads(data.decode('utf-8'))
        p = Prediction(words).fromJson(jdict)
        return p

    def complete_list(self, words):
        '''Return a Prediction with .variants.'''
        data = url_open(self.get_complete_url(words, full=True)).read()
        jdict = json.loads(data.decode('utf-8'))
        p = Prediction(words).fromJson(jdict)
        return p
