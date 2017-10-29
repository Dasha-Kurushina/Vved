X = [1,2,3,-1]

max = X[0]
for i in range(len(X)):
	x = X[i]
	if x > max:
		max = x

print(max)