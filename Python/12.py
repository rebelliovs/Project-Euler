# Importing the 'math' library for the 'sqrt' function

import math

# Defining the 'divNo' function so we can get the number of divisors.

def divNo(no):
	n = 0
	sr = int(math.sqrt(no)) # Has to be of type int, otherwise causes
							# an Overflow Error while doing sr**sr, those
							# being of type float

	for i in range (1,int(sr)):
		if no % i == 0: n += 2

	if sr**sr == no: n -= 1

	return n

# Cannot start from 0, since X modulo 0 causes ZeroDivisionError
# therefore, we initialize 'no' with 1, and 'i' with 2, instead of 1

no = 1
i = 2

while divNo(no) < 500:
	no += i
	i += 1

print("The first triangle number with over 500 divisors is: ", no)

# It is insanely slow, but it gets the job done.
# For a faster result, you can try solving it by
# using prime factorisation or maybe the coprime property

# To find a triangular number: Xn = (n(n+1)) / 2

# Problem 12 on Project Euler
# https://projecteuler.net/problem=12