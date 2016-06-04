answer = 0
chunk = range(2,20)
def mod_check(n):
	#print "n: %d" % n
	for x in chunk:
	#	print "x: %d" % x
		if n%x > 0:
			break
		else:
			answer=n


for i in range(2520, 100000000, 2):
	#print "i: %d" % i
	mod_check(i)

print "ANSWER: %d" % answer