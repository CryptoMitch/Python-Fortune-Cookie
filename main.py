# Project 1: Fortune Cookie from Python for Non-Programmers Course

# Instructor: Nick Walter

# Helpful Resources: https://www.w3schools.com/python/

import random

# Introduce Randomness Via an Integer
fortune_number = random.randint(1,8)

lucky_number = random.randint(15,99)

fortune_text = ""

# Introduce Randomness Via a Float
# print(random.random())

if fortune_number == 1:
  fortune_text = "You might encounter thunderstorms."

if fortune_number == 2:
  fortune_text = "You will love what happens today."

if fortune_number == 3:
  fortune_text = "Today will be a day you never forget..."

if fortune_number == 4:
  fortune_text = "Today will reveal hidden truths about someone."

if fortune_number == 5:
  fortune_text = "Today will change your future forever."
  
if fortune_number == 6:
  fortune_text = "Today will not go as planned."

if fortune_number == 7:
  fortune_text = "Today may come with a surprise ending."

if fortune_number == 8:
  fortune_text = "Today will be great."

# I tried if, elif and else and it didn't work, but if, if, if worked.

print(f"{fortune_text} Your lucky number is {lucky_number}")
