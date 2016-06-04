def is_prime(n):
    return not any(n%i == 0 for i in range(2, n))

def is_divisible(n):
	return not any(n%i == 0 for i in range(2, n))

def checker(n):
	for i in range(n):
		a = is_prime(i)
		print a
		b = is_divisible(i)
		print b
	if  a and b == True:
		return i

num = int(raw_input("--> "))

haf = num/2

q = is_prime(haf)

print q