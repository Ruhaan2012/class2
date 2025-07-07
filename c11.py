"""Sum of Natural Numbers
Outline:
Write a program to find the sum of natural numbers.

Infinity
Outline:
Write a program to check the infinite loop?

Armstrong number
Outline:
Write a program to check if the number entered by the user is an Armstrong number or not?

number=int(input("enter the value of term "))
sum=0
i=1
while i <= number:
    sum=sum+i
    i=i+1
print(sum)


i=0
while i <= 0:
    print("my name is ruhaan ")


while True: 
    number1=int(input("enter number 1"))
    number2=int(input("enter number 2"))

    print("addition = to",number1+number2)
    print("subtracion = to",number1-number2)
    print("multiplacation = to",number1*number2)
    print("division = to",number1/number2)"""

number1=int(input("enter your number "))
sum=0
a=number1
while a > 0:
    digit=a % 10
    sum=sum+(digit**3)
    a//=10
if number1==sum:
    print("its an armstrong number ")
else:
    print("its not an armstrong number ")
    
