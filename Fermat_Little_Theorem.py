#!/usr/bin/python
p = 561

#def str2bool(v):
#	return v.lower() in ("yes", "true", "t", "1")
	
#Fermat's Little Theorem
# a**p - a % a = 0 where 1  a  p and p is prime

for i in range(0,p+1):
	print(str(i**p) + " pass " + str ((i**p - i) % p == 0)) 