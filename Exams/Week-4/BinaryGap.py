def cnum(x):
	count = 0
	while (x!=0):
		x = (x & (x << 1)) 
		count=count+1
	 
	print(count)

# n = int(input())


# g_arr = []
# g_count = 0
def number(n):	
	print(n, end = " = ")	
	if n>0:
		print(bin(n)[2:],end = " = ")
		c = 0
		for i in bin(n)[2:]:
			if i == '1':
				c += 1
		if c>1:
			cnum(n)
		else:
			print(0)
	else:
		s = (bin((1 << 4) - -1*n))[2:]
		print(s, end = " = ")
		c = 0
		for i in s:
			if i == '1':
				c += 1
		if c>1:
			cnum(int(s,2))
		else:
			print(0)
		

number(22)
number(0)
number(55)
number(-5)
number(12354)
number(6)
number(256)


# s = s[2:]
# temp = 0
# co = 0
# print(s)
# check(s)

# for i in s:
# 	if i=='0':
# 		co = 0
# 	else:
# 		co += 1
# 		temp = max(temp,co)
# print(g_arr)
# print(max(g_arr))




