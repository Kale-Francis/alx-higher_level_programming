#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 5:
    print(f"Last digit of {number} is greater than 5")
elif number == 0:
    print("{number} is 0")
elif number < 6:
    print(f"Last digit of {number} is less than 6 and not 0")

print(number)

