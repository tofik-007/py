print("tuple's basic : ")
# here i use list to tuple conversion bcoz i find it easy. list to tuple
list = []

# number of elements as input
n = int(input("Enter number of elements for tuple : "))

# iterating till the range
for i in range(0, n):
    ele = input("enter the elements of tuple :")
    list.append(ele)  # adding the element

tuple = tuple(list)   #list = list(tuple)
print("Tuple : ", tuple)

index = int(input("enter an index number to get it value : "))
print("value of index number '",index,"' is : ",tuple[index])  # access value
# tuples r immutable
print("tuple has following methods : ")
print("cmp() does not work in python 3")
print("length of tuple is : ", len(tuple))
print("max of tuple is : ", max(tuple))
print("min of tuple is : ", min(tuple))
#del tuple
print("before deleting tuple : ", tuple)
del tuple
print("after delete tuple ", tuple)
