import nltk
import os
from nltk.probability import *
from nltk.corpus import *

STOPWORDS = stopwords.words("english") ## List of english stopwords
STEMMER = nltk.PorterStemmer() ## Stemmer converting laughing,laughed,laughs -> laugh

# Function to normalize frequencies
def norm_fd(fd):
	'''Normalizes the term frequency distribution'''
	fd_norm = {}
	n = fd.N()
	for word in fd.keys(): 
		fd_norm[word] =  fd[word]/n
	return fd_norm		

# Function to use for filtering
def is_not_TweetStopWord(word):
	'''Remove all tweet specific stopwords'''
	if word.startswith("@"): return False
	if word.lower()=="rt": return False
	if word.lower()=="via": return False
	return True


# Function to preprocess the text
def preprocessText(text):
	''' Preprocess all the text'''
	''' #s1 #Tokenize'''
	''' #s2 #RemoveStopWords--Generic'''
	''' #s3 #RemoveStopWords--Twitter Specific'''
	''' #s4 #Stemify'''
	tokens = [x.lower() for x in text]
	tokens = filter(is_not_TweetStopWord,tokens)
	doc = [word for word in tokens if word not in STOPWORDS and len(word) > 3]
	doc = [STEMMER.stem(word) for word in doc]
	return doc


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