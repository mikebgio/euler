num = 0
def fib2(n): # from Python Modules reference
	result = []
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, a+b
	return result


#print fibs
numin = raw_input("Enter Number --> ")
fibs = fib2(int(numin))
print fibs

# Find the even numbers in fibs list and add them together
for x in fibs:
	if (x % 2 == 0) and (x < 4000000):
		num += x
		
print ("Answer is: " + str(num))
#This will be the answer


#This is inefficient