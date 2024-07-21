
#1. Write a program that takes an integer input from the user and checks if it is a positive number. If the number is positive, print "The number is positive."

a=int(input("Enter the number:"))
if a>=0:
    print("The number is posivite")
else:
    print("The number is negative")


#2. Create a program that takes an integer input from the user and checks if it is an even number. If it is even, print "The number is even."python

a=int(input("Enter the number: "))
if a%2==0:
    print("The number is even")
else:
    print("The number is odd")


# 3.Create a program that asks the user for their age and determines if they are eligible to vote. Print "Eligible to vote" if they are 18 or older, otherwise print "Not eligible to vote."

a=int(input("Enter your age : "))
if a>=0 and a>=18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")


#4. Write a program that asks the user to enter a password and checks if it matches a predefined password. If the password matches, print "Access granted," otherwise print "Access denied."

a=int(input("Enter the password : "))
predefined=12345
if a==predefined:
    print("Access Granted")
else:
    print("Access Denied")


#5. Write a program that takes a year as input and checks if it is a leap year. A year is a leap year if it is divisible by 4 but not by 100, unless it is also divisible by 400.

a=int(input("Enter the year  : "))
if (a%4==0 and a%100!=0) or (a%400==0):
    print("This Year is Leap Year")
else:
    print("This is not a Leap Year")

#6. Write a program that takes a month as input (1-12) and prints the season it falls in:
#December, January, February: Winter
#March, April, May: Spring
#June, July, August: Summer
#September, October, November: Fall


a = int(input("Enter a month number (1-12): "))

if a < 1 or a > 12:
    print("Please enter a valid month number between 1 and 12.")
else:
    if a == 12 or a == 1 or a == 2:
        print("Winter")
    elif a == 3 or a == 4 or a == 5:
        print("Spring")
    elif a == 6 or a == 7 or a == 8:
        print("Summer")
    else:
        print("Fall")


#7. Create a program that takes three integers as input and determines the largest number. If two or more numbers are equal and the largest, indicate this in the output.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


if a > b and a > c:
    print(f"The largest number is a: {a}.")
elif b > a and b > c:
    print(f"The largest number is b: {b}.")
elif c > a and c > b:
    print(f"The largest number is c: {c}.")
else:
    if a == b == c:
        print("All three numbers are equal.")
    elif a == b and a > c:
        print(f"The largest numbers are a: {a} and b: {b}, which are equal.")
    elif a == c and a > b:
        print(f"The largest numbers are a: {a} and c: {c}, which are equal.")
    elif b == c and b > a:
        print(f"The largest numbers are b: {b} and c: {c}, which are equal.")


#8. Write a program that takes an integer input from the user and checks if it is within the range of 1 to 100. If it is, then check if it is even or odd. Print appropriate messages for each condition.

a = int(input("Enter a number: "))

if a < 1 or a > 100:
    print("Please enter a valid number between 1 and 100.")
else:
    if a % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")








