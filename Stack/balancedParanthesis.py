#The code is used to find if a given sequence of paranthesis is balanced or not.
from Stack import *

#function to check whether the corresponding values form a parenthesis pair.
def match(val1,val2):
	dic={"lpar1":"rpar1","lpar2":"rpar2","lpar3":"rpar3"};
	for key,value in dic.items():
		if key==val1 and value==val2 :
			return True
		else:
			return False

#function to find the type of paranthesis
def typeOfPara(exp):
	if exp is "{":
		return "lpar1"
	elif exp is "(":
		return "lpar2"
	elif exp is "[":
		return "lpar3"
	elif exp is "}":
		return "rpar1"
	elif exp is ")":
		return "rpar2"
	elif exp is "]":
		return "rpar3"


#function to check if paranthesis is balanced or not.
#if left paranthesis comes push it onto the stack 
#else pop the stack and check if the value from the stack and the rpar form a pair or not.
#if they  form a pair continue until the end of string 
#else break
#and check if the stack is empty or not
#if empty then its balanced 
#else its not balanced.
def balanced(expr):
	stck=Stack()
	for each in expr:
		if typeOfPara(each) is "lpar1" or typeOfPara(each) is "lpar2" or typeOfPara(each) is "lpar3":
			stck.push(each)
		elif typeOfPara(each) is "rpar1" or typeOfPara(each) is "rpar2" or typeOfPara(each) is "rpar3":
			typ=typeOfPara(each)
			spop=stck.pop()
			if match(spop,typ)==True:
				continue
			else:
				break


	if stck.isEmpty() is not True:
		print "Unbalanced Paranthesis"
	else:
		print "Balanced Paranthesis"


exprsn=list(raw_input("Enter the parenthesis expression"))
balanced(exprsn)