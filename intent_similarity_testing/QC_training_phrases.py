# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:47:44 2023

@title: create_tp_embeddings
@description: compute cosine similarity matrix from training phrase embeddings
@author: Alexandra Hansma
"""

##################################################

## TO DO
# Fix file paths

##################################################

import pandas as pd
import numpy as np
import pickle
import time
from sklearn.metrics.pairwise import cosine_similarity

#Load training phrase embeddings from pickle file
with open('C:/Users/602762/Documents/VoiceBot/intent_similarity_testing/tp_embeddings.pkl', 'rb') as f:
    embedding_dict = pickle.load(f)

#Create a list of reference numbers and embedding for later user
reference_numbers = list(embedding_dict.keys())
embeddings = list(embedding_dict.values())

#Compute cosine similarity between all pairs of embeddings
similarity_matrix = cosine_similarity(list(embeddings))

#Set the diagonal elements to 0
np.fill_diagonal(similarity_matrix, 0)

#Convert similarity matrix to a df
df = pd.DataFrame(similarity_matrix, index = reference_numbers, columns = reference_numbers)

#Create buckets & classify similarities accross phrases
df['0.5 - 0.6'] = df.apply(lambda x: [col for col in df.columns if x[col] > 0.50000 and x[col] < 0.60000], axis=1)
data = df.loc[:, ['0.5 - 0.6']]
df = df.drop('0.5 - 0.6', axis = 1)

data['0.6 - 0.7'] = df.apply(lambda x: [col for col in df.columns if x[col] > 0.60000 and x[col] < 0.70000], axis=1)
data['0.7 - 0.8'] = df.apply(lambda x: [col for col in df.columns if x[col] > 0.70000 and x[col] < 0.80000], axis=1)
data['0.8 - 0.9'] = df.apply(lambda x: [col for col in df.columns if x[col] > 0.80000 and x[col] < 0.90000], axis=1)
data['0.9 - 1.0'] = df.apply(lambda x: [col for col in df.columns if x[col] > 0.90000 and x[col] < 1.00001], axis=1)

#Join similarity matrix to phrases and intents
ref_file = pd.read_excel('C:/Users/602762/Documents/VoiceBot/intent_similarity_testing/output_data/tp_4242023.xlsx')

data.reset_index(drop = False, inplace = True)
data.rename(columns = {'index': 'ref_id'}, inplace = True)

final_df = pd.merge(data, ref_file, on = 'ref_id', how = 'inner')

#Output final results
timestr = time.strftime('%Y_%m_%d')
df.to_excel('C:/Users/602762/Documents/VoiceBot/voicebot/intent_similarity_testing/data/matches_ ' + timestr + '.xlsx')
