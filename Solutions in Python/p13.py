file = open("number.txt", "r")

sum = 0
for num in file:
	sum += int(num)
	
print ("%d" % sum)[0:10]