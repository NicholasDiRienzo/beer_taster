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
import numpy as np

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
beer = pd.read_csv('~/Dropbox/beer_scrape/cleaned_data/all_beers.csv')
beer_with_desc = beer[beer.description.str.contains('No notes at this time.') == False]
beer_with_desc.reset_index()
documents = beer_with_desc['description'].tolist()

# make df of just good beers
beers_good = beer_with_desc[beer_with_desc.beer_overall_score >4.00]

# load dictionary
dictionary = Dictionary.load('/home/nick/Documents/Insight/itemp/deerwester.dict')

# load corpus
corpus = corpora.MmCorpus('/home/nick/Documents/Insight/itemp/deerwester.mm')

# load model
lsi= LsiModel.load('/home/nick/Documents/Insight/itemp/model.lsi')
index = similarities.MatrixSimilarity.load('/home/nick/Documents/Insight/itemp/deerwester.index')

#################
######
# building in an if else

def get_beers_val(good, bad = 'xxx'):
    print(good)
    print(bad)
    #set stop words 
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # remove it if you need punctuation 
    
    tokens_good = [word.lower() for sent in nltk.sent_tokenize(good) for word in nltk.word_tokenize(sent) if word not in stop_words]
    
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    filtered_tokens_good = [token for token in tokens_good if re.search('[a-zA-Z]', token)]     
            
    #stem tokens
    sb_stemmer = SnowballStemmer("english")
    terms_good = [sb_stemmer.stem(i) for i in filtered_tokens_good]
    # joint them
    terms_good_2 = ' '.join(terms_good)

    print(terms_good_2)
    vec_good = lsi[dictionary.doc2bow(terms_good_2.lower().split())]
    print(vec_good)
    
    if vec_good == []:
        return('please try another characteristic')

    # for the bad words
    tokens_bad = [word.lower() for sent in nltk.sent_tokenize(bad) for word in nltk.word_tokenize(sent) if word not in stop_words]
    
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    filtered_tokens_bad = [token for token in tokens_bad if re.search('[a-zA-Z]', token)]     
            
    #stem tokens
    terms_bad = [sb_stemmer.stem(i) for i in filtered_tokens_bad]
    # joint them
    terms_bad_2 = ' '.join(terms_bad)
 
    print(terms_bad_2)
    vec_bad = lsi[dictionary.doc2bow(terms_bad_2.lower().split())]
    print(vec_bad)
    
    if vec_bad == []:
        vec_final = vec_good
        
        sims = index[vec_final] 
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        
        sims_2 = np.array(sims)
        sim_score = []
        for i in range(10):
            score = sims_2[i][1]
            sim_score.append(score)
        
        sim_score = pd.Series(sim_score)

        top = []
        for i in sims[0:10]:
            top.append(i[0])
            

        results = pd.DataFrame(beer_with_desc.iloc[top])
        results['sim_score'] = sim_score.values*100
        results = results.round(2)

    else:
        new_vec = []
        for i in range(len(vec_good)):
            val = np.array(vec_good[i][1]) - np.array(vec_bad[i][1])
            new_vec.append(val)
        
        num_list = list(range(0,len(vec_good)))


        vec_final = list(zip(num_list, new_vec))

        sims = index[vec_final] 
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        
        sims_2 = np.array(sims)
        sim_score = []
        for i in range(10):
            score = sims_2[i][1]
            sim_score.append(score)
        
        sim_score = pd.Series(sim_score)

        top = []
        for i in sims[0:10]:
            top.append(i[0])
            

    results = pd.DataFrame(beer_with_desc.iloc[top])
    results['sim_score'] = sim_score.values*100
    results = results.round(2)
    return(results)

