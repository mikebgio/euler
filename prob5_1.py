td = 20
bd = 2
divisors = range(bd,(td+1))
chunk = [10, 100]
def mod_check(n):
	for x in divisors:
		if n%x > 0:
			break
		elif x>=td:
			return n
		

def range_check():
	for i in range(chunk[0], chunk[1]+bd, bd):
		first = mod_check(i)
		if first > 0:
			print "AHA!"
			return first
		elif i == (chunk[1]):
			print "Nothing found in %r" % chunk

should_restart=True
while should_restart:
	chunk[0]*=10
	chunk[1]*=10
	answer = range_check()
	if answer > 0:
		should_restart=False

print "ANSWER: %r" % answer