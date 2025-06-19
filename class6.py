"""Write a program to check whether the given values have boolean values or not.
a=10
b=20
c=15
if a < b or a > c:
    print("both conditions are true ")
else:
    print("either one or both conditions are false ")"""


"""Write a program to check the application of not equal operator
a=10
b=12
c=12
print(b==c)
print(a!=b)"""

"""Write a program to calculate the BMI of a person?"""
weight=int(input("enrter your weight in kg "))
height=int(input("enter your height in cm "))
bmi=weight/(height/100)**2
print("your bmi is ",bmi)
if bmi <= 18.5:
    print("your underweight")
elif bmi <= 25:
    print("your healthy ")
elif bmi <= 35:
    print("you are overweight ")
elif bmi <= 40:
    print("your obese ")
else:
    print("your serveley obese ")