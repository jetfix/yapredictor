# -*- coding: utf-8 -*-

import unittest
from locale import setlocale, LC_ALL

from yapredict import *

if pyver == 2:
	import sys; reload(sys); sys.setdefaultencoding('utf-8') # yes, I realy hate this junk :(

class TestPredictFunctions(unittest.TestCase):
	def setUp(self):
		self.predictor = YaPredictor(PredictLang.ru)

	def test_init(self):
		self.assertEqual('ru', self.predictor.mt_lang)

	def test_lang_setup(self):
		self.predictor.lang(PredictLang.en)
		self.assertEqual('en', self.predictor.mt_lang)
		self.predictor.lang(PredictLang.ru)

	def test_words_url(self):
		self.assertEqual( self.predictor.get_complete_url('test') , 
						  'http://predictor.yandex.net/suggest.json/complete?site=mt-ru&q=test&v=0')
		self.assertEqual( self.predictor.get_complete_url('is ok') , 
						  'http://predictor.yandex.net/suggest.json/complete?site=mt-ru&q=is+ok&v=0')
		self.assertEqual( self.predictor.get_complete_url('test', full=True) , 
						  'http://predictor.yandex.net/suggest.json/get?site=mt-ru&q=test&v=0')

	def test_words_cyr_url(self):
		self.assertEqual( self.predictor.get_complete_url('провер') , 
						  'http://predictor.yandex.net/suggest.json/complete?site=mt-ru&q=' +
						  '%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80&v=0')
		self.assertEqual( self.predictor.get_complete_url('это работает, д') , 
						  'http://predictor.yandex.net/suggest.json/complete?site=mt-ru&q=' +
						  '%D1%8D%D1%82%D0%BE+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82%2C+%D0%B4&v=0')
		self.assertEqual( self.predictor.get_complete_url('провер', full=True) , 
						  'http://predictor.yandex.net/suggest.json/get?site=mt-ru&q=' +
						  '%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80&v=0')

	def test_completion_te(self):
		p = YaPredictor(PredictLang.en).complete('te')
		self.assertEqual(p.is_end, False)
		self.assertEqual(p.pos, -2)
		self.assertEqual(p.src, 'te')
		self.assertEqual(p.text, 'texas')
		self.assertEqual(p.new_words(), 'texas')
	
	def test_completion_test_m(self):
		p = YaPredictor(PredictLang.en).complete('test m')
		self.assertEqual(p.is_end, False)
		self.assertEqual(p.pos, -1)
		self.assertEqual(p.src, 'm')
		self.assertEqual(p.text, 'my')
		self.assertEqual(p.new_words(), 'test my')

	def test_completion_cyr_te(self):
		p = self.predictor.complete('те')
		self.assertEqual(p.is_end, False)
		self.assertEqual(p.pos, -2)
		self.assertEqual(p.src, 'те')
		self.assertEqual(p.text, 'тем')
		self.assertEqual(p.new_words(), 'тем')

	def test_completion_cyr_test_m(self):
		p = self.predictor.complete('проверь м')
		self.assertEqual(p.is_end, False)
		self.assertEqual(p.pos, -1)
		self.assertEqual(p.src, 'м')
		self.assertEqual(p.text, 'меня')
		self.assertEqual(p.new_words(), 'проверь меня')

	def test_completion_list_cyr_test_m(self):
		p = self.predictor.complete_list('проверь м')
		self.assertEqual(p.variants[0], 'проверь м')
		self.assertEqual(p.variants[1], 'проверь меня')
		self.assertEqual(p.variants[3], 'проверь машину')

	def test_completion_list_cyr_test_m(self):
		p = self.predictor.complete_list('проверь меня')
		self.assertEqual(p.variants[0], 'проверь меня')
		self.assertEqual(len(p.variants), 1)


if __name__ == '__main__':
	setlocale(LC_ALL)
	unittest.main()