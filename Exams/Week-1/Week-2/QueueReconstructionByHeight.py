def queueconstruct(order):
	dicti = {}
	for i in order:
		if i[0] in dicti:
			dicti[i[0]].append(i[1])
		else:
			dicti[i[0]] = [i[1]]
	for i in dicti.keys():
		dicti[i].sort()
	order1 = []
	answer = []
	order3 = []
	for i in order:
		if i[0] not in order1:
			order1.append(i[0])
	order1.sort()
	order2 = []

	for i in order1[::-1]:
		for j in dicti[i]:
			order2.append([i,j])


	# for i in order1:
	# 	for j in order:
	# 		if i == j[0] and j not in order2:
	# 			order2.append(j)
	# for i in range(len(order2)-1,-1,-1):
	# 	order3.append(order2[i])
	# order2 = order3
	# print(order2)
	answer.append(order2[0])
	for i in order2[1:]:
		# print("i: ",i)
		position = 0
		count = 0
		for j in range(len(answer)):
			if answer[j][0]>=i[0]:
				count += 1
			if count == i[1]:
				position = 1
				if i not in answer:
					answer.insert(j+1,i)
				# answer[j+1],answer[len(answer)-1] = answer[len(answer)-1],answer[j+1]
				break
		
		if (position!=1):
			answer.insert(0,i)
		# print(answer)
	return answer





print(queueconstruct([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
# print("+++++++++++++++++++++++++++++++++++++++++++++++++")
print(queueconstruct([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]))
print(queueconstruct([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]))
print(queueconstruct([ [5,0], [4,0], [7,0], [6,0], [4,4], [5,3],[6,2],[7,1]]))