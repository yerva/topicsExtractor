import nltk
import os
from nltk.probability import *
from nltk.corpus import *


#############################################################################################
class TextUtils:
    ''' Contains utility functions related to operations on text'''

    STOPWORDS = stopwords.words("english") ## List of english stopwords
    STEMMER = nltk.PorterStemmer() ## Stemmer converting laughing,laughed,laughs -> laugh

    @staticmethod
    # Function to use for filtering
    def is_not_TweetStopWord(word):
        '''Remove all tweet specific stopwords'''
        if word.startswith("@"): return False
        if word.lower()=="rt": return False
        if word.lower()=="via": return False
        return True


    @staticmethod
    # Function to preprocess the text
    def preprocessText(text):
        ''' **Preprocess all the text** '''
        ''' #s0 remove Punctuations '''
        ''' #s1 #Tokenize'''
        ''' #s2 #RemoveStopWords--Generic'''
        ''' #s3 #RemoveStopWords--Twitter Specific'''
        ''' #s4 #Stemify'''
        tokens = [x.lower() for x in text]
        tokens = filter(TextUtils.is_not_TweetStopWord,tokens)
        doc = [word for word in tokens if word not in TextUtils.STOPWORDS and len(word) > 3]
        doc = [TextUtils.STEMMER.stem(word) for word in doc]
        return doc

    @staticmethod
    # Function to preprocess a Line.. by removing the punctuations
    def preprocessLine(text):
        text = text.replace('.',' ').replace('!',' ').replace('/',' ').replace('\\',' ')
        text = text.replace('?',' ').replace('-',' ').replace('\'',' ').replace('"',' ').replace('*',' ')
        return text

#############################################################################################
class WordCounter:
    wordDict = dict()

    @staticmethod
    # returns word count for the list of words in the docDictionary
    def wordCount(doc,docDict):
        for word in doc:
            d = dict()
            d['wordCount'] = doc.count(word) 
            docDict[word] = d 

###############################Document Collection based Methods################################
##### IDF Computation #####
class IDF:            
    ''' This class helps in computing the IDF of a document collection'''
    def __init__(self,dictsCollection):
        self.N = len(dictsCollection) ### Number of Documents
        self.dict = dict()
        for D in dictsCollection:
            for word in D.keys():
                if not self.dict.has_key(word):
                    self.dict[word] = 0
                self.dict[word] = self.dict[word] + 1
    
    ''' Returns the IDF-score(**number of documents containing the word**) of a word'''
    def getScore(self,word):
        if self.dict.has_key(word): return self.dict[word]
        return 0


##### Topic Models Computation #####
class TopicModels:
    ''' This class helps in computing the IDF of a document collection'''
    def __init__(self,dictsCollection):
        self.topicModel = {}


#############################################################################################

# Function to normalize frequencies
def norm_fd(fd):
	'''Normalizes the term frequency distribution'''
	fd_norm = {}
	n = fd.N()
	for word in fd.keys(): 
		fd_norm[word] =  fd[word]/n
	return fd_norm		



def dirFilesIterator(folder):
	''' Given a ``folder`` this function yields after returning a filename'''
	return

def getTFStats(document):
	fdist = FreqDist([w for w in document if w not in STOPWORDS])
	return fdist

class DocumentCorpus:
	''' ``DocumentCorpus`` class gets an handle to the document collection corpus. 
	This corpus could be used in the different topics extraction modules'''


	def init(self,folder, corpusName):
		''' ``folder`` argument represents the folder in which your corpus(``corpusName``) directory exists'''
		if folder not in nltk.path:
			nltk.path.append(folder)
		from nltk.corpus import corpusName
		self.corpus = corpusName
		return

class Document:
	''' ``Document`` class refers to an individual Document in a corpus'''
	
	def init(self,docName):
		self.docName=docName
		return

	def getText():
		return self.text


# ##########################################################
# ####################################################################################
# #-*- coding: utf-8 -*-
 
# import re
# import nltk
# from nltk.tokenize import RegexpTokenizer
# from nltk import bigrams, trigrams
# import math
 
 
# stopwords = nltk.corpus.stopwords.words('portuguese')
# tokenizer = RegexpTokenizer("[\w]+", flags = re.UNICODE) 
 
# def freq(word, doc):
#     return doc.count(word)
 
 
# def word_count(doc):
#     return len(doc)
 
 
# def tf(word, doc):
#     return (freq(word, doc) / float(word_count(doc)))
 
 
# def num_docs_containing(word, list_of_docs):
#     count = 0
#     for document in list_of_docs:
#         if freq(word, document) > 0:
#             count += 1
#     return 1 + count
 
 
# def idf(word, list_of_docs):
#     return math.log(len(list_of_docs) /
#             float(num_docs_containing(word, list_of_docs)))
 
 
# def tf_idf(word, doc, list_of_docs):
#     return (tf(word, doc) * idf(word, list_of_docs))
 
# #Compute the frequency for each term.
# vocabulary = []
# docs = {}
# all_tips = []
# for tip in (['documment 1', 'documment 2']):
#     tokens = tokenizer.tokenize(tip)
#     # tokens = tokenizer.tokenize(tip.text)
 
#     bi_tokens = bigrams(tokens)
#     tri_tokens = trigrams(tokens)
#     tokens = [token.lower() for token in tokens if len(token) > 2]
#     tokens = [token for token in tokens if token not in stopwords]
 
#     bi_tokens = [' '.join(token).lower() for token in bi_tokens]
#     bi_tokens = [token for token in bi_tokens if token not in stopwords]
 
#     tri_tokens = [' '.join(token).lower() for token in tri_tokens]
#     tri_tokens = [token for token in tri_tokens if token not in stopwords]
 
#     final_tokens = []
#     final_tokens.extend(tokens)
#     final_tokens.extend(bi_tokens)
#     final_tokens.extend(tri_tokens)
#     docs[tip] = {'freq': {}, 'tf': {}, 'idf': {},
#                         'tf-idf': {}, 'tokens': []}
 
#     for token in final_tokens:
#         #The frequency computed for each tip
#         docs[tip]['freq'][token] = freq(token, final_tokens)
#         #The term-frequency (Normalized Frequency)
#         docs[tip]['tf'][token] = tf(token, final_tokens)
#         docs[tip]['tokens'] = final_tokens
 
#     vocabulary.append(final_tokens)
 
# for doc in docs:
#     for token in docs[doc]['tf']:
#         #The Inverse-Document-Frequency
#         docs[doc]['idf'][token] = idf(token, vocabulary)
#         #The tf-idf
#         docs[doc]['tf-idf'][token] = tf_idf(token, docs[doc]['tokens'], vocabulary)
 
# #Now let's find out the most relevant words by tf-idf.
# words = {}
# for doc in docs:
#     for token in docs[doc]['tf-idf']:
#         if token not in words:
#             words[token] = docs[doc]['tf-idf'][token]
#         else:
#             if docs[doc]['tf-idf'][token] > words[token]:
#                 words[token] = docs[doc]['tf-idf'][token]
 
#     print doc
#     for token in docs[doc]['tf-idf']:
#         print token, docs[doc]['tf-idf'][token]
 
# for item in sorted(words.items(), key=lambda x: x[1], reverse=True):
#     print "%f <= %s" % (item[1], item[0])		