def countdown(n):
	if n<=0:
		print("Over?")
	else:
		print(n)
		countdown(n-1)
n=int(input('n='))
countdown(n)