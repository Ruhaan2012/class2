"""Exam Eligibility Check
Outline:
Write a program to check whether the student can take an exam or not.
 Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed.
If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.

mc=(input("enter your medical cause y/n"))
if mc.lower()=="y":
    print("you are alledgible to write the exam ")
else:
    att=int(input("enter your attendace score "))
    if att > 75:
        print("ypu are alledgible to take the exam ")
    else:
        print("you are not alledgible ")"""

            
"""bill"""

unit=int(input("enter your units "))

if unit < 50:
    amt=unit * 2.60 + 25
elif unit < 100:
     amt=unit * 3.25 + 35
elif unit < 200:
      amt=unit * 5.25 + 45
else:
     amt=unit * 7.25 + 75

print("your electricity bill is ",amt)

