def meetingcalc(lister):
	count1 = 0
	for i in lister:
		for j in i:
			if j==1:
				count1 += 1
	if count1<=1:
		return 0
	dist = 9999999999
	for i in range(len(lister)):
		for j in range(len(lister[i])):
			x_c = i
			y_c = j
			# print(i,j)
			count = 0
			for i1 in range(len(lister)):
				for j1 in range(len(lister[i1])):
					if(lister[i1][j1]==1):
						# print(i1,j1)
						count += abs(i1-x_c)+abs(j1-y_c)
			# print(count)
			if(dist>count):
				dist = count
	return dist


print(meetingcalc([[1, 0, 0, 0, 1],[0, 0, 0, 0, 0],[0, 0, 1, 0, 0]]))
print(meetingcalc([[1, 0, 1, 0, 1],[0, 1, 0, 0, 0],[0, 1, 1, 0, 0]]))
print(meetingcalc([[1,1],[1,1]]))
print(meetingcalc([[0,0],[0,0]]))
print(meetingcalc([[1,0],[0,0]]))