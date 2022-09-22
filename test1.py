var = int(input("enter a number : "))
if var < 100:
	print("<100")
elif var > 100:
	print(">100")
else:
	print("=100")
n = int(input("enter a number to check if it's prime or not :"))
print("prime")  if n % 2 == 0 else print("not prime")