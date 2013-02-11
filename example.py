import readline
from yapredict import *

predictor = YaPredictor(PredictLang.en)

print ('Type any part of message and press <enter>')
w=input('>> ')

for n, wd in enumerate(predictor.complete_list(w).variants):
	print (n, wd)
