#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 5:
    print(f"Last digit of {number} > 5")
elif number == 0:
    print("{number} 0")
elif number < 6:
    print(f"Last digit of {number} < 6 not 0")

print(number)

