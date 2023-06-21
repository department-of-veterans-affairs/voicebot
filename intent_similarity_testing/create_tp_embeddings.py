# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:20:34 2023

@title: create_tp_embeddings
@description: create embeddings of training phrases using tensorflow's universal sentence encoder model
@author: Alexandra Hansma
"""

##################################################

## TO DO
# Determine format of excel that will be read in
# Determine which columns need to be kept from original file 
# Add code to preprocess
# Fix file paths

##################################################

import pandas as pd
import pickle
import time
import tensorflow as tf
import tensorflow_hub as hub

#Load the Universal Sentence Encoder model
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

#Read in dataframe
df = pd.read_excel('C:/Users/602762/Documents/VoiceBot/ml_testing/testing_round_2_ah.xlsx')

#Create a list of the phrases and ref ids
phrases = df['phrase'].tolist()
reference_numbers = df['ref_id'].tolist()

#Compute embedding for each sentece
embeddings = embed(phrases).numpy()

#Add the reference id back to the embeddings
embedding_dict = {}
for i, ref_num in enumerate(reference_numbers):
    embedding_dict[ref_num] = embeddings[i]
    
#Save embeddings to a pickle file
timestr = time.strftime('%Y_%m_%d')
with open('C:/Users/602762/Documents/VoiceBot/voicebot/intent_similarity_testing/data/tp_embeddings_ ' + timestr + '.pkl', 'wb') as f:
    pickle.dump(embedding_dict, f)
    

