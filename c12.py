"""Character occurrence
Outline:
Write a program to check how many times a character is repeated in a word?

Is this a Prime Number
Outline:
Write a program to print all the prime numbers which come in the range entered by the user?

Mid product
Outline:
Write a program to calculate the product of the middle digits of a number?








word=input("please enter your own word ")
char=input("please enter your character ")
i=0
count=0
while(i < len(word)):
    if (word[i]==char):
        count=count+1
    i=i+1
print("the total number of times the given character occured is ",count)

start=int(input("enter the lower range "))
end=int(input("enter the upper range "))
for i in range(start,end+1):
    if i > 1:
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print(i)"""

"""Mid product
Outline:
Write a program to calculate the product of the middle digits of a number?"""

num = int(input("Enter the number : "))
t = num
numLen = 0
#iterate the loop
while t>0: 
  numLen = numLen+1
  t = int(t/10)

if numLen>=4: #condition 1
  numLen = int(numLen/2)
  chk = 0
  while num>0: #iterate loop
    rem = num%10
    if chk==numLen: #nested condition 1
      midOne = rem
    elif chk==(numLen-1): 
      midTwo = rem
    num = int(num/10)
    chk = chk+1
  prod = midOne*midTwo #product of middle digits
  #display the result
  print("\nProduct of Mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)

else:
  print("\nIt's not a 4 or more than 4-digit number!")
