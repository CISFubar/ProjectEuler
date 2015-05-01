longest = 0
start = 0

for x in range(1, 999998, 2):
	count = 0
	temp = x + 2
	
	while temp != 1:
		if temp % 2 == 0:
			temp /= 2
		else:
			temp = 3 * temp + 1
		count += 1
	
	if count > longest:
		longest = count
		start = x + 2
		print x + 2, count, "*"
	else:
		print x + 2, count

print "* %d %d *" % (start, longest)