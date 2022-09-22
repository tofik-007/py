# creating an empty list
list = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = input("enter the elements of list :")
	list.append(ele) # adding the element
print("list is : ",list)
print("list to tuple conversion :")
tuple = tuple(list)
print ("Tuple elements : ", tuple)