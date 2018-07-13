def Base_convert(string):
	dicti={}
	for i in range(len(string)):
		dicti[i]=string[i]
	return dicti


short_URL_length = 7
ShortURL_Dict={}
Long_URL_Dict={}
count=0
base_62=Base_convert("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")


def URL_Shortnermethod(Given_URL):
	if (Given_URL in Long_URL_Dict):
		print("ShortURL Exists"+Long_URL_Dict[Given_URL])
		return
	global count
	s=""
	k=count
	count+=1

	if (k==0):
		s="0000000"
		if (s not in ShortURL_Dict):
			ShortURL_Dict[s]=Given_URL
			Long_URL_Dict[Given_URL]=s
			print("short URL for "+Given_URL+" is https://ca.ke/"+s)
			return

	while(k!=0):
		s=base_62[k%62]+s
		k=k//62
	l=len(s)

	if (l<short_URL_length):
		for i in range(short_URL_length-l):
			s="0"+s

	if (s not in ShortURL_Dict):
		ShortURL_Dict[s]=Given_URL
		Long_URL_Dict[Given_URL]=s

	print("Shortened URL for "+Given_URL+" is https://ca.ke/"+s)

while (True):
	print("\n\t1)Generate ShortURL\n\t2)Redirect ShortURL\n\t3)Stop\n\tYour option:",end="")
	i=int(input())
	if (i==1):
		Given_URL=input("Enter URL: ")
		URL_Shortnermethod(Given_URL)
	elif (i==2):
		Correct_URL=input("Enter a short URL: ")
		if ShortURL_Dict.get(Correct_URL,None) is not None:
			print("Redirect to "+ShortURL_Dict[Correct_URL])
		else:
			print("URL does not exist")
	elif(i==3):
		print("Thank you")
		break
	else:
		print("Please enter valid Input")