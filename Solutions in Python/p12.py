from math import sqrt

# generate a lot of prime numbers (less than 50000)
primes = [2, 3]
i = 3

while i < 50000:
	i += 2
	div = False
	for x in primes:
		if x > sqrt(i):
			break
		if i % x == 0:
			div = True
			break
	if not div:
		primes.append(i)

i = 0
sum = 0

while True:
	i += 1
	sum += i # update triangular number
	
	a = [] # list of exponents of prime factors
	s = sum # a substitue to work with
	
	for x in primes: # break down triangular number into prime factors
		c = 0 # exponent of prime factor
		while s % x == 0:
			c += 1
			s /= x
		if c != 0:
			a.append(c)
		
		if s == 1:
			break
	
	count = 1 # variable for number of factors
	
	for x in a: # number of factors = (a + 1)(b + 1)... for i^a * j^b... where i and j are prime factors
		count *= x + 1
	
	print sum, count # prints triangular number and number of factors
	
	if count >= 500: # stops when the first number with more than 500 factors is found
		print "\n%d has more than 500 factors" % sum
		break
	
