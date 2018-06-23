#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 08:49:36 2018

@author: nick
"""
from flask_beer.models import beer_model
import logging
import os
import re
import pandas as pd

import gensim
from gensim.parsing.preprocessing import STOPWORDS
from gensim import corpora, models, similarities
from gensim.corpora import Dictionary
from gensim.models import LsiModel

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO

#Load in beer data, clean it, and reindex
beer = pd.read_csv('~/Dropbox/beer_scrape/cleaned_data/full_data_2.csv')
beer_with_desc = beer[beer.description.str.contains('No notes at this time.') == False]
beer_with_desc.reset_index()
documents = beer_with_desc['description'].tolist()

# load dictionary
dictionary = Dictionary.load('/home/nick/Documents/Insight/itemp/deerwester.dict')

# load corpus
corpus = corpora.MmCorpus('/home/nick/Documents/Insight/itemp/deerwester.mm')

# load model
lsi= LsiModel.load('/home/nick/Documents/Insight/itemp/model.lsi')
index = similarities.MatrixSimilarity.load('/home/nick/Documents/Insight/itemp/deerwester.index')



#tokenizer function
def get_beers(text):
    #set stop words 
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # remove it if you need punctuation 
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent) if word not in stop_words]
    
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    filtered_tokens = [token for token in tokens if re.search('[a-zA-Z]', token)]     
            
    #stem tokens
    sb_stemmer = SnowballStemmer("english")
    terms = [sb_stemmer.stem(i) for i in filtered_tokens]
    
    terms_2 = ' '.join(terms)

    doc = terms_2
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow] # convert the query to LSI space

    sims = index[vec_lsi] 
    sims = sorted(enumerate(sims), key=lambda item: -item[1])

    top = []
    for i in sims[0:10]:
        top.append(i[0])

    results = beer_with_desc.iloc[top]
    return(results)
