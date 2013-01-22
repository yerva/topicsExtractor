####################################################################################
# '''This module contains all the **Entities** related to profiling our entity'''
# ''' @User represents user'''
# ''' @Doc represents the document'''

from utils import *

#############################################################################################
class User:
    '''Represents the User  '''
    def __init__(self,ID,name,docLoc,lists=[]):
        self.id = ID
        self.name = name
        self.docLoc = docLoc
        self.doc = Doc(ID,name,docLoc) ### Creating a Document Object
        self.lists = lists ## set of lists in which this user is present
        return

    def getTopKeywords_TF(self,k=10):
        swc=sorted(self.doc.wordCountDict.items(),reverse=True,key=lambda x: x[1]['wordCount'])
        return swc[0:min(k,len(swc))] 

    def getTopKeywords_IDF(self,k=10):
        swc=sorted(self.doc.wordCountDict.items(),reverse=True,key=lambda x: x[1]['IDF'])
        return swc[0:min(k,len(swc))] 
    def getTopKeywords(self,TYPE='TF-IDF',k=10):
        swc=sorted(self.doc.wordCountDict.items(),reverse=True,key=lambda x: x[1][TYPE])
        return swc[0:min(k,len(swc))] 

#############################################################################################
class Doc:
    '''Represents the Document  '''
    def __init__(self,ID,name,docLoc):
        self.id = ID
        self.name = name ## name of the user related to this document
        self.doc = docLoc
        self.wordCountDict = dict()
        self.computeWordCounts()
        return

    def computeWordCounts(self):
        wordList = []
        for l in open(self.doc): wordList = wordList + TextUtils.preprocessLine(l.strip()).split()
        processWordList = TextUtils.preprocessText(wordList)
        WordCounter.wordCount(processWordList,self.wordCountDict)
        return

    def computeIDFCounts(self,IDF_Object):
        self.N = IDF_Object.N
        for word in self.wordCountDict:
            self.wordCountDict[word]['IDF'] = IDF_Object.getScore(word)
        self.computeTFIDFscores()

    def computeTFIDFscores(self):
        for word in self.wordCountDict:
            d=self.wordCountDict[word]
            self.wordCountDict[word]['TF-IDF'] = d['wordCount']/d['IDF']



#############################################################################################