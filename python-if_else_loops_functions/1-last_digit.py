#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# if number < 0:         #solution initiale
#    number = number * -1
#    digit = number % 10
#    number = number * -1
#    digit = digit * -1
# else:
#    digit = number % 10
if number >= 0:  # solution de cécile
    digit = number % 10
else:
    digit = -(abs(number) % 10)
if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
