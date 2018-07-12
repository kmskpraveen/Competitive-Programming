Main_Dictionary = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--",	 "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--.."}

def diff_calc(words):
	String = []

	for i in words:
		s = ""
		for j in i:
			s += Main_Dictionary[j.upper()]
		if s not in String:
			String.append(s)
	return len(String)


print(diff_calc(["gin", "zen", "gig", "msg"]))
print(diff_calc(["a", "z", "g", "m"]))
print(diff_calc(["bhi", "vsv", "sgh", "vbi"]))
print(diff_calc(["a", "b", "c", "d"]))
print(diff_calc(["hig", "sip", "pot"]))
