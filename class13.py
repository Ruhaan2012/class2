
"""Right angle triangle
Outline:
Write a program to demonstrate a right angle triangle pattern?

Floyd’s triangle
Outline:
Write a program to demonstrate a Floyd triangle pattern?

Diamond Pattern
Outline:
Write a program to demonstrate the numbers in a diamond pattern?

row=int(input("enter the number of rows "))
for i in range(row):
    for j in range(i+1):
        print("* ",end="")
    print()


row=int(input("enter the number of rows "))
number=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(row,end="")
        number=number+1
    print()"""

row=int(input("enter the number of rows "))
if row%2==0:
    half=int(row/2)
else:
    half=int(row/2)+1
space= half-1
for i in range(1,half+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range (2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,half):
    for j in range(1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range (1,2*(half-i)):
        print(end=str(num))
        num=num+1
    print()
