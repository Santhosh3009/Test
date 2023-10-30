def factorial(n):
	if n <= 1:
		return 1
	else:
		n = n * factorial(n - 1)
		return n

# Recursion is the easiest way to 
# solve this problem
# but, to make sure recursion's depth ends, above
# condition is necessary, otherwise
# errors occur

# Another way to solve problem
def factorial_(n):
	if n <= 1:
		return 1
	else:
		m = 1
		# range function produces inclusive range
		for integer in range(1, n + 1):
			m *= integer
		return m 
