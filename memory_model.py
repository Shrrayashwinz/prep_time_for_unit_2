import copy

b = [4, [5,6,7], 8, [9,10,11], 12]

c = copy.deepcopy(b)

c[1] = 2
b[3].append(13)
b[2] = 0

print(b,c)