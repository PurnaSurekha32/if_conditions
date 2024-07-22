
# Write a program that prints an action based on the traffic light colour

a=input("Enter the color: ")
if a=="RED" or a=="red":
    print("Stop")
elif a=="YELLOW" or a=="yellow":
    print("Prepare to go")
elif a=="GREEN" or a=="green":
    print("Go")
else:
    print("Valid Colour")

#Write a program to classifies a person's Body Mass Index(BMI) based on their BMI value

a=float(input("Enter your BMI : "))
if a<18.5:
    print("Under Weight")
elif a>=18.5 and a<=24.9:
    print("Normal Weight")
elif a>=25 and a<=29.9:
    print("Over Weight")
elif a>30:
    print("Obese")


#Write a program that takes a string input from the user and chacks if it's length is greater than 5 char.

a=input("Enter a String : ")
b=len(a)
if b>5:
    print("The string is more that 5 character")
    

# Write a program that takes a person's age as input and prints their ticket price

a=int(input("Enter your age : "))
if a<3:
    print("Free")
elif a>=3 and a<=12:
    print("$10")
else:
    print("$15")


# Write a Python program that takes a student's score as input and prints out their corresponding grade based on the following criteria:
#90 and above: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F

a=int(input("Enter the score :"))
if a>=90:
    print("Grade A")
elif a>=80 and a<=89:
    print("Grade B")
elif a>=70 and a<=79:
    print("Grade C")
elif a>=60 and a<=69:
    print("Grade D")
else:
    print("Grade F")


# Write a Python program that takes a single character as input and prints out whether it is a vowel or a consonant.

a=input("Enter a Letter :")
if a=="a" or a=="A":
    print("Vowel")
elif a=="e" or a=="E":
    print("Vowel")
elif a=="I" or a=="i":
    print("Vowel")
elif a=="O" or a=="o":
    print("Vowel")
elif a=="U" or a=="u":
    print("Vowel")
else:
    print("Not a Vowel")


#Write a program that asks for an applicant's monthly income and credit score. First, check if the monthly income is above $3000. If it is, then check if the credit score is above 650. Print appropriate messages for each condition.

a=int(input("Enter your monthly Income : "))
b=int(input("Enter your Credit Score : "))
if a>3000 :
    if b>650:
        print("Loan is Approved")
    else:
        print("Loan is not Approved")
else:
    print("Loan Not Approve")






