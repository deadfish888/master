def factorial(n):
	"""
	Ham tinh n!
	Tra ve giai thua cua n
	"""
	if n==0:
		return 1
	else:
		return n * factorial(n-1)

print('x!=',factorial(int(input('x='))))