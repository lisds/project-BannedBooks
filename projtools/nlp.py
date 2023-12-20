import spacy
import string
import numpy as np
import math
import pandas as pd
english_nlp = spacy.load('data/en_core_web_sm/en_core_web_sm-3.7.1')

vad_df = pd.DataFrame(pd.read_csv("data/NRC-VAD-Lexicon.txt")['aaaaaaah\t0.479\t0.606\t0.291'].str.split('\t'))
vad_df = vad_df.rename(columns={'aaaaaaah\t0.479\t0.606\t0.291':'Words'})

#splitting up list into multiple columns
vad_df['Valence'] = vad_df['Words'].apply(lambda x: x[1])
vad_df['Arousal'] = vad_df['Words'].apply(lambda x: x[2])
vad_df['Dominance'] = vad_df['Words'].apply(lambda x: x[3])
vad_df['Words'] = vad_df['Words'].apply(lambda x: x[0])
valence_dict = vad_df.set_index('Words')['Valence'].astype('float').to_dict()
arousal_dict = vad_df.set_index('Words')['Arousal'].astype('float').to_dict()
dominance_dict = vad_df.set_index('Words')['Dominance'].astype('float').to_dict()


def remove_punctuation(x):
    punctuation_trans = str.maketrans("", "", string.punctuation.join('/w'))
    # Use translate method to remove punctuation
    final_string = x.translate(punctuation_trans)
    return final_string
def lemmatizer(x):
    processed = english_nlp(x)
    lemmatized_string = ' '.join([token.lemma_ for token in processed])
    return lemmatized_string
def valence_average(x):
    scores = []
    for i in range(len(x)):
        #takes the uncapitalised version and retrieves its value from the dictionary
        scores.append(valence_dict.get(x[i].lower(), np.nan))
    #removing NaNs so that the length corresponds to the number of values
    scores = [score for score in scores if not math.isnan(score)]
    if len(scores) == 0:
        return np.nan
    return sum(scores)/len(scores)
def arousal_average(x):
    scores = []
    for i in range(len(x)):
        #takes the uncapitalised version and retrieves its value from the dictionary
        scores.append(arousal_dict.get(x[i].lower(), np.nan))
    #removing NaNs so that the length corresponds to the number of values
    scores = [score for score in scores if not math.isnan(score)]
    if len(scores) == 0:
        return np.nan
    return sum(scores)/len(scores)
def dominance_average(x):
    scores = []
    for i in range(len(x)):
        #takes the uncapitalised version and retrieves its value from the dictionary
        scores.append(dominance_dict.get(x[i].lower(), np.nan))
    #removing NaNs so that the length corresponds to the number of values
    scores = [score for score in scores if not math.isnan(score)]
    if len(scores) == 0:
        return np.nan
    return sum(scores)/len(scores)