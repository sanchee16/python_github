#this code uses stack to reverse a string. In case there is a delimiter, it takes delimiter also as a part of string and reverses the complete string.
from Stack import *

def revrse(expr):
	revsd=[]
	stck=Stack()
	for each in expr:
		stck.push(each)
	while stck.isEmpty() is not True:
		revsd.append(stck.pop())
	print ''.join(revsd)



inpt=raw_input("Enter the string to be reversed!!!")
revrse(inpt)
