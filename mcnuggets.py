# def mcnugget_nums (i):
list_of_6 = []
list_of_9 = []
list_of_20 = []
non_nugget_small_nums = [1,2,3,4,5]
non_nugget_nums = []

def list_of_multiples (x, list_item):
	for i in range (6,43):
		if i%x == 0:
			list_item.append(i)

list_of_multiples (6,list_of_6)	
list_of_multiples (9,list_of_9)	
list_of_multiples (20,list_of_20)			

'''
print ("List of 6:", list_of_6)
print ("List of 9:", list_of_9)
print ("List of 20:", list_of_20)
'''

for i in range (6,44):
	if (i not in list_of_6): 
		if (i not in list_of_9):
			if (i not in list_of_20):
				if (i%3 != 0):
					if (i%20 != 0):
						non_nugget_nums.append(i)
	
print ("My set: ", non_nugget_small_nums + non_nugget_nums)


# still not catching 26, 29, 32, 35, 38, 41






def non_mcnugget_nums():
	# creating lists in one line, great syntax
	sixes = list(range(0,43,6))
	nines = list(range(0,43,9))
	twenties = list(range(0,43,20))

	# creates alist of all the mcnugget numbers
	all_mc_nums = set ()
	for t in twenties:
		for n in nines:
			for s in sixes:
				all_mc_nums.add(t + n +s)

	# check if every number is in the set or not 
	results = [0]
	for i in range (0,44):
		if i not in all_mc_nums:
			results.append(i)
	return results
	
print ("Working set: ", non_mcnugget_nums())			




