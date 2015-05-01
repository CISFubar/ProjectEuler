a, b = 1, 1
list = [1]

while b / (10 ** 999) <= 1:
	a, b = b, a + b
	list.append(a)

print len(list) - 1