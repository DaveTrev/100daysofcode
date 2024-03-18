print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combined_couple = name1 + name2
lower_couple = combined_couple.lower()
t = lower_couple.count("t")
r = lower_couple.count("r")
u = lower_couple.count("u")
e = lower_couple.count("e")
first_digit = t + r + u + e

l = lower_couple.count("l")
o = lower_couple.count("o")
v = lower_couple.count("v")
e = lower_couple.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")