
#Task1- If a number is even or odd
number=int(input("enter the number: "))
if number%2==0:
    print( number, "is an even number")
else:
    print(number, 'is an odd number')

#Task2- sum of integers from 1 to 50 using loop
total=0
for i in range(1,51):
 total= total + i
 print("The sum of numbers from 1 to", i, "is",total)
