# Initializing and calculating the number (2^1000) and converting it to a string
number = str(2**1000)
r = 0 # r = result

# Iterating through the string we just created and summing up the digits

for i in range(len(number)):
	r += int(number[i])

print("The sum of digits of 2^1000 is:", r)

# Problem 16 on Project Euler
# https://projecteuler.net/problem=16