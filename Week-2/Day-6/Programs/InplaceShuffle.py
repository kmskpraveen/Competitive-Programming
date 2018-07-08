import random

def shuffle(the_list):

	# Shuffle the input in place
	if(len(the_list)>1):
		for i in range(len(the_list)):
			j = random.randint(i,len(the_list)-1)
			if i!=j:
				the_list[i],the_list[j] = the_list[j],the_list[i]



sample_list = [1, 2, 3, 4, 5]
print 'Sample list:', sample_list

print 'Shuffling sample list...'
shuffle(sample_list)
print sample_list
