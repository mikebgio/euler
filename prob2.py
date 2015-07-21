fibs = []
a = 1
b = 1
c = 1
i = 1
num = 0   #final answer

while i < 4000000:
	i = a
	print ("Step 1: %d" % i)
	fibs.append(i)
	c = a + b
	i = c
	print ("Step 2: %d" % i)
	fibs.append(i)
	b = a + c
	i = b
	print ("Step 3: %d" % i)
	fibs.append(i)
	a = c + b


#print fibs


# Find the even numbers in fibs list and add them together
for x in fibs:
	if (x % 2 == 0) and (x < 4000000):
		num += x

#This will be the answer
print num  

#This is inefficient