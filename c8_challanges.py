"""Operator precedence
Outline:
Write a program to understand how the operator precedence works
a = 12

b = 3

c = 4

d = 9

answer = b**c + d/ b*c + a
print("this it the ",answer)

Divisible Number
Outline:
Write to check a number is divisible by another number

number=int(input("enter the number 1 "))
number2=int(input("enter the number 2 "))
if number % number2==0: 
    print("number2 is divisible by number 1 ")
else:
    print("number2 is not divisible by number 1 ")


 Mean Value
Outline:
The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers."""
mean1=38

wrong_number=36

correct_number=56

total_number=40

#sum of 40 numbers

sum=mean1*total_number

print("The sum of 40 numbers:",sum)

#correct sum of these numbers

SUM2=sum-(wrong_number)+(correct_number)

print("CORRECTED SUM",SUM2)

#the correct mean

mean2=SUM2/total_number

print(mean2)

0