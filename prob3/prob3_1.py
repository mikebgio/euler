#NOT FINISHED

prime_collection = []
def divy(n):
	bp = [2,3,5,7,11,13,17,19,23]
	bo = []
	for i in bp:
		#print i
		t = n % i
		print t
		if n % i == 0:
			print i
			bo.append(i)
	print bo


indo = int(raw_input("number? -->"))
x = divy(indo)
print x
#pull_primes(indo)
#print("Primes: " + str(prime_collection))
#answer = divider(indo, prime_collection)
#print("ANSWER: " + str(answer))