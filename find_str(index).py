print("str.index -> same as find  but raise exception if index not find")
str1 = input("enter a string :")
str2 = input("enter sub-string to finf it in a string :")
print("length of main string is : ",len(str1))
print("sub-string found in main string at index => ",str1.index(str2))
print("to find sub-string in specific range only enter start & end :")
start = int(input("enter a starting point to find from above string :"))
end = int(input("enter a ending point to find from string :"))
print("sub-string is in between index ",start," to ",end," => ",str1.index(str2, start,end ))
# str,start,stop