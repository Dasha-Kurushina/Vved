X = [1,2,3,-1]

min = X[0]
for i in range(len(X)):
	x = X[i]
	if x < min:
		min = x

print(min)

# int m[5] = {1, -1, 0, 4, 2};
# int min = m[0];
# for(int i = 0; i < 5; ++i) {
#     if(m[i] < min) {
#         min = m[i];
#     }
# }