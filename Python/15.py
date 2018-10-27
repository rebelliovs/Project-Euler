# Initialize the number of paths to 1
# Using combinatorics
# (2N)    (n)
# (  )  = ( )
# ( N)    (k)
# What I've used is the sum of [(n-k+i)/i] from 1 to k
# https://en.wikipedia.org/wiki/Binomial_coefficient

paths = 1

for i in range(20):
	paths *= (2 * 20) - i
	paths /= i + 1

print("The number of paths in a 20x20 grid is:", paths)

# Problem 15 on Project Euler
# https://projecteuler.net/problem=15