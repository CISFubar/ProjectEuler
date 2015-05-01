from math import sqrt

def factors(n):
	if not isinstance(n, (int, long)):
		raise Exception("Incorrect data type")
		
	fact = [[i, n / i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0]
	factors = []
	
	for x in fact:
		factors += x
	
	f = []
	for x in factors:
		if x not in f:
			f.append(x)
			
	return sorted(f)

def primes(n):
	i = 3
	primes = [2, 3]
	
	if not isinstance(n, (int, long)):
		raise Exception("Incorrect data type")
	if n < 0:
		raise Exception("Cannot input negative numbers")
	if n > 2:
		while len(primes) < n:
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
	elif n == 1:
		primes = [2]
	elif n == 0:
		primes = []
		
	return primes
	
def fib(n):
	f = [1]
	a, b = 1, 1
	
	if not isinstance(n, (int, long)):
		raise Exception("Incorrect data type")
	if n < 0:
		raise Exception("Cannot input negative numbers")
		
	while len(f) < n:
		f.append(a)
		a, b = b, a + b
		
	return f
	
def factorial(n):
	fact = 1
	
	if not isinstance(n, (int, long)):
		raise Exception("Incorrect data type")
	if n < 0:
		raise Exception("Cannot input negative numbers")
	if n > 0:
		for i in range(2, n + 1):
			fact *= i
	
	return fact
	
def ncr(n, r):
	comb = 1
	
	if not (isinstance(n, (int, long)) and isinstance(r, (int, long))):
		raise Exception("Incorrect data type(s)")
	elif n < r:
		raise Exception("n cannot be less than r")
	elif n < 0 or r < 0:
		raise Exception("n and r cannot be negative")
	if r != 0 or n - r != 0:
		comb = factorial(n) / (factorial(r) * factorial(n - r))
	
	return comb
	
def npr(n, r):
	perm = 1
	
	if not (isinstance(n, (int, long)) and isinstance(r, (int, long))):
		raise Exception("Incorrect data type(s)")
	elif n < r:
		raise Exception("n cannot be less than r")
	elif n < 0 or r < 0:
		raise Exception("n and r cannot be negative")
	if r != 0 or n - r != 0:
		perm = factorial(n) / factorial(n - r)
	
	return perm