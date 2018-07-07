import string

string1 = raw_input("Enter first string: ")
string2 = raw_input("Enter second string: ")
str1 = ""
str2 = ""
for i in string1:
	if i==" ":
		continue
	else:
		str1 += i.lower()
for i in string2:
	if i==" ":
		continue
	else:
		str2 += i.lower()
# print(str1)
# print(str2)



count = 0
if(len(str1)==len(str2)):
	list1 = [1 for i in range(len(str1))]
	list2 = [1 for i in range(len(str2))]
	for i in range(len(str1)):
		for j in range(len(str2)):
			if str1[i]==str2[j] and list1[i]==1 and list2[j]==1:
				list1[i] = 0
				list2[j] = 0
		# else:
		# 	count = 1
		# 	print("False")
		# 	break

	# print(list1)
	# print(list2)
	if(count == 0):
		for i in list1:
			if i == 1:
				count = 2
				print("False")
				break
	if(count==0):
		for i in list2:
			if i == 1:
				count = 2
				print("False")
				break
	if(count==0):
		print("True")
else:
	print("False")