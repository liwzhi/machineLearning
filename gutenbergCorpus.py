# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 19:49:20 2015

@author: weizhi
"""

import nltk
from nltk.corpus import gutenberg
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

#text = strip_headers(load_etext(2701)).strip()
#assert text.startswith('MOBY DICK; OR THE WHALE\n\nBy Herman Melville')


from gutenberg.query import get_etexts
from gutenberg.query import get_metadata
