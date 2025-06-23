"""Identity operator
Outline:
Write a program to illustrate the use of 'is' identity operator
#is,is not

a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=a
print(a is b)
print(a is c)
print(a is not b)

x=5
if(type(x) is  int ):
    print("true")
else:
    print("false")

b=2.5
if(type(b) is float ):
    print("true")
else:
    print("false")

#mebership operators=in,not in
numbers=[10,20,30,40,50]
a=20
print(a in numbers)
b=15
print(b not in numbers)


ASCII value
Outline:
Create a program to check the Ascii value of a given character."""
a=input("enter the character ")
if len(a)==1:
    ascii=ord(a)
    print("ascii value of the given character is ",ascii)
