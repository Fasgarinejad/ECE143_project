import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import collections
from collections import Counter

books = pd.read_csv('book_data.csv',error_bad_lines = False)
books = books[books['book_title'].notna()] #removing null
books = books[books['genres'].notna()] #removing null
Horror_t = ""

import collections
from collections import Counter
stopwords_dict = Counter(stop_words)


#text = ' '.join([word for word in books.iloc[0].book_title.split() if word not in stopwords_dict])

for i in range(len(books)):
    text = ' '.join([word for word in books.iloc[i].book_title.split() if word not in stopwords_dict])
    Horror_t += text

Horror_words = Horror_t.split(" ")
Horror_words = [h.lower() for h in Horror_words]
dict_H = {}
for i in Horror_words:
    if i not in dict_H:
        dict_H[i] =1
    else:
        dict_H[i] +=1
sorted_dict_H = {k: v for k, v in sorted(dict_H.items(), key=lambda item: item[1])}
more_than_10 = {k:v for k,v in dict_H.items() if v>=100}
