#The code for sorting the input using insertion sort.

#Here, we take each element starting from second.
#To find the correct position of an element under consideration we compare its value with the previous values 
#until the index value is greater than zero and the currentvalue is less than the value being compared to.
#If true, shift the elements one position to the right
#and finally allocate the current value to the location where all the elements before the currentvalue are less than the currentvalue.
 
def insertionSort(lst):
	for indx in range(1,len(lst)):
		loc=indx
		curValue=lst[indx]
		while loc>0 and lst[loc-1]>curValue:
			lst[loc]=lst[loc-1]
			loc-=1
		lst[loc]=curValue
	print lst

#Take input from user. 
#using map function we convert the input into list of integers.
#call insertionSort function to sort the numbers.

strng=raw_input("Enter the list to be sorted")
numbers = map(int, strng.split())
insertionSort(numbers)