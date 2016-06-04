indo = int(raw_input("--> "))
sqs = []

def squares(n):
	for i in range(1,n):
		sqs.append(i**2)

def summ(n):
	bunch = range(n+1)
	t=0
	for i in bunch:
		print bunch
		if bunch != []:
			s=bunch.pop()
			print "bunchpop %r" % bunch		
			t+=s
			print t

summ(10)


