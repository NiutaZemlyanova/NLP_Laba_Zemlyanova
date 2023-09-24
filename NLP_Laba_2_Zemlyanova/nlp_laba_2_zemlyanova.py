# -*- coding: utf-8 -*-
"""NLP_Laba_2_Zemlyanova.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nI-OcRRdhzLwQMzUrlegySzgwD6zB_-l

Практическая работа «Векторное представление слов»
Землянова Анна Группа 932001

Задание:

Используя import gensim, необходимо реализовать вычисление десяти самых близких по смыслу слов, находящихся в окрестности от результата операций сложения и вычитания в векторной модели.
Дана пара слов: "макароны" и "гуляш". Необходимо найти такую линейную комбинацию исходных слов, чтобы в результате вычислений заданная пара попадала в первую десятку.
"""

#подключим необходимые библиотеки
import gensim
import re

pat = re.compile("(.*)_NOUN")

from google.colab import drive
drive.mount('/content/drive')

word2vec = gensim.models.KeyedVectors.load_word2vec_format("/content/drive/MyDrive/marigostra.ru_persist_cbow.txt", binary=False, unicode_errors='ignore')

pos = ["макароны_NOUN"]

dist = word2vec.most_similar(positive=pos)
for i in dist:
 print (i)

neg = ["макароны_NOUN"]

dist = word2vec.most_similar(negative=neg, topn=10)
for i in dist:
 print (i)

pos = ["гуляш_NOUN"]

dist = word2vec.most_similar(positive=pos)
for i in dist:
 print (i)

neg = ["гуляш_NOUN"]

dist = word2vec.most_similar(negative=neg, topn=10)
for i in dist:
 print (i)

pos = ["вермишель_NOUN"]
neg = ["изображаться_VERB"]

dist = word2vec.most_similar(positive=pos, negative=neg, topn=10)
for i in dist:
 print (i)

pos = ["вермишель_NOUN"]
neg = ["изображаться_VERB"]
dist = word2vec.most_similar(positive=pos, negative=neg, topn=10)
for i in dist:
  e = pat.match(i[0])
  if e is not None:
    print(e.group(1))

pos = ["вермишель_NOUN"]
neg = ["совращения_NOUN"]

dist = word2vec.most_similar(positive=pos, negative=neg, topn=10)
for i in dist:
 print (i)

pos = ["вермишель_NOUN"]
neg = ["совращения_NOUN"]
dist = word2vec.most_similar(positive=pos, negative=neg, topn=10)
for i in dist:
  e = pat.match(i[0])
  if e is not None:
    print(e.group(1))