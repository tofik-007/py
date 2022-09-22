num1 = 10
num2 = 25
s = [1, 2, 3, 4, 5, 6, 7,8 ,9]
if num1 in s:
    print("num1 is in the s")
else:
    print("num1 is  not in s")
if num2 in s:
    print("num2 is in the s")
else:
    print("num2 is  not in s")

num3 = int(input("enter a nbumber to check availablity in the list: "))
if num3 in s:
    print(num3, "is in list s")
else:
    print(num3,"is not in list")
num4=int(input("enter a nbumber to check availablity in the list: "))
if num4 not in s:
    print("not present")
else:
    print("present")
