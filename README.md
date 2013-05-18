YaPredictor
===========

Simple wrapper for Yandex prediction typing API.
Typical usage is:

```python
>> from yapredict import YaPredictor, PredictLang
>> p = YaPredictor(PredictLang.ru, 'your-api-key-here')
>> p.complete_list('проверка').variants
["проверка", "проверка наличия","проверка скорости","проверка наличия номеров","проверка на",
 "проверка скорости интернета","проверка орфографии","проверках","проверка и","проверками","проверкам"]
>> p.complete('провер').new_words()
проверка
```
