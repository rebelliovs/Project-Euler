# Initializing the maximum length and the number

maxx = 0
num = 0

# Iterating through a list from 1 to 1mil

for i in range(1,1000000):
	j = i
	count = 0
	while(j != 1):
		count +=1
		if j%2 == 0:
			j = j/2
		else:
			j = j*3 + 1
	if count > maxx:
		maxx = count
		num = i
maxx += 1

print("The longest chain is ", maxx, " produced by the number: ", num)

# Problem 14 on Project Euler
# https://projecteuler.net/problem=14

# Collatz sequence
# if n is even -> n = n/2
# if n is odd -> n = 3*n + 1