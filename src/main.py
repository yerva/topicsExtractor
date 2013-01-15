# '''Main module'''
import entities
import utils

# UserList .. Contains the list of users used in the experiments
UserList = []
UserObjects = dict() ## Maintains all the users
DocObjects = dict() ## Maintains all the documents
ID = 0
for username in UserList:
	user = User(ID,username,docLoc,lists) ### Making an user object with all available user information
	UserObjects[username] = user
	DocObjects[username] = user.doc


