#using Stack from Stack.py to convert infix expression to postfix expression
#TODO incorporate /0 and %0 not valid
from Stack import *

#Calculates the precedence of an operator
def precedence(op):
	pc={1:['('],2:['+','-'],3:['*','/','%'],4:['^']}
	for key,value in pc.items():
		if op in ' '.join(value):
			return key
	return None

#Assigns string values to operators
def typeof(op):
	if op is '(':
		return "lpar"
	elif op is ')':
		return "rpar"
	elif op is '+' or op is '-' or op is '*' or op is '/' or op is '%' or op is '^':
		return "oprator"
	elif op is ' ':
		return "empty"
	else:
		return "oprand" 

#converting to infix to postfix expression
def infix2postfix(expr):
	stck=Stack()
	pof_expr=[]
	for each in expr:
		x=typeof(each)
		if x is "lpar":
			stck.push(each)
		elif x is "rpar":
			next_item=stck.pop()
			while typeof(next_item) is not "lpar":
				pof_expr.append(next_item)
				next_item=stck.pop()
		elif x is "oprand":
			pof_expr.append(each)
		elif x is "empty":
			continue
		elif x is "oprator":
			while stck.size() is not 0 and precedence(each)<=precedence(stck.peek()):
				pof_expr.append(stck.pop())
			stck.push(each)

	while stck.size()>0:
		pof_expr.append(stck.pop())
	print ''.join(pof_expr)

exp=raw_input("Enter the infix notation")
x=list(exp)
for each in x:
	if x.index(each)%2==0 and typeof(each) is not "oprator":
		flag=1
	else:
		flag=0
if flag==1:
	print "Not a valid type"
else:
	infix2postfix(exp)
