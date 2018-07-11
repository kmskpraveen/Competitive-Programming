import random


def rand5():
    return random.randint(1, 5)


def rand7():

    # Implement rand7() using rand5()

    while (True):
    	i = rand5()
    	j = rand5()

    	if (i-1)*5+j<=21:
    		return ((i-1)*5+j)%7+1
    

print 'Rolling 7-sided die...'
print rand7()