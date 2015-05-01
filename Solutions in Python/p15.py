def factorial(x): # returns factorial of x
	fact = 1
	if x != 0:
		for x in range(x):
			fact *= x + 1
	return fact
	
def ncr(n, r): # returns n choose r
	if r == 0 or n - r == 0:
		return 1
	else:
		return factorial(n) / (factorial(r) * factorial(n - r))

sum = 0
num = 20
for x in range(num + 1):
	sum += ncr(num - 1, x) * ncr(num + 1, x + 1)
	
print sum