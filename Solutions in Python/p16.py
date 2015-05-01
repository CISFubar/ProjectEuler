var = 2 ** 1000
s = "%d" % var
sum = 0

for c in s:
	sum += int(c)

print sum