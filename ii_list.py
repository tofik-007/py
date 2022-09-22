list = []

# number of elements as input
n = int(input("Enter number of elements for list : "))

# iterating till the range
for i in range(0, n):
    ele = input("enter the elements of list :")
    list.append(ele)  # adding the element
print("list is : ",list)

def add():
    print("<<<<<<<<<<----------- append the list ----------->>>>>>>>>>\n")
    print(list,"\n")
    add = input("add the object for list to apppend it : ")
    list.append( add ) #add at the end of list
    print ("appended list : ", list,"\n")

def update():
    print("<<<<<<<<<<----------- list update ----------->>>>>>>>>>\n")
    print(list,"\n")
    index = int(input("enter numbder of index which you want to update (digit): "))
    update  = input("enter new object to update it at the current object of index  : ")
    list [index] = update #update object
    print("updated list : ",list,"\n")
def insert():
    print("<<<<<<<<<<----------- insert object in list ----------->>>>>>>>>>\n")
    print(list,"\n")
    index = int(input("enter an index number at which you want to insert object (digit) :->"))
    val = input("enter a value for object to insert in the list : ")
    list.insert(index,val)
    print("after inserting ",val," at ",index," list is ",list,"\n")
add()
update()
insert()

