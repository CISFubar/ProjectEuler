def factorial(x): # returns factorial of x
	fact = 1
	if x != 0:
		for x in range(x):
			fact *= x + 1
	return fact

sum = 0
for x in "%d" % factorial(100):
	sum += int(x)
	
print sum