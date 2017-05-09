# -*- coding: utf-8 -*-
"""
Created on Wed May 10 01:14:28 2017

@author: myself
"""

import pandas as pd
import re
from collections import Counter 
from nltk.corpus import words

class nltk_word_check:
    words = nltk.corpus.words.words()
    def is_english_word(self,w):
        # creation of this dictionary would be done outside of 
        #     the function because you only need to do it once.
        english_vocab = set(w.lower() for w in self.words)
        chk = w in english_vocab
        if chk == True :
            return True
        else :
            return False

class abb_word:

    dic = pd.read_csv('abb_dictionary.csv')
    abb_words  = dic['word']
    
    #def __init__(self):

    def replace_word(self,word):
         for i in range(len(self.dic['word'])):
             if word.lower() == self.dic['word'][i].lower():
                 return self.dic['meaning'][i]
             else:
                 return ''
                 
             
class spell_check:
    
    def words(text): return re.findall(r'\w+', text.lower())
    
    WORDS = Counter(words(open('big.txt').read()))
    
    def P(word, N=sum(WORDS.values())): 
        "Probability of `word`."
        return WORDS[word] / N
    
    def correction(word): 
        "Most probable spelling correction for word."
        return max(candidates(word), key=P)
    
    def candidates(word): 
        "Generate possible spelling corrections for word."
        return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
    
    def known(words): 
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in WORDS)
    
    def edits1(word):
        "All edits that are one edit away from `word`."
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)
    
    def edits2(word): 
        "All edits that are two edits away from `word`."
        return (e2 for e1 in edits1(word) for e2 in edits1(e1))
             