def toWord(num):
	f1 = open("words.txt", "r")
	f2 = open("words_2.txt", "r")
	
	basic = []
	other = []
	
	for line in f1:
		basic.append(line)
	for line in f2:
		other.append(line)
		
	s = "%d" % num
	
	while len(s) < 3:
		s = "0" + s
	
	a, b, c = int(s[0:1]), int(s[1:2]), int(s[2:3])
	
	x = ""
	y = ""
	
	if b == 0:
		x = basic[c - 1]
	elif b == 1:
		x = other[c]
	elif c != 0:
		x = other[b + 8][0:len(other[b + 8]) - 1] + " " + basic[c - 1]
	else:
		x = other[b + 8][0:len(other[b + 8]) - 1] + " "
		
	if a != 0:
		y = basic[a - 1][0:len(basic[a - 1]) - 1] + " hundred"
	
	if num % 100 != 0:
		word = y + " and " + x
	else:
		word = y + " "
		
	if num == 1000:
		word = "one thousand"
	elif num >= 100:
		word = word[:len(word) - 1]
	else:
		word = word[5:len(word) - 1]
		
	return word

sum = 0

for x in range(1000):
	print toWord(x + 1), x + 1
	sum += len(toWord(x + 1).replace(" ", ""))

print sum