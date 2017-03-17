# -*- coding: utf-8 -*-
from nltk import FreqDist
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.feature_extraction import DictVectorizer


def buildDTMFromArrayOfRecipes(recipesArray):
    ## An element of the array has the form {'id': .. , 'cuisine'}
    countList = []
    vectorizer = DictVectorizer()
    #vectorizer.fit_transform(recipesArray)
    for recipe in recipesArray:
        #vectorizer.fit_transform(FreqDist(recipe['ingredients']))
        countList.append(FreqDist(recipe['ingredients']))
        
    #DTM = pd.DataFrame(countList)
    #return DTM
    
    return vectorizer.fit_transform(countList)
    

def buildTfIdfMatrix(recipesArray):
    tfIdfVectorizer = TfidfTransformer()
    return tfIdfVectorizer.fit_transform(buildDTMFromArrayOfRecipes(recipesArray))

# print(buildTfIdfMatrix([{'ingredients':['salt', 'pepper']},{'ingredients':['meaaat', 'pepper']}]))
