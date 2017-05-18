import math

def quadratic(a,b,c):
	L=[a,b,c]
	for m in L:
		if not isinstance(m,(int,float)):
			raise TypeError('bad operandtype')
	n=b*b-4*a*c
	if a==0:
		return Error
	elif n>0:
		x1=(-b+math.sqrt(n))/(2*a)
		x2=(-b-math.sqrt(n))/(2*a)
		return x1,x2
	elif n==0 :
		x=-b/(2*a)
		return x
	else:
		return 'No answan'
print (quadratic(2, 3, 1))
print (quadratic(1, 3, -4))
