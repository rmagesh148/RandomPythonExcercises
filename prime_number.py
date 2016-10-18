import math

def prime_number(n):
	#print "Yes"
	#print n
	limit = int(math.floor(math.sqrt(n)))
	#print limit
	if (n%2==0):
		#print "executing"
		return False
	for i in range(3,limit,2):
		#print i
		if (i%n == 0):
			return False
	return True

if prime_number(361):
	print "Prime"
else:
	print "Not a Prime"