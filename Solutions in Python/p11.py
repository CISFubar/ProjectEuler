grid = open("grid.txt", "r")
arr = []

for l in grid:
	arr.append([int(i) for i in l.split()])

largest = 0

# search horizontally
for list in arr:
	product = 1
	count = 0
	
	while count < len(list) - 4:
		product = 1
		a = list[count:count + 4]
		
		for x in a:
			product *= x
			
		count += 1
		
	if product > largest:
		largest = product
		
tarrTuple = zip(*arr)
tarr = []

for x in tarrTuple:
	a = []
	for y in x:
		a.append(y)
	tarr.append(a)

# search vertically
for list in tarr:
	product = 1
	count = 0
	
	while count < len(list) - 4:
		product = 1
		a = list[count:count + 4]
		
		for x in a:
			product *= x
			
		count += 1
		
	if product > largest:
		largest = product
		
# search diagonally
list = [arr, tarr]

for a in list:
	i, j = 0, 0
	
	while i < len(a):
		while j < len(a[i]):
			if i + 3 < len(a) and j + 3 < len(a[i]):
				product = a[i][j] * a[i + 1][j + 1] * a[i + 2][j + 2] * a[i + 3][j + 3]
				
				if product > largest:
					largest = product
			j += 1
		i += 1
			
print largest