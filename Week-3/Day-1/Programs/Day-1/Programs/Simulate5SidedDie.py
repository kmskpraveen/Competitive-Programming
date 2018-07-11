import random


def rand7():
	return random.randint(1, 7)


def rand5():

	# Implement rand5() using rand7()
	while (True):
		i = rand7()
		if i<=5:
			return i	


print 'Rolling 5-sided die...'
print rand5()