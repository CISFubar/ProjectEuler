import extmath

def isAbundant(n):
	factors = extmath.factors(n)
	
	sum = 0
	for x in factors:
		if x != n:
			sum += x
	
	return sum > n
	
abundant = []

for x in range(28123 / 2 + 1):
	if isAbundant(x):
		abundant.append(x)

n = []
		
for x in range(1, 28124):
	c = False
	for i in abundant:
		if x - i in abundant:
			c = True
			break
		if i > x:
			break
	if not c:
		n.append(x)
		
a = []
for x in n:
	if x not in a:
		a.append(x)

sum = 0
for x in a:
	sum += x
	
print sum