def valueOf(c):
	a = []
	valueList = open("value.txt", "r")
	for x in valueList:
		a.append(x[:1])
	return a.index(c) + 1

nameList = open("names.txt", "r")

l = nameList.read().split(",")
list = []

for n in l:
	list.append(n[1:-1])

sList = sorted(list)

finalSum = 0

for name in sList:
	place = sList.index(name) + 1
	sum = 0
	
	for c in name:
		sum += valueOf(c)
	
	value = place * sum
	finalSum += value

print finalSum