from util import fib
import sys

def main(max_fib=30):
	if max_fib > 30:
		raise Exception

	for i in range(0, max_fib):
		print fib(i)


if __name__ == "__main__":
	main(int(sys.argv[1]))