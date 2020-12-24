# Search
Для начала работы следует запустить парсер из корня проекта:

scrapy crawl pycoder -o output.json

Проверить, что файл output.json создался без проблем и в нормальной кодировке (переставить с UTF-8 на ANSI).

Затем можно запустить файл elastic_search.py:

python elastic_search.py
