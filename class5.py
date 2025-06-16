"""write a program to check whether the given number is positive?
number=int(input("enter the number"))
if number > 0:
    print("it's a positive number")
else:
    print("it's a negative number")
    

Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?
cost=int(input("enter the cost price "))
sell=int(input("enter the selling price "))
if sell > cost:
    print("it's a profit ",sell-cost)
else:
    print("it's a loss ",cost-sell)

    

Write a program to check whether the given number is greater than 15 or smaller than 15.

number=int(input("enter the number "))
if number > 15:
    print("it's greater than 15 ")
else:
    print("it's smaller than 15")

    

Write a program to check whether the given number is even or odd?"""
number=int(input("enter the number "))
if number % 2==0:
    print("it's a even number")
else:
    print("it's a odd number")
