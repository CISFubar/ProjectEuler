from math import sqrt

def factors(n):
	return reduce(list.__add__,([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))

def d(n):
	sum = 0
	
	for i in factors(n):
		if i != n:
			sum += i
	return sum

sum = 0	
for i in range(1, 10000):
	x = i + 1
	a = d(x)
	
	if d(a) == x and a != x:
		sum += x

print sum