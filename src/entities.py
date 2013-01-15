####################################################################################
# '''This module contains all the **Entities** related to profiling our entity'''
# ''' @User represents user'''
# ''' @Doc represents the document'''

import utils


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
        for l in open(self.doc): wordList = wordList + l.strip().split()
        processWordList = TextUtils.preprocessText(wordList)
        WordCounter.wordCount(processWordList,self.wordCountDict)
        return


#############################################################################################