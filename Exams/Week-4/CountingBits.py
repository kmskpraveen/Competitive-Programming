def number(n):
	print(n, end = " = ")
	array = []
	for i in range(n+1):
		s = bin(i)[2:]	
		c = 0	
		for j in s:
			if j=='1':
				c +=1
		array.append(c)
	print(array)

number(5)
number(15)
number(16)
number(1)
number(25)
number(6)
