i = 1
j = 3
mainArr = [None] * 101
for i in range(len(mainArr)):
	if i == 0 or i == 101:
		continue
	if i%2 == 1:
		mainArr[i] = 1
	else:
		mainArr[i] = 0
for j in range(101):
	if j == 1 or j == 2 or j == 0:
		continue
	for i in range(len(mainArr)):
		if i == 0 or i == 101:
			continue
		if i%j == 0:
			if mainArr[i] == 0:
				mainArr[i] = 1
			else:
				mainArr[i] = 0
count = 0
for i in range(len(mainArr)):
	if i == 0 or i == 101:
		continue
	else:
		count += mainArr[i]
print count
print mainArr
