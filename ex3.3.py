def is_even(x):
	if x==0:
		return True
	else:
		return is_odd(x-1)

def is_odd(x):
	return not is_even(x)

print(is_odd(5))			#[True]
print(is_even(6))			#[True]