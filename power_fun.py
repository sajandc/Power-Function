x=int(input())
n=int(input())
d=int(input())
def power(x,n,d):
	s=0
	a=1
	for i in range(0,n):
		a=a*x	
	s=a%d
	return s
print(power(x,n,d))
