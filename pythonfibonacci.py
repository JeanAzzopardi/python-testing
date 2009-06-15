def fib(n):
	a,b = 0,1
	while b < n:
		print(b, end=' ')
		a,b = b, a+b
	print()

def main():
	print ("You are entering the main function!")
	fib(10)
