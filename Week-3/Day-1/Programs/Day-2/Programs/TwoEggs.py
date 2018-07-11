def eggs(number):
	check=14
	i1=0
	j1=0
	while i1<number:
		j1=i1
		i1=i1+check
		check=check-1
		print(i1,end=",")
		
	for k1 in range(j1+1,number+1):
		print(k1,end=",")