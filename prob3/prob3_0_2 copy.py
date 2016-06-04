prime_collection = [2]

def is_prime(n):  #found this on StackOverflow when I needed help speeding up my code
    return not any(n%i == 0 for i in range(2, n))

def divider(main, numr):
	for x in range(len(numr)):
		print("Testing " + str(numr[x]))
		mod = main % numr[x]
		if mod == 0:
			return numr[x]
		else:
			pass
			
def pull_primes(num):
	print("Start pull_primes")
	numb = range(int(num**0.5)+1)
	print(numb)
	for i in numb:
		print("Iteration: " + str(i))
		q = is_prime(numb[i])
		if q ==True:
			prime_collection.append(numb[i])
	prime_collection.sort(reverse=True)

indo = long(raw_input("number? -->"))
print("Please Wait...")
pull_primes(indo)
answer = divider(indo, prime_collection)
print("ANSWER: " + str(answer))


###BELOW IS MY ORIGINAL METHOD WHICH CRASHED ON BIG NUMBERS###

def find_primes(num):
	mod_holder = []
	for x in range(2, num):
		mod = num % x
		print("mod: "+ str(mod))
		mod_holder.append(mod)
		x+=1
	if 0 in mod_holder:
		pass
	else:
		prime_collection.append(num)
		print("Added " + str(num) + " to primes")

##############################################