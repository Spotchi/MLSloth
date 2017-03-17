# TfIdf using blob documents
# http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/
# To install
# conda install -c https://conda.anaconda.org/sloria textblob
# python -m textblob.download_corpora
from __future__ import division, unicode_literals
import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist)/(1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
