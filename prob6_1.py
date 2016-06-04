indo = int(raw_input("Enter Number: "))
chunk = range(1,indo+1)

def squares(x): return pow(x,2)
def sub(x,y): return x-y
squareSums = squares(sum(chunk))
sumSquares = sum(map(squares,chunk))
answer = sub(squareSums,sumSquares)

print "Answer: %d" % answer