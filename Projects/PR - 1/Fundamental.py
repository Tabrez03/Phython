print("Welcome to Interactive Personal Data collecter!\n")

name = input("Please enter your name :")
age = input("Enter your age:")
height = input("please enter your height in meter :")
number = input("please enter your Fevorite number :")


print("\n Thank you! here is the  information we collected\n")

y=2026-int(age)

print("Name:",name ,("Type:" ,type(name),"memory address:",id(name)))

print("Age:",age ,("Type:" ,type(age),"memory address:",id(age)))

print("Height:",height ,("Type:" ,type(height),"memory address:",id(height)))

print("Number:",number ,("Type:" ,type(number),"memory address:",id(number)))

print("Your birth year is approximately:",y ,("based on your age of",age))