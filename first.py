def multiply(n):
  return 2*n
  
def generations(x,n):
  for y in range(x):
    n = multiply(n)
  return n

  
def auto_time():
	return generations(10, 1)