# '''Main module'''
from entities import *
from utils import *
import simplejson as json

### CONFIG-INFO ####
DATA_FOLDER_PATH = '/home/yerva/workspace/topicsExtractor/src/data/test/'



jsonString = ""
for l in open('usersList.json.conf'):
	jsonString += l.strip()


# UserList .. Contains the list of users used in the experiments
UserList = json.loads(jsonString)['users']
UserObjects = dict() ## Maintains all the users
DocObjects = dict() ## Maintains all the documents
DictObjects = []
ID = 0
for u in UserList:
	user = User(ID,u['username'],DATA_FOLDER_PATH+u['docLoc'],u['lists']) ### Making an user object with all available user information
	UserObjects[user.name] = user
	DocObjects[user.name] = user.doc
	DictObjects.append(user.doc.wordCountDict)

#### computing IDF statistics only after all the user objects are loaded ###
IDF_OBJ = IDF(DictObjects)
for doc in DocObjects:
	DocObjects[doc].computeIDFCounts(IDF_OBJ)	
###########################################################################	

u1=UserObjects['sampleuser1']
print u1.getTopKeywords_TF(5)
print u1.getTopKeywords_IDF(5)
print '****'
print u1.getTopKeywords('TF-IDF',5)
