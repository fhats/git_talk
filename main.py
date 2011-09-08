def main():
	max_fib = 30
	for i in range(0, max_fib):
		print fib(i)

def fib(n):
	"""Find the nth term of the Fibonacci sequence."""
	if n < 2:
		return n
	
	return fib(n-2) + fib(n-1)

if __name__ == "__main__":
	main()