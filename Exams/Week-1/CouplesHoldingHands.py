
tracker = 0

def swap(Listl,n,pos):
	global tracker
	for i in range(len(Listl)):
		if Listl[i]==n:
			Listl[pos],Listl[i] = Listl[i],Listl[pos]
			tracker += 1
			break


def checker(Listnumbers):
	global tracker
	for i in range(0,len(Listnumbers)-1,2):
		# print(Listnumbers)
		if(Listnumbers[i]%2==0):
			if(Listnumbers[i+1]-Listnumbers[i]==1):
				continue
			else:
				swap(Listnumbers,Listnumbers[i]+1,i+1)
		else:
			if(Listnumbers[i]-Listnumbers[i+1]==1):
				continue
			else:
				swap(Listnumbers,Listnumbers[i]-1,i+1)



	# print(Dictionary)



def maincode():
	global tracker
	print(tracker)
	tracker = 0


checker([0,2,1,3])
maincode()
checker([3,2,0,1])
maincode()
checker([1,3,4,0,2,5])
maincode()
checker([3,2,0,1])
maincode()
checker([1,0])
maincode()