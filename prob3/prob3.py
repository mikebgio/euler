#NOT FINISHED

prime_collection = []

def find_primes(num):
	mod_holder = []
	for x in range(2, num):
		#print("x= " + str(x) + "\nNum = " + str(num))
		mod = num % x
		#print("mod: "+ str(mod))
		mod_holder.append(mod)
		x+=1
	#print(mod_holder)
	try:
		mod_holder.index(0)
	except ValueError:
		prime_collection.append(num)
		print("Added " + str(num) + " to primes")
	#else:
	#	pass
		#print(".")

def pull_primes(num):
	print("Start pull_primes")
	numb = range(int(num**0.5)+1)
	print(numb)
	for i in numb:
		print("Iteration: " + str(i))
		find_primes(numb[i])
	#prime_collection.pop()
	prime_collection.sort(reverse=True)
	#prime_collection.pop()

def divider(main, numr):
	for x in range(len(numr)):
		print("Testing " + str(numr[x]))
		mod = main % numr[x]
		if mod == 0:
			return numr[x]
		else:
			pass


indo = long(raw_input("number? -->"))
print("Please Wait...")
pull_primes(indo)
#print("Primes: " + str(prime_collection))
answer = divider(indo, prime_collection)
print("ANSWER: " + str(answer))