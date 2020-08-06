length = int(input())
array = [int(i) for i in input().split(' ')]
 
maximum = 0
i = 1
found = False
while i < length:
	ascending = 0
	while (i < length) and (array[i] > array[i - 1]):
		ascending += 1
		i += 1
	if ascending > 0:
		descending = 0
		while (i < length) and (array[i] < array[i - 1]):
			descending += 1
			i += 1
		if descending > 0:
			maximum_local = min(ascending, descending)
			maximum = max(maximum, maximum_local)
			found = True
	
	if ascending == 0:
		i += 1
 
if found:
	print(maximum, end=' ')
else:
	print(0, end=' ')
	
minimum = 0
i = 1
found = False
while i < length:
	descending = 0
	while (i < length) and (array[i] < array[i - 1]):
		descending += 1
		i += 1
	if descending > 0:
		ascending = 0
		while (i < length) and (array[i] > array[i - 1]):
			ascending += 1
			i += 1
		if ascending > 0:
			minimum_local = min(descending, ascending)
			minimum = max(minimum, minimum_local)
			found = True
	
	if descending == 0:
		i += 1
 
if found:
	print(minimum)
else:
	print(0)