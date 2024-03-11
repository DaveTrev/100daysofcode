
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
       print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


# # Which number do you want to check?
# number = int(input())
# # If the number can be divided by 2 with 0 remainder.
# if number % 2 == 0:
#   print("This is an even number.")
# # Otherwise (number cannot be divided by 2 with 0 remainder).
# else:
#   print("This is an odd number.")


##BMI CALC
# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = weight / (height * height)

# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25.0:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")

# leap year check
# Which year do you want to check?
# year = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year ")

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? "S", "M", or "L"
# add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
# extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# # Your code below this line 👇
# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1

# print(f"Your final bill is: ${bill}.")