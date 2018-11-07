# Defining a function so we calculate the sum of the divisors of N up to N
def sumOfDivisors(n):
	res = 0
	for i in range(1,n):
		if n % i == 0 and i != n: res += i
	return res

# Initializing the result to 0
result = 0

# Iterating through the list of 10000 numbers
for i in range(1,10000):
	num = sumOfDivisors(i) # num becomes the sumOfDivisors of i
	if i == sumOfDivisors(num) and i != num: # we check if i == sumOfDivisors(num), and i is different than num
		result+= i + num # summing up

# Printing the result and dividing to 2, since we have pairs, so all numbers will be added twice
print("The sum of amicable numbers under 10000 is",int(result/2))

# Problem 21 on Project Euler
# https://projecteuler.net/problem=21