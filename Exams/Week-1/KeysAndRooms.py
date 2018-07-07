
Dictionary = {}
def unlock(pop):
	global Dictionary
	for i in pop:
		Dictionary[i] = 1

def checker(Listnumbers):
	global Dictionary
	for i in range(len(Listnumbers)):
		Dictionary[i] = 0
	Dictionary[0] = 1
	for i in range(len(Listnumbers)):
		for keys in Dictionary.keys():
			if Dictionary[keys]==1:
				unlock(Listnumbers[keys])
	# print(Dictionary)



def maincode():
	global Dictionary
	count = 0
	for i in Dictionary.keys():
		if Dictionary[i]==0:
			count = 1
			print("False")

	if count==0:
		print("True")

	Dictionary = {}


checker([[1], [0,2,4], [1,3,4], [2], [1,2]])
maincode()
checker([[1,3], [3,0,1], [2], [0]])
maincode()
checker([[1], [0,2], [2]])
maincode()
checker([[1,3], [3,0,1], [2], [0]])
maincode()
checker([[1,2,3], [0], [0], [0]])
maincode()
checker([[1], [0,2,4], [1,3,4], [2], [1,2]])
maincode()
checker([[1], [2,3], [1,2], [4], [1], [5]])
maincode()
checker([[1], [2], [3], [4], [2]])
maincode()
checker([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]])
maincode()
checker([[4], [0], [1], [2], [3]])
maincode()