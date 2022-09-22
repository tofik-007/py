def sort():
    print("<<<<<<<<<<----------- sort the list(create list to sort it) ----------->>>>>>>>>>\n")
    list = []
    n = int(input("enter number of element of list : "))
    for i in range(0,n):
        ele = input("enter an elements of list : " )
        list.append(ele)
    print("list before sorting is : ",list,"\n")
    list.sort()
    print("list after sorting is : ",list,"\n")
sort()