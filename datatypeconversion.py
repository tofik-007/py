#datatype conversion
a = "audi"
b = "bentely"
c = "chevrolet", "viper"
d = "dodge"
e = 152
f = 250.365
#types of variables
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# #conversion of int to  float & vice versa
# print(int(f))
# print(float(e))
# #complex nummber 
# g=complex(58,5.5)
# print(g)
# print(type(g))                    
o = "jaguar"    # repr() printable string of given object
# o = 125.25
print(o)
print(repr(o))
#object -> string str(x) #can't understand
x = "james","bond" #-->tuple
print(str(x))
# print(type(x)) -> tuple
#eval(str) -> eval string <- object
# pagani = 1254
# pagani = 456
pagani = 7568
pagani = "boathead "
a = "pagani"
print(eval(a))
# print(type(a))
# s-> tuple
# s = "jarvis"
# print(tuple(s))
# print(list(s))
# frozenset------------------------------->
# s = "jarvis" #-->tuple
# s = frozenset(s) #---->unorderd
# print(s)
# random dictionary
person = {"name": "John", "age": 23, "gender": "male"}
fSet = frozenset(person) #takes key as value i frozenset
print('The frozen set is:', fSet) 
# list with frozenset
list = [1,2,3,4,5,6]
fset = frozenset(list)
# fset[1] = "hi" #doesn't support  item assignment
print(list)
print(fset)
# creating a list
favourite_subject = ["OS", "DBMS", "Algo"]

# creating a frozenset
f_subject = frozenset(favourite_subject)

# below line will generate error
f_subject[1] = "Networking"

# chr(x)
#returns the character that represent specific unicode ascii 
# print(chr(97))
# print(chr(96))
# print(chr(54)) unicode -> alphabet
# print(chr(104))
#unichr()In python 3, unichr is now called chr whereas unichr does no longer exist.
#ord() Converts a single character to its integer value.
# s = "h"
# print(ord("h"))  #ascii value: alphabet -> unicode
#hex(x) int -> hexadecimal string
# print(hex(10))
# print(hex(11))  #hex string means string wid prefix Xo
# print(oct(25.2)) #octal string means string wid prefix 0o #float won't work

